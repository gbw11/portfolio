<script setup>
</script>

<template>
  <div>
    <!-- 네비게이션 -->
    <nav style="background: #2c3e50; padding: 16px 40px; display: flex; gap: 24px;">
      <RouterLink to="/" style="color: white; text-decoration: none; font-weight: bold;">
        🏅 스포츠 대시보드
      </RouterLink>
      <RouterLink to="/free" style="color: white; text-decoration: none; font-weight: bold;">
        ✈️ 여행 대시보드
      </RouterLink>
    </nav>

    <!-- 페이지 렌더링 -->
    <RouterView />
  </div>
</template>