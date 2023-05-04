<template>
  <div class="homebrand">
    <div class="title">Thương Hiệu Chính Hãng <img class="icon-title" src="https://salt.tikicdn.com/ts/tka/71/61/5d/dee57a81920f1f4e4dcc3b5878d9bfed.png" alt="icon-title" width="70" height="16"></div>

    <div class="image-container">
      <div v-for="(ele, index) in IMAGE_URL_LIST" :key="index" class="image-wrapper">
        <img :src="ele" alt="Image" class="image">
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      IMAGE_URL_LIST: [
        "https://salt.tikicdn.com/ts/tikimsp/d6/ca/d8/f17842294bc50a72d10a3f4cccad06ea.png",
        "https://salt.tikicdn.com/ts/tikimsp/ee/13/02/935f92fc47588c0e8f86b1f93e44455b.png",
        "https://salt.tikicdn.com/ts/tikimsp/a5/f0/a8/60980d75a063dca3e839808a067f1a59.png",
        "https://salt.tikicdn.com/ts/tikimsp/12/15/fd/5412899fd893c1b2fe0e47c3cd9c91a8.png",
        "https://salt.tikicdn.com/ts/tikimsp/cd/69/dc/5dfc18f054da8ceedea227e43fa0e867.png",
        "https://salt.tikicdn.com/ts/tikimsp/81/4d/0b/b63465ef484caff2ff01e130bb51cbe2.png"
      ]
    }
  }
}
</script>
<style lang="scss" scoped>
  .homebrand {
    margin-top: 16px;
    padding: 12px 16px;
    background: linear-gradient(rgba(255, 255, 255, 0) 22.49%, rgb(255, 255, 255) 73.49%), linear-gradient(264.03deg, rgb(220, 229, 251) -10.27%, rgb(234, 236, 255) 35.65%, rgb(213, 236, 253) 110.66%);
    border-radius: 8px;
    min-height: 278px;
    width: 1138px;

    .title {
      margin-bottom: 12px;
      font-weight: 700;
      font-size: 16px;
      line-height: 150%;
      color: rgb(39, 39, 42);

      .icon-title {
        margin-left: 8px;
      }
    }

    .image-container {
      display: flex;
      .image-wrapper {
        padding: 0px 8px;
        .image {
          width: 169px;
          height: 255.5px;

          border: 1px solid rgba(0, 0, 0, 0.05);
          border-radius: 8px;
          cursor: pointer;
          overflow: hidden;
        }
      }
    }


  }
</style>
