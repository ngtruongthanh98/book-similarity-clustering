<template>
  <div class="navbar">
    <div class="navbar-main">
      <div class="navbar-main__left">
        <img class="tiki-logo" src="/tiki-logo-brand.png" alt="Tiki logo" height="40" width="57">

        <SearchInput/>
      </div>
      <div class="navbar-main__right">Right</div>
    </div>
  </div>
</template>

<script>
import SearchInput from '../SearchInput/index.vue'

export default {
  components: {
    SearchInput
  }
}
</script>
<style lang="scss">
.navbar {
  height: 88px;
  padding: 8px 0px;

  display: flex;
  flex-direction: column;
  align-items: center;

  background: #ffffff;

  &-main {
    display: flex;
    justify-content: space-between;

    &__left {
      display: flex;
      align-items: center;

      .va-input-wrapper__prepend-inner {
        margin-left: 18px;
      }


      .tiki-logo {
        margin-right: 48px;
      }
    }

    &__right {
    }
  }
}
</style>
