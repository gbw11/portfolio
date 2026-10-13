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

const props = defineProps({
  data: { type: Array, default: () => [] }
})

const chartData = ref(null)

const chartOptions = {
  responsive: true,
  indexAxis: 'y',  // 가로 막대
  plugins: {
    legend: { position: 'top' },
    title: {
      display: true,
      text: '여행지별 평균 비용 및 만족도'
    }
  },
  scales: {
    x: {
      type: 'linear',
      position: 'bottom',
      title: { display: true, text: '평균 비용 (원)' }
    },
    x2: {
      type: 'linear',
      position: 'top',
      title: { display: true, text: '만족도' },
      min: 0,
      max: 5,
      grid: { drawOnChartArea: false }
    }
  }
}

watch(() => props.data, (newData) => {
  if (!newData.length) return

  const labels = newData.map(d => d.destination)
  const costs = newData.map(d => d.average_cost_krw)
  const ratings = newData.map(d => d.satisfaction_rating)

  chartData.value = {
    labels,
    datasets: [
      {
        label: '평균 비용 (원)',
        data: costs,
        backgroundColor: 'rgba(54, 162, 235, 0.7)',
        xAxisID: 'x'
      },
      {
        label: '만족도',
        data: ratings,
        backgroundColor: 'rgba(255, 99, 132, 0.7)',
        xAxisID: 'x2'
      }
    ]
  }
}, { immediate: true })
</script>

<template>
  <div>
    <Bar v-if="chartData" :data="chartData" :options="chartOptions" />
    <p v-else>데이터 로딩 중...</p>
  </div>
</template>