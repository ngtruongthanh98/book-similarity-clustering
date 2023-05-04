<template>
  <div class="universal-free-ship">
    <div class="item-wrapper">
      <img src="https://salt.tikicdn.com/ts/upload/5e/ec/fb/150f3c633781ed1da9921e45db90c62d.png" alt="free-ship" width="81" height="12">
      <strong class="title">
        mỗi ngày, tự động áp dụng không cần săn mã
      </strong>
      <img class="arrow-icon" src="https://salt.tikicdn.com/ts/upload/51/20/3f/1bb77cdb828972a5284a06dac79c0afc.png" alt="arrow" width="7" height="11">
    </div>
  </div>
</template>
<script>
export default {

}
</script>
<style lang="scss">
  .universal-free-ship {
    display: flex;
    justify-content: center;

    background-color: rgb(255, 232, 128);

    position: relative;
    z-index: 1;
    display: flex;
    padding: 8px 16px;
    gap: 4px;
    border-width: 1px 0px;
    border-style: solid;
    border-color: rgb(235, 235, 240);

    .item-wrapper {
      display: flex;
      align-items: center;

      .title {
        font-size: 14px;
        line-height: 150%;
        padding-left: 4px;
        color: rgb(39, 39, 42);
      }

      .arrow-icon {
        margin-left: 4px;
      }
    }
  }
</style>
