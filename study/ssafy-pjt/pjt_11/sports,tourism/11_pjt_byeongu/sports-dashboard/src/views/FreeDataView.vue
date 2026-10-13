<script setup>
import { ref, computed, onMounted } from 'vue'
import { loadTourismData } from '../utils/dataLoader.js'
import TourismCompareChart from '../components/charts/TourismCompareChart.vue'
import TourismSeasonChart from '../components/charts/TourismSeasonChart.vue'
import TourismBubbleChart from '../components/charts/TourismBubbleChart.vue'

const allData = ref([])
const selectedType = ref('전체')
const selectedSeason = ref('전체')

// 여행 타입 목록 추출
const typeOptions = computed(() => {
  const types = new Set()
  allData.value.forEach(item => {
    item.type.split(',').map(t => t.trim()).forEach(t => types.add(t))
  })
  return ['전체', ...types]
})

// 성수기 목록 추출
const seasonOptions = computed(() => {
  const seasons = new Set()
  allData.value.forEach(item => {
    item.peak_season.split(',').map(s => s.trim()).forEach(s => seasons.add(s))
  })
  return ['전체', ...seasons]
})

// 필터링된 데이터
const filteredData = computed(() => {
  return allData.value.filter(item => {
    const typeMatch = selectedType.value === '전체' ||
      item.type.split(',').map(t => t.trim()).includes(selectedType.value)

    const seasonMatch = selectedSeason.value === '전체' ||
      item.peak_season.split(',').map(s => s.trim()).includes(selectedSeason.value)

    return typeMatch && seasonMatch
  })
})

onMounted(async () => {
  allData.value = await loadTourismData()
})
</script>

<template>
  <div style="max-width: 1200px; margin: 40px auto; padding: 0 20px;">
    <h1>✈️ 여행/관광 데이터 대시보드</h1>

    <!-- 인터랙티브 필터 (F312) -->
    <div class="filter-bar">
      <label>
        여행 타입:
        <select v-model="selectedType">
          <option v-for="t in typeOptions" :key="t" :value="t">{{ t }}</option>
        </select>
      </label>
      <label>
        성수기:
        <select v-model="selectedSeason">
          <option v-for="s in seasonOptions" :key="s" :value="s">{{ s }}</option>
        </select>
      </label>
      <span class="count">{{ filteredData.length }}개 여행지</span>
    </div>

    <!-- 요약 카드 -->
    <div class="summary-cards">
      <div class="card">
        <p class="card-label">총 여행지</p>
        <p class="card-value">{{ filteredData.length }}곳</p>
      </div>
      <div class="card">
        <p class="card-label">평균 비용</p>
        <p class="card-value">
          {{
            filteredData.length
              ? (filteredData.reduce((a, b) => a + b.average_cost_krw, 0) / filteredData.length)
                  .toLocaleString('ko-KR', { maximumFractionDigits: 0 })
              : 0
          }}원
        </p>
      </div>
      <div class="card">
        <p class="card-label">평균 만족도</p>
        <p class="card-value">
          {{
            filteredData.length
              ? (filteredData.reduce((a, b) => a + b.satisfaction_rating, 0) / filteredData.length)
                  .toFixed(2)
              : 0
          }} / 5.0
        </p>
      </div>
      <div class="card">
        <p class="card-label">총 방문자 수</p>
        <p class="card-value">
          {{
            filteredData.length
              ? (filteredData.reduce((a, b) => a + b.number_of_visitors, 0))
                  .toLocaleString()
              : 0
          }}명
        </p>
      </div>
    </div>

    <!-- 차트 그리드 (F311) -->
    <div class="chart-grid">
      <div class="chart-box wide">
        <h3>📊 여행지별 평균 비용 · 만족도 비교</h3>
        <TourismCompareChart :data="filteredData" />
      </div>
      <div class="chart-box">
        <h3>🌸 성수기별 여행지 분포</h3>
        <TourismSeasonChart :data="filteredData" />
      </div>
      <div class="chart-box">
        <h3>🫧 비용 vs 만족도 버블 차트</h3>
        <TourismBubbleChart :data="filteredData" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.filter-bar {
  display: flex;
  gap: 20px;
  align-items: center;
  background: #f0f4ff;
  padding: 16px 20px;
  border-radius: 12px;
  margin-bottom: 24px;
}

.filter-bar select {
  margin-left: 8px;
  padding: 6px 12px;
  border-radius: 8px;
  border: 1px solid #ccc;
  font-size: 14px;
}

.count {
  margin-left: auto;
  font-size: 14px;
  color: #666;
}

.summary-cards {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 24px;
}

.card {
  background: white;
  border-radius: 12px;
  padding: 20px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.card-label {
  font-size: 13px;
  color: #888;
  margin: 0 0 8px 0;
}

.card-value {
  font-size: 22px;
  font-weight: bold;
  color: #333;
  margin: 0;
}

.chart-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

.chart-box {
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.chart-box.wide {
  grid-column: 1 / -1;  /* 전체 너비 차지 */
}

.chart-box h3 {
  margin: 0 0 16px 0;
  font-size: 15px;
  color: #333;
}
</style>