<template>
  <div class="good-price-today">
    <div class="header">
      <div class="header-left">
        <div class="title">Giá tốt hôm nay</div>
        <div class="countdown-container">
          <span>04</span>
          <b>:</b>
          <span>48</span>
          <b>:</b>
          <span>40</span>
        </div>
      </div>

      <div class="header-right">
        <div class="name">Xem thêm</div>
        <img class="icon-more" src="https://salt.tikicdn.com/ts/upload/d8/38/d3/4bef23fec35f9fbfa1757d30184ddb9c.png" alt="icon-more">
      </div>
    </div>

    <div class="deal-container">


      <div v-for="(ele, index) in TODAY_DEALS" :key="index" class="discount-item">
        <div class="image-wrapper">
          <img :src="ele.imageUrl" alt="Image" width="145" height="145">

          <img class="tiki-freeship" src="https://salt.tikicdn.com/ts/upload/dc/0d/49/ef9dc5d8164bd62b011e54276502b342.png" alt="tiki-freeship" width="91" height="16">

          <span class="discount">{{ ele.discount }}</span>
        </div>

        <div class="new-price">{{ ele.newPrice }}<sup> {{ ele.unit }}</sup></div>

        <div class="deal-quantity">
          <div class="deal-progress" :style="{ width: ele.progress + '%' }"></div>
          <span class="inner-text">Vừa mới mở bán</span>
        </div>
      </div>


    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      TODAY_DEALS: [
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/22/cb/a9/524a27dcd45e8a13ae6eecb3dfacba7c.jpg.webp',
          discount: '-40%',
          newPrice: '59.000',
          unit: '₫',
          progress: '20'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/90/df/b3/887a5353b09f029b778edaac1dc5684a.jpg.webp',
          discount: '-41%',
          newPrice: '50.000',
          unit: '₫',
          progress: '25'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/d0/04/96/ba43c5e0e7bf36677eca801420b7cda1.png.webp',
          discount: '-40%',
          newPrice: '93.000',
          unit: '₫',
          progress: '15'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/9c/b3/8e/3ff8d70257c97a38d377eeaa564c7f37.jpg.webp',
          discount: '-42%',
          newPrice: '109.000',
          unit: '₫',
          progress: '10'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/06/6e/3a/82b51c0fafcd6a00ec46766773343169.jpg.webp',
          discount: '-25%',
          newPrice: '116.000',
          unit: '₫',
          progress: '10'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/41/70/78/2fe24b310f97f81e927e0238bd6b5726.jpg.webp',
          discount: '-13%',
          newPrice: '210.000',
          unit: '₫',
          progress: '15'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/02/9f/0e/92ac0533439de4351247a5c4fea2a036.jpg.webp',
          discount: '-41%',
          newPrice: '105.000',
          unit: '₫',
          progress: '10'
        }
      ]
    }
  }
}
</script>
<style lang="scss" scoped>
  .good-price-today {
    width: 100%;
    margin-right: 0px;
    margin-top: 16px;
    padding: 12px 16px;
    background-color: rgb(255, 255, 255);
    border-radius: 8px;
    overflow: hidden;
    min-height: 265px;
    width: 1138px;

    .header {
      display: flex;
      justify-content: space-between;
      margin-bottom: 12px;

      &-left {
        display: flex;
        align-items: center;

        .title {
          font-weight: 700;
          font-size: 16px;
          line-height: 150%;
          color: rgb(39, 39, 42);
          margin-right: 12px;
        }

        .countdown-container {
          color: rgb(120, 120, 120);
          font-size: 15px;
          display: flex;
          -webkit-box-align: center;
          align-items: center;

          span {
            font-size: 15px;
            font-weight: 500;
            line-height: 1.6;
            margin: 0px 4px;
            padding: 0px 3px;
            background-color: rgb(255, 66, 78);
            border-radius: 4px;
            color: white;
          }
        }
      }

      &-right {
        display: flex;
        align-items: center;
        cursor: pointer;

        .name {
          font-weight: 500;
          font-size: 14px;
          line-height: 150%;
          color: rgb(10, 104, 255);
        }

        .icon-more {
          width: 24px;
          height: 24px;
          margin-top: -1px;
          margin-left: 8px;
        }
      }
    }

    .deal-container {
      display: flex;

      .discount-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 140px;
        margin: 0px 8px;

        .image-wrapper {
          position: relative;

          .tiki-freeship {
            position: absolute;
            bottom: 0px;
            left: 0px;
          }

          .discount {
            position: absolute;
            top: 4px;
            left: 4px;
            padding: 2px;
            background: rgb(255, 219, 222);
            border-radius: 4px;
            color: rgb(255, 66, 78);
            font-weight: 700;
            font-size: 12px;
            line-height: 150%;
          }
        }

        .new-price {
          text-align: left;
          font-size: 16px;
          line-height: 24px;
          font-weight: 500;
          color: rgb(56, 56, 61);
          margin: 8px 0px;
          display: flex;
          -webkit-box-align: center;
          align-items: center;
          white-space: nowrap;
          color: rgb(255, 66, 78);
        }

        .deal-quantity {
          background-color: rgb(255, 170, 175);
          color: rgb(255, 255, 255);
          border-radius: 10px;
          position: relative;
          display: flex;
          width: 100%;
          height: 20px;

          .deal-progress {
            position: absolute;
            left: 0px;
            top: 0px;
            background-color: rgb(255, 66, 78);
            height: 20px;
            border-radius: 10px;
            min-width: 20px;
          }

          .inner-text {
            font-size: 11px;
            line-height: 16px;
            padding: 0px 0px 0px 6px;
            display: flex;
            -webkit-box-align: center;
            align-items: center;
            -webkit-box-pack: center;
            justify-content: center;
            height: 100%;
            width: 100%;
            position: absolute;
            text-align: center;
          }
        }
      }


    }
  }
</style>
