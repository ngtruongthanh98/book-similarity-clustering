<template>
  <div class="price">
    <h4 class="title">Giá</h4>

    <div class="fast-price-filter">
      <div class="item">
        <span class="">Dưới 40.000</span>
      </div>

      <div class="item">
        <span class="">40.000 -&gt; 120.000</span>
      </div>

      <div class="item">
        <span class="">120.000 -&gt; 280.000</span>
      </div>

      <div class="item">
        <span class="">Trên 280.000</span>
      </div>
    </div>

    <div class="price-small-text">Chọn khoảng giá</div>

    <div class="input-group">
      <input pattern="[0-9]*" placeholder="Giá từ" value="0">
      <span>-</span>
      <input pattern="[0-9]*" placeholder="Giá đến" value="0">
    </div>

    <button>Áp dụng</button>
  </div>
</template>
<script>
export default {

}
</script>
<style lang="scss" scoped>
  .price {
    padding: 0px 16px 12px;
    border-top: 1px solid rgb(247, 247, 247);

    .title {
      margin: 0px;
      line-height: 20px;
      display: block;
      color: rgb(56, 56, 61);
      font-size: 14px;
      padding: 12px 0px;
      font-weight: 500;
    }

    .fast-price-filter {
      .item {
        > span {
          background: rgb(238, 238, 238);
          font-size: 12px;
          padding: 4px 12px;
          line-height: 16px;
          display: inline-block;
          position: relative;
          color: rgb(56, 56, 61);
          border-radius: 12px;
          margin-bottom: 4px;
          cursor: pointer;
        }
      }
    }

    .price-small-text {
      color: rgb(128, 128, 137);
      font-size: 12px;
      padding-bottom: 8px;
      margin-top: 4px;
    }

    .input-group {
      display: flex;
      -webkit-box-align: center;
      align-items: center;

      > input {
        flex: 1 1 0%;
        width: 77px;
        height: 30px;
        padding: 0px 8px;
        background: rgb(255, 255, 255);
        border-radius: 4px;
        text-align: left;
        border: 1px solid rgb(184, 184, 184);
        outline: 0px;
        font-size: 13px;
      }

      > span {
        width: 7px;
        height: 1px;
        font-size: 0px;
        display: inline-block;
        background: rgb(154, 154, 154);
        margin: 0px 4px;
        vertical-align: middle;
      }
    }

    > button {
      background: rgb(255, 255, 255);
      border: 1px solid rgb(11, 116, 229);
      font-size: 12px;
      color: rgb(11, 116, 229);
      padding: 5px 15px;
      width: 100%;
      margin-top: 8px;
      border-radius: 4px;
      cursor: pointer;
    }
  }
</style>
