<script setup>
import { ref, watch } from 'vue'
import { Scatter } from 'vue-chartjs'
import {
  Chart as ChartJS,
  LinearScale,
  PointElement,
  Tooltip,
  Legend,
  Title
} from 'chart.js'

ChartJS.register(LinearScale, PointElement, Tooltip, Legend, Title)

const chartData = ref(null)

const props = defineProps({
  data: {
    type: Array,
    default: () => []
  }
})

const chartOptions = {
  responsive: true,
  plugins: {
    legend: { position: 'top' },
    title: {
      display: true,
      text: '관중 수 vs 시청률 상관관계'
    },
    tooltip: {
      callbacks: {
        label: (ctx) => {
          return `관중: ${ctx.parsed.x.toLocaleString()}명 / 시청률: ${ctx.parsed.y}%`
        }
      }
    }
  },
  scales: {
    x: {
      title: { display: true, text: '관중 수' }
    },
    y: {
      title: { display: true, text: '시청률 (%)' }
    }
  }
}

watch(
  () => props.data,
  (newData) => {
    if (!newData.length) return

    const countMap = {}

    newData.forEach(item => {
      const sport = item.sport_type
      countMap[sport] = (countMap[sport] || 0) + 1
    })

    const labels = Object.keys(countMap)
    const values = Object.values(countMap)

    chartData.value = {
      labels,
      datasets: [
        {
          label: '경기 수',
          data: values,
          backgroundColor: [
            '#FF6384',
            '#36A2EB',
            '#FFCE56',
            '#4BC0C0',
            '#9966FF',
            '#FF9F40'
          ]
        }
      ]
    }
  },
  { immediate: true }
)
</script>

<template>
  <div>
    <Scatter v-if="chartData" :data="chartData" :options="chartOptions" />
    <p v-else>데이터 로딩 중...</p>
  </div>
</template>