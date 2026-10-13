<script setup>
import { ref, watch } from 'vue'
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

const chartData = ref(null)

const props = defineProps({
  data: {
    type: Array,
    default: () => []
  }
})



const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { position: 'top' },
    title: {
      display: true,
      text: '종목별 경기 수'
    }
  }
}

watch(
  () => props.data,
  (newData) => {
    console.log('받은 데이터:', newData)
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
  <div style="height:350px">
    <Bar v-if="chartData" :data="chartData" :options="chartOptions" />
    <p v-else>데이터 로딩 중...</p>
  </div>
</template>