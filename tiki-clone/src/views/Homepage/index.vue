<template>
  <div class="home-page">
    <Sidebar />
  </div>
</template>

<script>
import Sidebar from './Sidebar/index.vue'

export default {
  components: {
    Sidebar
  }
}
</script>
<style lang="scss" scoped>
  .home-page {
    background-color: #f5f5fa;
    min-height: calc(100vh - 80px - 8px);
    padding-top: 16px;
  }
</style>
