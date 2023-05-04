<template>
  <div class="good-price-brand">
    <div class="title">Hàng Thương Hiệu Giá Tốt
</div>

    <div class="image-container">
      <div v-for="(ele, index) in IMAGE_URL_LIST" :key="index" class="image-wrapper">
        <div v-if="ele.isSmall" class="inner-wrapper">
          <img class="image-small" :src="ele.imageUrl" alt="Image">
          <img class="image-small" :src="ele.imageUrl2" alt="Image">
        </div>

        <img v-else :src="ele.imageUrl" alt="Image" class="image"/>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      IMAGE_URL_LIST: [
        {
          imageUrl: 'https://salt.tikicdn.com/ts/tikimsp/4c/17/9c/1d6271dd2922784cf69ec340e64ae44b.png',
          isSmall: false,
        },
        {
          imageUrl: 'https://salt.tikicdn.com/ts/tikimsp/31/d3/e6/3e24522af76c9c58db06533fe9f52e46.png',
          imageUrl2: 'https://salt.tikicdn.com/ts/tikimsp/1e/7a/b9/10ddc4f44c2cd000ba9d216b855d240a.png',
          isSmall: true,
        },
        {
          imageUrl: 'https://salt.tikicdn.com/ts/tikimsp/71/b6/25/229c808ba3654f3549e417df186ba3b6.png',
          isSmall: false
        },
        {
          imageUrl: 'https://salt.tikicdn.com/ts/tikimsp/ac/23/a0/68e01c0e8ac2a2428efda9c47da24de8.png',
          imageUrl2: 'https://salt.tikicdn.com/ts/tikimsp/55/7d/41/284bf09a09977cc57dbb212f968dd42b.png',
          isSmall: true
        },
        {
          imageUrl: 'https://salt.tikicdn.com/ts/tikimsp/27/4e/19/6e347e9531d19e36cb04ba634bbec442.png',
          isSmall: false,
        },
        {
          imageUrl: 'https://salt.tikicdn.com/ts/tikimsp/3e/f8/7b/61761236f31f25933845884b214515d1.png',
          imageUrl2: 'https://salt.tikicdn.com/ts/tikimsp/35/83/ec/50b40ab665f4c01af8efc74991751f0c.png',
          isSmall: true,
        },
      ]
    }
  }
}
</script>
<style lang="scss" scoped>
  .good-price-brand {
    margin-top: 16px;
    padding: 12px 16px;
    background: #ffffff;
    border-radius: 8px;
    min-height: 278px;
    width: 1138px;

    .title {
      margin-bottom: 12px;
      font-weight: 700;
      font-size: 16px;
      line-height: 150%;
      color: rgb(39, 39, 42);
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

        .image-small {
          width: 169px;
          height: 127px;

          border: 1px solid rgba(0, 0, 0, 0.05);
          border-radius: 8px;
          cursor: pointer;
          overflow: hidden;
        }
      }
    }


  }
</style>
