<template>
  <div class="sidebar">
    <SidebarItemGroup title="Nổi bật" :itemList="HOME_SIDEBAR.OUTSTANDING"/>

    <SidebarItemGroup title="Danh mục" :itemList="HOME_SIDEBAR.CATEGORY"/>

    <SidebarItemGroup :itemList="HOME_SIDEBAR.SHOP"/>
  </div>
</template>

<script>
import SidebarItemGroup from './SidebarItemGroup/index.vue'
import { HOME_SIDEBAR } from '../../../constants'

export default {
  components: {
    SidebarItemGroup
  },
  data() {
    return {
      HOME_SIDEBAR
    }
  }
}
</script>
<style lang="scss" scoped>
  .sidebar {
    display: flex;
    flex-direction: column;

    max-height: 100vh;
    position: sticky;
    overflow-y: scroll;
    top: 16px;
    width: 282px;

    &::-webkit-scrollbar {
      display: none;
    }

    .sidebar-item-group {
      margin-bottom: 16px;
    }
  }
</style>
