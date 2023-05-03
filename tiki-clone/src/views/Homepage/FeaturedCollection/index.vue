<template>
  <div class="featured-collection">
    <div class="title">Bộ sưu tập nổi bật</div>

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
        "https://salt.tikicdn.com/ts/brickv2og/d9/f7/25/662c06ed85e459a7e9475fb1c0937881.png",
        "https://salt.tikicdn.com/ts/brickv2og/0c/f9/b8/a7ef4d81e123dbc27f50effe036efaf6.png",
        "https://salt.tikicdn.com/ts/brickv2og/f1/7e/e3/cd47bd0e901a933524603bc6ea426fbf.png",
        "https://salt.tikicdn.com/ts/brickv2og/1c/66/0b/566eb5699b390d4b61529c6f03ea924b.png",
        "https://salt.tikicdn.com/ts/brickv2og/91/cb/28/de8ddf662b816bcc7786673a41339323.png",
        "https://salt.tikicdn.com/ts/brickv2og/ac/6c/8d/3022e6ddee419ded138ea844c65f8c01.png"
      ]
    }
  }
}
</script>
<style lang="scss" scoped>
  .featured-collection {
    margin-top: 16px;
    padding: 12px 16px;
    background: #ffffff;
    border-radius: 8px;
    min-height: 278px;

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
          width: 171px;
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
