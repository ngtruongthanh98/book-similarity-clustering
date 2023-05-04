<template>
  <div class="hightlight-list">
    <div class="title">Danh mục nổi bật</div>

    <div class="image-container">
      <div v-for="(ele, index) in IMAGE_URL_LIST" :key="index" class="image-item">
        <div  class="image-wrapper">
        <img :src="ele.imageUrl" alt="Image" class="image" width="169" height="169">

        <div class="sub-title"><span>{{  ele.name  }}</span></div>
      </div>
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
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/41/11/3a/6c870f4d70da003b599141f1f9be6203.jpg.webp',
          name: 'Giáo Trình Đại Học - Cao Đẳng'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/f3/5d/b2/4bb1e2c5e2d544d06c33079479b58e22.jpg.webp',
          name: 'Triết học'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/37/ac/1c/eb40db51e8203143d9c0b4839046c76a.jpg.webp',
          name: 'Lý Luận Chính Trị'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/d9/e7/c5/1e8879b20f37a74b93bd7b6dd0e64e13.png.webp',
          name: 'Sách tư duy - Kỹ năng sống'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/84/e8/3a/9fa5db012e8a500642367c85202f5497.jpg.webp',
          name: 'Máy đọc sách'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/a6/5a/97/e5b221c15e6636148ddabbd7c2dcb5c0.jpg.webp',
          name: 'Sách hướng nghiệp - Kỹ năng mềm'
        }
      ]
    }
  }
}
</script>
<style lang="scss" scoped>
  .hightlight-list {
    margin-top: 16px;
    padding: 12px 16px;
    background: #ffffff;
    border-radius: 8px;
    min-height: 265px;
    width: 1138px;

    margin-bottom: 48px;

    .title {
      margin-bottom: 12px;
      font-weight: 700;
      font-size: 16px;
      line-height: 150%;
      color: rgb(39, 39, 42);
    }

    .image-container {
      display: flex;
      justify-content: center;

      .image-item {
        padding: 0px 8px;

        .image-wrapper {
          // padding: 0px 8px;
          border: 1px solid rgba(0, 0, 0, 0.05);
          border-radius: 8px;
          cursor: pointer;
          overflow: hidden;
          max-width: 171px;

          .image {
            // width: 169px;
            // height: 255.5px;

            border: 1px solid rgba(0, 0, 0, 0.05);
            border-radius: 8px;
            cursor: pointer;
            overflow: hidden;
          }

          .sub-title {
            padding: 8px;
            font-weight: 600;
            font-size: 12px;
            line-height: 150%;
            color: rgb(39, 39, 42);

            span {
              display: -webkit-box;
              min-height: 18px;
              -webkit-box-orient: vertical;
              -webkit-line-clamp: 1;
              overflow: hidden;
            }
          }
        }
      }
    }
  }
</style>
