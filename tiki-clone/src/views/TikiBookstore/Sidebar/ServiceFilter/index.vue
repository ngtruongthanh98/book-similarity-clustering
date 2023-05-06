<template>
  <div class="service-filter">
    <h4 class="title">Dịch vụ</h4>

    <label data-view-label="Giao siêu tốc 2H">
      <label class="main-item">
        <input type="checkbox">
        <div class="service-wrap">
          <img class="filter-icon" width="78" height="24" src="https://salt.tikicdn.com/ts/upload/b3/21/cf/c6525bcd44b3bb1b793277cc98487799.png" alt="Giao siêu tốc 2H">
          <span>Giao siêu tốc 2H</span>
        </div>
      </label>
    </label>

    <label data-view-label="Giao siêu tốc 2H">
      <label class="main-item">
        <input type="checkbox">
        <div class="service-wrap">
          <img class="filter-icon" width="125" height="24" src="https://salt.tikicdn.com/ts/upload/e9/14/26/52318ad1543ad9d3ee5b633b3df0750d.png" alt="Thưởng thêm Astra">
          <span>Thưởng Thêm Astra</span>
        </div>
      </label>
    </label>

    <label data-view-label="Giao siêu tốc 2H">
      <label class="main-item">
        <input type="checkbox">
        <div class="service-wrap">
          <span>Trả góp 0%</span>
        </div>
      </label>
    </label>


    <label data-view-label="Giao siêu tốc 2H">
      <label class="main-item">
        <input type="checkbox">
        <div class="service-wrap">
          <span>Giảm sâu</span>
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
  .service-filter {
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
