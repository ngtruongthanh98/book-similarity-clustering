<template>
  <div class="providers">
    <h4 class="title">Nhà cung cấp</h4>

    <label data-view-label="Giao siêu tốc 2H">
      <label class="main-item">
        <input type="checkbox">
        <div class="service-wrap">
          <span>Nhà sách Fahasa</span>
        </div>
      </label>
    </label>

    <label data-view-label="Giao siêu tốc 2H">
      <label class="main-item">
        <input type="checkbox">
        <div class="service-wrap">
          <span>Nhà Sách Vĩnh Thụy</span>
        </div>
      </label>
    </label>

    <label data-view-label="Giao siêu tốc 2H">
      <label class="main-item">
        <input type="checkbox">
        <div class="service-wrap">
          <span>info book</span>
        </div>
      </label>
    </label>


    <label data-view-label="Giao siêu tốc 2H">
      <label class="main-item">
        <input type="checkbox">
        <div class="service-wrap">
          <span>HỆ THỐNG NHÀ SÁCH ABC</span>
        </div>
      </label>
    </label>

    <label data-view-label="Giao siêu tốc 2H">
      <label class="main-item">
        <input type="checkbox">
        <div class="service-wrap">
          <span>Times Books</span>
        </div>
      </label>
    </label>

    <a class="toggler">
      Xem thêm
      <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 512 512" color="#0B74E5" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg" style="color: rgb(11, 116, 229);">
        <path d="M256 294.1L383 167c9.4-9.4 24.6-9.4 33.9 0s9.3 24.6 0 34L273 345c-9.1 9.1-23.7 9.3-33.1.7L95 201.1c-4.7-4.7-7-10.9-7-17s2.3-12.3 7-17c9.4-9.4 24.6-9.4 33.9 0l127.1 127z">
        </path>
      </svg>
    </a>

  </div>
</template>
<script>
export default {

}
</script>
<style lang="scss" scoped>
  .providers {
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

    .toggler {
      font-size: 12px;
      font-weight: 500;
      display: flex;
      -webkit-box-align: center;
      align-items: center;
      line-height: 16px;
      color: rgb(11, 116, 229);
      cursor: pointer;

      > svg {
        margin-left: 5.5px;
      }
    }
  }
</style>
