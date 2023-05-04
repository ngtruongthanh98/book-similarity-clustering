<template>
  <div class="promotion-container">
    <Carousel />

    <img src="https://salt.tikicdn.com/cache/w750/ts/tikimsp/6e/ab/79/ec5c7be2e74207acee785972307338f3.png.webp" alt="Promotion image" class="image" width="280" height="280">
  </div>
</template>

<script>
import Carousel from '../../../components/Carousel/index.vue'

export default {
  components: {
    Carousel
  }
}
</script>
<style lang="scss" scoped>
  .promotion-container {
    display: flex;

    .image {
      border-radius: 8px;
      cursor: pointer;
    }
  }
</style>
