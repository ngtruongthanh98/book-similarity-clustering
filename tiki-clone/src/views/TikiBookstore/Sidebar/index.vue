<template>
  <div class="sidebar-bookstore">
    <ProductCategories />
    <LocationWrapper />
    <ServiceFilter />
    <Rating />
    <Brands />
    <Providers />
    <Shipping />
  </div>
</template>

<script>
import ProductCategories from './ProductCategories/index.vue'
import LocationWrapper from './LocationWrapper/index.vue'
import ServiceFilter from './ServiceFilter/index.vue'
import Brands from './Brands/index.vue'
import Rating from './Rating/index.vue'
import Providers from './Providers/index.vue'
import Shipping from './Shipping/index.vue'

export default {
  components: {
    ProductCategories,
    LocationWrapper,
    ServiceFilter,
    Rating,
    Brands,
    Providers,
    Shipping
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
