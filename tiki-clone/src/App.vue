<template>
  <div>
    <Navbar />
    <UniversalFreeShip />
    <router-view />
    <PageFooter v-if="showFooter" />
  </div>
</template>

<script>
import Navbar from './components/Navbar/index.vue';
import UniversalFreeShip from './components/UniversalFreeShip/index.vue';
import PageFooter from './components/PageFooter/index.vue';

export default {
  components: {
    Navbar,
    UniversalFreeShip,
    PageFooter,
  },
  computed: {
    showFooter() {
      return this.$route.name !== "home";
    },
  },
};
</script>
