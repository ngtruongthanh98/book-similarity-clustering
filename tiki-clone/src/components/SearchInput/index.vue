<template>
  <va-input
    v-model="value"
    class="search-input"
    placeholder="Rẻ mỗi ngày, không cần săn sale"
    background="#ffffff"
  >
    <template #prependInner>
      <img src="https://salt.tikicdn.com/ts/upload/33/d0/37/6fef2e788f00a16dc7d5a1dfc5d0e97a.png" alt="search-icon" width="20" height="20">
    </template>

    <template #appendInner>
      <va-button
        preset="secondary"
        hover-opacity="0.3"
        color="rgb(10, 104, 255)"
      >
        Tìm kiếm
      </va-button>
    </template>
  </va-input>
</template>
<script>
export default {

}
</script>
<style lang="scss">
.search-input {
  .va-input-wrapper__field {
    height: 40px;
    width: 680px;
    padding: 0;
    border: 1px solid rgb(221, 221, 227);

    .va-input-wrapper__append-inner {
      background: #ffffff;
    }

    .va-input-wrapper__text {
      border-right: 1px solid rgb(221, 221, 227);
      margin-right: 0;
    }

    .va-button {
      margin-bottom: 0;
      width: 92px;
      height: 40px;

      border-top-left-radius: 0px;
      border-bottom-left-radius: 0px;

      .va-button__content {
        padding: 0;
      }
    }

  }
}
</style>
