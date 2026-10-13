<script setup>
import { ref } from 'vue'

const props = defineProps({
  minDate: String,  // "2023-01"
  maxDate: String   // "2024-12"
})

const emit = defineEmits(['filter'])

const startDate = ref(props.minDate)
const endDate = ref(props.maxDate)

function applyFilter() {
  emit('filter', { start: startDate.value, end: endDate.value })
}
</script>

<template>
  <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 16px;">
    <label>시작 연월:
      <input type="month" v-model="startDate" :min="minDate" :max="maxDate" />
    </label>
    <label>종료 연월:
      <input type="month" v-model="endDate" :min="minDate" :max="maxDate" />
    </label>
    <button @click="applyFilter">필터 적용</button>
  </div>
</template>