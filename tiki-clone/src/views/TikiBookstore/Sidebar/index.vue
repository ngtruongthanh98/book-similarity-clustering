<template>
  <div class="sidebar-bookstore">
    <ProductCategories />
  </div>
</template>

<script>
import ProductCategories from './ProductCategories/index.vue'

export default {
  components: {
    ProductCategories
  }
}
</script>
<style lang="scss" scoped>
  .sidebar-bookstore {
    display: flex;
    flex-direction: column;

    background: rgb(255, 255, 255);
    width: 200px;
    border-radius: 4px 0px 0px 4px;
    overflow: hidden;
  }
</style>
