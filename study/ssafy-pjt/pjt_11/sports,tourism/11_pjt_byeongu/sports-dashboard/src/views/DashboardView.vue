<script setup>
import { ref, onMounted } from 'vue'
import { loadSportsData } from '@/utils/dataLoader.js'
import DateFilter from '@/components/DateFilter.vue'
import SportCountChart from '@/components/charts/SportCountChart.vue'
import SportAvgChart from '@/components/charts/SportAvgChart.vue'
import TimeSeriesChart from '@/components/charts/TimeSeriesChart.vue'
import CorrelationChart from '@/components/charts/CorrelationChart.vue'

const allData = ref([])
const filteredData = ref([])
const minDate = ref('')
const maxDate = ref('')

onMounted(async () => {
  console.log('함수 실행')
  const data = await loadSportsData()
  console.log('로드한 데이터:', data)
  allData.value = data
  filteredData.value = data

  // 전체 데이터의 최소/최대 연월 추출
  const months = data.map(d => d.date.slice(0, 7)).sort()
  minDate.value = months[0]
  maxDate.value = months[months.length - 1]

})

function onFilter({ start, end }) {
  filteredData.value = allData.value.filter(item => {
    const ym = item.date.slice(0, 7)
    return ym >= start && ym <= end
  })
}
</script>

<template>
  <div style="max-width: 1200px; margin: 40px auto; padding: 0 20px;">
    <h1>🏅 스포츠 데이터 대시보드</h1>

    <!-- 날짜 필터 (F306) -->
    <DateFilter
      :minDate="minDate"
      :maxDate="maxDate"
      @filter="onFilter"
    />

    <!-- 대시보드 그리드 (F305) -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
      <div class="chart-box">
        <h3>종목별 경기 수</h3>
        <SportCountChart :data="filteredData" />
      </div>
      <div class="chart-box">
        <h3>종목별 평균 관중·시청률</h3>
        <SportAvgChart :data="filteredData" />
      </div>
      <div class="chart-box">
        <h3>월별 경기 추이</h3>
        <TimeSeriesChart :data="filteredData" />
      </div>
      <div class="chart-box">
        <h3>관중 수 vs 시청률</h3>
        <CorrelationChart :data="filteredData" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.chart-box {
  background: #f9f9f9;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.chart-box h3 {
  margin: 0 0 16px 0;
  font-size: 16px;
  color: #333;
}
</style>