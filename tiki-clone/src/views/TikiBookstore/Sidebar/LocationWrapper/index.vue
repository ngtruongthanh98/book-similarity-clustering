<template>
  <div class="location-wrapper">
    <h4 class="title">Địa chỉ nhận hàng</h4>
    <div class="address">Q. 1, P. Bến Nghé, Hồ Chí Minh</div>
    <div class="address-change">Đổi địa chỉ</div>
  </div>
</template>
<script>
export default {

}
</script>
<style lang="scss" scoped>
  .location-wrapper {
    border-top: 1px solid rgb(235, 235, 240);
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

    .address {
      text-decoration: underline;
      font-size: 12px;
      line-height: 16px;
      font-weight: 400;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      margin-bottom: 4px;
    }

    .address-change {
      color: rgb(11, 116, 229);
      font-size: 12px;
      line-height: 16px;
      font-weight: 500;
      flex-shrink: 0;
      cursor: pointer;
    }
  }
</style>
