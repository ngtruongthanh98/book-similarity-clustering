<template>
  <div class="navbar">
    <div class="navbar-main">
      <div class="navbar-main__left">
        <img class="tiki-logo" src="/tiki-logo-brand.png" alt="Tiki logo" height="40" width="57">

        <SearchInput/>
      </div>
      <div class="navbar-main__right">
        <IconButton buttonName="Trang chủ" imageUrl="https://salt.tikicdn.com/ts/upload/b4/90/74/6baaecfa664314469ab50758e5ee46ca.png" imageUrlActive="https://salt.tikicdn.com/ts/upload/32/56/db/d919a4fea46f498b5f4708986d82009d.png" :isActive="isHomeRoute"/>

        <IconButton buttonName="Astra" imageUrl="https://salt.tikicdn.com/ts/upload/41/28/7d/4713aa0d2855c5c770799f248692f0c5.png" imageUrlActive="https://salt.tikicdn.com/ts/upload/90/77/3e/caed2497697df4ca9b8fba5d92cf6278.png"/>

        <IconButton buttonName="Tài khoản" imageUrl="https://salt.tikicdn.com/ts/upload/07/d5/94/d7b6a3bd7d57d37ef6e437aa0de4821b.png" />

        <div class="cart-zone">
          <div class="divider"></div>

          <IconButton className="cart-wrapper" imageUrlActive="https://salt.tikicdn.com/ts/upload/51/e2/92/8ca7e2cc5ede8c09e34d1beb50267f4f.png" isActive />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SearchInput from '../SearchInput/index.vue'
import IconButton from '../IconButton/index.vue'

export default {
  components: {
    SearchInput,
    IconButton
  },
  computed: {
    isHomeRoute() {
      return this.$route.name === "home";
    },
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
    align-items: center;
    width: 1392px;

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
      margin-left: 48px;
      display: flex;

      .cart-zone {
        display: flex;
        align-items: center;

        .divider {
          width: 1px;
          height: 24px;
          border-right: 1px solid rgb(221, 221, 227);;
          margin-right: 24px;
          margin-left: 24px;
        }

        .cart-wrapper {
          height: 40px;
          width: 40px;
          display: flex;
          justify-content: center;
          align-items: center;
        }
      }
    }
  }
}
</style>
