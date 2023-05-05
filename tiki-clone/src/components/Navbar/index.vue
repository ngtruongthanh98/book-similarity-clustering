<template>
  <div class="navbar">
    <div class="navbar-main">
      <div class="navbar-main__left">
        <img class="tiki-logo" src="/tiki-logo-brand.png" alt="Tiki logo" height="40" width="57" @click="onClickGotoHome">

        <SearchInput/>
      </div>
      <div class="navbar-main__right">
        <IconButton buttonName="Trang chủ" imageUrl="https://salt.tikicdn.com/ts/upload/b4/90/74/6baaecfa664314469ab50758e5ee46ca.png" imageUrlActive="https://salt.tikicdn.com/ts/upload/32/56/db/d919a4fea46f498b5f4708986d82009d.png" :isActive="isHomeRoute" @click="onClickGotoHome"/>

        <IconButton buttonName="Astra" imageUrl="https://salt.tikicdn.com/ts/upload/41/28/7d/4713aa0d2855c5c770799f248692f0c5.png" imageUrlActive="https://salt.tikicdn.com/ts/upload/90/77/3e/caed2497697df4ca9b8fba5d92cf6278.png"/>

        <IconButton buttonName="Tài khoản" imageUrl="https://salt.tikicdn.com/ts/upload/07/d5/94/d7b6a3bd7d57d37ef6e437aa0de4821b.png" />

        <div class="cart-zone">
          <div class="divider"></div>

          <IconButton className="cart-wrapper" imageUrlActive="https://salt.tikicdn.com/ts/upload/51/e2/92/8ca7e2cc5ede8c09e34d1beb50267f4f.png" isActive />
        </div>
      </div>
    </div>

    <div class="navbar-sub">
      <div class="navigate-container">
        <div v-for="(item, index) in recommendList" :key="index" class="item">
          {{ item }}
        </div>
      </div>

      <div class="address-container">
        <img class="location-icon" src="https://salt.tikicdn.com/ts/upload/88/5c/9d/f5ee506836792eb7775e527ef8350a44.png" alt="Location" width="20" height="20" />

        <div class="title">Giao đến:</div>

        <div class="address">H. Nhà Bè, X. Phước Kiển, Hồ Chí Minh</div>
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
  data() {
    return {
      ITEM_LIST: [
        'trái cây',
        'thịt, trứng',
        'rau củ quả',
        'sữa, bơ, phô mai',
        'hải sản',
        'gạo, mì ăn liền',
        'đồ uống, bia rượu',
        'bánh kẹo'
      ],
      ITEM_LIST_BOOKS: [
        'cây cam ngọt của tôi',
        'triết học',
        'nguyễn nhật ánh',
        'không gia đình',
        'vẻ đẹp của sự cô đơn',
        'tâm lý học',
        'hiểu về trái tim'
      ]
    }
  },
  computed: {
    isHomeRoute() {
      return this.$route.name === "home";
    },
    recommendList() {
      if(this.$route.name === 'home') {
        return this.ITEM_LIST
      }

      return this.ITEM_LIST_BOOKS
    }
  },
  methods: {
    onClickGotoHome() {
      this.$router.push({ name: 'home' });
    }
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
        cursor: pointer;
      }
    }

    &__right {
      display: flex;
      justify-content: end;

      .cart-zone {
        display: flex;
        align-items: center;

        .divider {
          width: 1px;
          height: 24px;
          border-right: 1px solid rgb(221, 221, 227);;
          margin-right: 12px;
          margin-left: 12px;
        }

        .cart-wrapper {
          height: 40px;
          width: 40px;
          display: flex;
          justify-content: center;
          align-items: center;

          .icon {
            margin-right: 0;
          }
        }
      }
    }
  }

  &-sub {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 1392px;

    .navigate-container {
      display: flex;
      width: 872px;
      margin-left: 105px;
      margin-top: 8px;
      align-items: flex-start;
      flex-wrap: wrap;
      overflow: hidden;

      .item {
        margin-right: 8px;
        display: block;
        font-weight: 400;
        font-size: 14px;
        line-height: 150%;
        color: rgb(128, 128, 137);
        margin-right: 12px;
        white-space: nowrap;

        cursor: pointer;
      }
    }

    .address-container {
      display: flex;
      margin-top: 8px;
      width: 350px;

      .location-icon {
        margin-right: 4px;
      }

      .title {
        color: rgb(128, 128, 137);
        font-weight: 400;
        font-size: 14px;
        line-height: 150%;
        padding-right: 4px;
      }

      .address {
        text-decoration: underline;
        font-weight: 600;
        font-size: 14px;
        line-height: 150%;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        color: rgb(39, 39, 42);

        cursor: pointer;
      }
    }
  }
}
</style>
