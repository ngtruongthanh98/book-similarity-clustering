<template>
  <div class="sidebar-item">
    <img class="image" :src="imageUrl" alt="Logo" height="32" width="32">

    <div class="name">{{ itemName }}</div>
  </div>
</template>
<script>
export default {
  props: {
    imageUrl: {
      type: String,
      default: ''
    },
    itemName: {
      type: String,
      default: ''
    }
  }
}
</script>
<style lang="scss" scoped>
  .sidebar-item {
    display: flex;
    align-items: center;

    padding: 7px 16px;

    &:hover {
      background-color: #f5f5fa;
      border-radius: 8px;
      cursor: pointer;
      transition: all 0.3s ease 0s;
    }

    .image {
      margin-right: 8px;
    }

    .name {
      font-weight: 400;
      font-size: 14px;
      line-height: 150%;
      color: rgb(39, 39, 42);
    }
  }
</style>
