<template>
  <div class="product-categories">
    <h4 class="title">Danh Mục Sản Phẩm</h4>

    <div class="list">
      <div v-for="(ele, index) in PRODUCT_LISTS" :key="index" class="list-item">
        {{ ele.name }}
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      PRODUCT_LISTS: [
        {
          name: 'English Books',
        },
        {
          name: 'Sách tiếng Việt'
        },
        {
          name: 'Văn phòng phẩm'
        },
        {
          name: 'Quà lưu niệm'
        }
      ]
    }
  }
}
</script>
<style lang="scss" scoped>
  .product-categories {
    padding: 0px 16px 12px;

    .title {
      margin: 0px;
      line-height: 20px;
      display: block;
      color: rgb(56, 56, 61);
      font-size: 14px;
      padding: 12px 0px;
      font-weight: 500;
    }

    .list {
      &-item {
        font-size: 12px;
        font-weight: 400;
        color: rgb(56, 56, 61);
        padding: 0px 0px 12px;
        line-height: 16px;
        display: flex;
        -webkit-box-align: center;
        align-items: center;
        cursor: pointer;
      }
    }
  }
</style>
