import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '@/views/DashboardView.vue'
import FreeDataView from '@/views/FreeDataView.vue'
const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: DashboardView
    },
    {
      path: '/free',
      component: FreeDataView
    }
  ]
})

export default router