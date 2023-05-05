<script setup>
import Navbar from './components/Navbar/index.vue'
import UniversalFreeShip from './components/UniversalFreeShip/index.vue'
import PageFooter from './components/PageFooter/index.vue'

</script>

<template>
  <Navbar />
  <UniversalFreeShip />
  <router-view />
  <PageFooter />
</template>

<style scoped>
</style>
