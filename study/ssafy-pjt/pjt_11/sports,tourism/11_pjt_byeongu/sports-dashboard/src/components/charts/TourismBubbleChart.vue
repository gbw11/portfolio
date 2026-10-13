<script setup>
import { ref, watch } from 'vue'
import { Bubble } from 'vue-chartjs'
import {
  Chart as ChartJS,
  LinearScale,
  PointElement,
  Tooltip,
  Legend,
  Title
} from 'chart.js'

ChartJS.register(LinearScale, PointElement, Tooltip, Legend, Title)

const props = defineProps({
  data: { type: Array, default: () => [] }
})

const chartData = ref(null)

const chartOptions = {
  responsive: true,
  plugins: {
    legend: { position: 'top' },
    title: {
      display: true,
      text: '비용 vs 만족도 (버블 크기 = 방문자 수)'
    },
    tooltip: {
      callbacks: {
        label: (ctx) => {
          const raw = ctx.raw
          return [
            `여행지: ${raw.label}`,
            `평균 비용: ${raw.x.toLocaleString()}원`,
            `만족도: ${raw.y}`,
            `방문자 수: ${raw.visitors.toLocaleString()}명`
          ]
        }
      }
    }
  },
  scales: {
    x: {
      title: { display: true, text: '평균 비용 (원)' }
    },
    y: {
      title: { display: true, text: '만족도' },
      min: 3.5,
      max: 5.0
    }
  }
}

watch(() => props.data, (newData) => {
  if (!newData.length) return

  const points = newData.map(item => ({
    x: item.average_cost_krw,
    y: item.satisfaction_rating,
    r: Math.sqrt(item.number_of_visitors) / 800,  // 버블 크기 조정
    label: item.destination,
    visitors: item.number_of_visitors
  }))

  chartData.value = {
    datasets: [
      {
        label: '여행지',
        data: points,
        backgroundColor: 'rgba(54, 162, 235, 0.5)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      }
    ]
  }
}, { immediate: true })
</script>

<template>
  <div>
    <Bubble v-if="chartData" :data="chartData" :options="chartOptions" />
    <p v-else>데이터 로딩 중...</p>
  </div>
</template>