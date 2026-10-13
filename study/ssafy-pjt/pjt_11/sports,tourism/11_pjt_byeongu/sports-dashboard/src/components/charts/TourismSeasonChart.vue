<script setup>
import { ref, watch } from 'vue'
import { Doughnut } from 'vue-chartjs'
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
  Title
} from 'chart.js'

ChartJS.register(ArcElement, Tooltip, Legend, Title)

const props = defineProps({
  data: { type: Array, default: () => [] }
})

const chartData = ref(null)

const chartOptions = {
  responsive: true,
  plugins: {
    legend: { position: 'right' },
    title: {
      display: true,
      text: '성수기별 여행지 분포'
    },
    tooltip: {
      callbacks: {
        label: (ctx) => {
          const label = ctx.label
          const value = ctx.parsed
          const total = ctx.dataset.data.reduce((a, b) => a + b, 0)
          const percent = ((value / total) * 100).toFixed(1)
          return `${label}: ${value}곳 (${percent}%)`
        }
      }
    }
  }
}

watch(() => props.data, (newData) => {
  if (!newData.length) return

  // 성수기별 여행지 수 집계
  // peak_season이 "봄, 가을" 처럼 복수일 수 있어서 분리해서 처리
  const seasonMap = {}
  newData.forEach(item => {
    const seasons = item.peak_season.split(',').map(s => s.trim())
    seasons.forEach(season => {
      seasonMap[season] = (seasonMap[season] || 0) + 1
    })
  })

  const labels = Object.keys(seasonMap)
  const values = Object.values(seasonMap)

  chartData.value = {
    labels,
    datasets: [
      {
        data: values,
        backgroundColor: [
          '#FF6384',  // 봄
          '#36A2EB',  // 여름
          '#FFCE56',  // 가을
          '#4BC0C0',  // 겨울
          '#9966FF'   // 기타
        ],
        hoverOffset: 8
      }
    ]
  }
}, { immediate: true })
</script>

<template>
  <div>
    <Doughnut v-if="chartData" :data="chartData" :options="chartOptions" />
    <p v-else>데이터 로딩 중...</p>
  </div>
</template>