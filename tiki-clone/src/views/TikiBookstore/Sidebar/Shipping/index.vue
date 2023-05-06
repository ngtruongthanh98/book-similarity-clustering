<template>
  <div class="shipping">
    <h4 class="title">Giao hàng</h4>

    <label data-view-label="Giao siêu tốc 2H">
      <label class="main-item">
        <input type="radio">
        <div class="service-wrap">
          <span>Hàng Nội Địa</span>
        </div>
      </label>
    </label>

    <label data-view-label="Giao siêu tốc 2H">
      <label class="main-item">
        <input type="radio">
        <div class="service-wrap">
          <span>Hàng Quốc Tế</span>
        </div>
      </label>
    </label>

  </div>
</template>
<script>
export default {

}
</script>
<style lang="scss" scoped>
  .shipping {
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

    > label {
      display: flex;
      -webkit-box-align: center;
      align-items: center;
      font-size: 12px;
      line-height: 16px;
      text-transform: capitalize;
      margin-bottom: 12px;
      color: rgb(56, 56, 61);

      .main-item {
        display: flex;
        align-items: center;
      }

      > label {
        margin-right: 2px;
        width: 100%;
        align-items: flex-start;
        display: flex;
        cursor: pointer;
        -webkit-box-align: center;

        > input {
          // display: none;
          margin-right: 2px;
        }

        > span {
          margin: 0px 12px 0px 0px;
        }

        .service-wrap {
          display: flex;
          -webkit-box-align: center;
          align-items: center;
          min-height: 16px;
          flex: 1 1 0%;
          flex-wrap: wrap;
          gap: 4px;

          margin-left: 8px;

          > img {
            max-height: 10px;
            width: auto;
          }

          > span {
            position: relative;
          }
        }
      }
    }
  }
</style>
