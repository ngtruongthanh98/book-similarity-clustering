<template>
  <div class="sidebar-item-group">
    <div class="title">{{ title }}</div>

    <SidebarItem v-for="(ele, index) in itemList" :key="index" :imageUrl="ele.imageUrl" :itemName="ele.itemName"/>
  </div>
</template>

<script>
import SidebarItem from './SidebarItem/index.vue'

export default {
  components: {
    SidebarItem
  },
  props: {
    title: {
      type: String,
      default: "",
    },
    itemList: {
      type: Array,
      default: [],
    }
  }
}
</script>
<style lang="scss" scoped>
.sidebar-item-group {
  background-color: #ffffff;
  width: 230px;

  display: flex;
  flex-direction: column;
  justify-content: center;

  padding: 8px 12px;
  border-radius: 8px;

  .title {
    margin-bottom: 8px;
    padding-left: 16px;
    font-weight: 700;
    font-size: 14px;
    line-height: 150%;
    color: rgb(39, 39, 42);
  }
}
</style>
