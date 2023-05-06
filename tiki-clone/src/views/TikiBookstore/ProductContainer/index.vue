<template>
  <div class="product-container">
    <div class="product-container__body">
      <div class="content">

        <div v-for="(ele, index) in PRODUCT_LIST" :key="index" class="product-item" @click="onClickProductDetail(ele.productId)">
          <div class="styled-item">
            <div class="thumbnail">
              <img class="official-image" src="https://salt.tikicdn.com/ts/upload/5d/4c/f7/0261315e75127c2ff73efd7a1f1ffdf2.png" alt="Official" width="68" height="14">

              <div class="thumbnail-wrapper">
                <img :src="ele.imageUrl" alt="Product image" width="183" height="183">
              </div>

            </div>

            <div class="description-wrapper">
              <div class="info">
                <div class="name">{{ ele.name }}</div>

                <div class="rate-wrapper">
                  <div class="full-rating">
                    <span class="score">{{ ele.score }}</span>

                    <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" size="14" color="#fdd836" height="14" width="14" xmlns="http://www.w3.org/2000/svg" style="color: rgb(253, 216, 54);"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"></path></svg>
                  </div>

                  <div class="sold-amount">
                    <div class="divider"></div>
                    <div class="quantity">Đã bán {{ ele.quantity }}</div>
                  </div>
                </div>

                <div class="price-discount has-discount">
                  <div class="price-discount__price">{{ ele.price }} ₫</div>
                  <div class="price-discount__discount">-{{ele.discount}}%</div>
                </div>

                <div class="badge-under-price">
                  Tặng tới {{ ele.backAmount }} ASA ({{ ele.backAmountPrice }} ₫)
                  <br>
                  ≈ 0.5% hoàn tiền
                </div>

                <div class="badge-under-rating"></div>
              </div>
            </div>

            <div class="badge-delivery">
              <img src="https://salt.tikicdn.com/ts/upload/bf/5b/b9/f54345d674f86ab1bc3f8a68e91ee049.png" alt="Now" width="32" height="16">

              <span>Giao siêu tốc 2H</span>
            </div>
          </div>
        </div>
      </div>

      <div class="view-more-button">
        Xem Thêm
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      PRODUCT_LIST: [
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/7c/e3/95/dae5605536e6c8b9bd8073e6482b0335.jpg.webp',
          name: 'Không Diệt Không Sinh Đừng Sợ Hãi (TB5)',
          score: '4.95',
          quantity: '1000+',
          price: '82.000',
          discount: '25',
          backAmount: '2',
          backAmountPrice: '408',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/f5/52/80/675e31a670afc560e7b0e46c0b65fb4f.png.webp',
          name: 'Apple iPhone 14 Pro Max',
          score: '4.95',
          quantity: '1000+',
          price: '27.450.000',
          discount: '19',
          backAmount: '686',
          backAmountPrice: '136k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/aa/24/e0/57914989351786ef9dfe027046ba4626.jpg.webp',
          name: 'Apple iPhone 11',
          score: '4.8',
          quantity: '1000+',
          price: '10.610.000',
          discount: '18',
          backAmount: '265',
          backAmountPrice: '53k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/0c/dd/e7/4be0add110579c0ce57e53fba16e656e.png.webp',
          name: 'Apple iPhone 14 Pro',
          score: '4.95',
          quantity: '881',
          price: '30.990.000',
          discount: '13',
          backAmount: '631',
          backAmountPrice: '126',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/a2/38/6c/ce008c63f4ac771550439da44f5f8ee8.png.webp',
          name: 'Apple iPhone 13',
          score: '4.95',
          quantity: '1000+',
          price: '16.990.000',
          discount: '32',
          backAmount: '425',
          backAmountPrice: '84k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/0c/28/ef/8c4a83ffeb29e5faa120a80ad05ba178.jpg.webp',
          name: 'Điện Thoại Xiaomi Redmi Note 12 4GB/128GB - Hàng Chính Hãng',
          score: '4.95',
          quantity: '8',
          price: '3.988.000',
          discount: '20',
          backAmount: '2100',
          backAmountPrice: '20k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/45/3b/fc/aa81d0a534b45706ae1eee1e344e80d9.jpg.webp',
          name: 'Nhà Giả Kim (Tái Bản 2020)',
          score: '4.95',
          quantity: '1000+',
          price: '51.350',
          discount: '35',
          backAmount: '1',
          backAmountPrice: '255',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/eb/76/de/a0e87ef33a285d22f4659374a1f1f177.jpg.webp',
          name: 'Clean Code – Mã Sạch Và Con Đường Trở Thành Lập Trình Viên Giỏi',
          score: '4.8',
          quantity: '631',
          price: '230.800',
          discount: '40',
          backAmount: '6',
          backAmountPrice: '1k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/29/43/11/71c0b521f23ae08bc4dc6ed24dbc98a7.jpg.webp',
          name: 'Quạt Hơi Nước Mini, Quạt Phun Sương Mini Tạo Ẩm Làm Mát Để Bàn',
          score: '4.5',
          quantity: '32',
          price: '284.050',
          discount: '5',
          backAmount: '56',
          backAmountPrice: '11k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/54/ff/25/bfdf0febe11a28eaa7cd3fa735a82c49.png.webp',
          name: 'Apple iPad 10.2-inch (9th Gen) Wi-Fi, 2021',
          score: '4.95',
          quantity: '32',
          price: '7.090.000',
          discount: '35',
          backAmount: '177',
          backAmountPrice: '35k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/94/df/44/1efb32bd47cbe070887e460a3ec8cb83.jpg.webp',
          name: 'Bột Cần Tây Sấy Lạnh Jan\'s mới 20 gói tiện dụng',
          score: '4.7',
          quantity: '1000+',
          price: '195.000',
          discount: '7',
          backAmount: '5',
          backAmountPrice: '969',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/c0/be/5a/67433e81553e46f4351ac451382c7ec0.png.webp',
          name: 'Giá Đỡ Máy Tính, Laptop, iPad, Macbook Hợp Kim Nhôm Cao Cấp. Hỗ Trợ Tản Nhiệt Chống Mỏi Cổ, Vai, Gáy. Hàng Chính Hãng Tamayoko',
          score: '4.95',
          quantity: '1000+',
          price: '459.000',
          discount: '6',
          backAmount: '11',
          backAmountPrice: '2k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/da/fe/dc/cb8682708ffee62939112775f1538fe5.jpg.webp',
          name: 'Xoài Sấy Dẻo Vinamit 250g',
          score: '5',
          quantity: '124',
          price: '120.000',
          discount: '10',
          backAmount: '3',
          backAmountPrice: '596',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/2d/59/84/1ec9c569287d0532dd40cecf4094071f.jpg.webp',
          name: 'Thẻ Nhớ microSD SanDisk Ultra 128GB UHS-I - 100MB/s (New 2020) - Hàng Nhập Khẩu',
          score: '4.8',
          quantity: '1000+',
          price: '219.000',
          discount: '7',
          backAmount: '5',
          backAmountPrice: '1k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/81/ee/a6/831809b5596fdce0ae16033df2522d30.jpg.webp',
          name: 'Trà Gạo Lứt Quê Việt - Giảm mỡ máu, giải độc gan, kiểm soát đường huyết, ngăn ngừa ung thư ( gạo lứt, đậu đen xanh lòng, đậu đỏ, kỷ tử, hoa nhài, cỏ ngọt)',
          score: '4.8',
          quantity: '1000+',
          price: '179.000',
          discount: '19',
          backAmount: '4',
          backAmountPrice: '890',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/98/07/0a/c1086b930db321b12e09588910fbead2.jpg.webp',
          name: 'Thức Ăn Hạt Cho Mèo Thái Lan Hello Cat Tuna 1.2Kg - Tặng Lon Pate Hello Cat 190G',
          score: '4.7',
          quantity: '629',
          price: '105.000',
          discount: '36',
          backAmount: '21',
          backAmountPrice: '4k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/5e/18/24/2a6154ba08df6ce6161c13f4303fa19e.jpg.webp',
          name: 'Cây Cam Ngọt Của Tôi',
          score: '4.95',
          quantity: '1000+',
          price: '70.200',
          discount: '35',
          backAmount: '2',
          backAmountPrice: '349',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/b3/d0/de/f9f879a32d4ba31bf5084b05e6fc7889.jpg.webp',
          name: 'Bộ Dao Kéo KNSCS-BCI Benchusch',
          score: '4.5',
          quantity: '76',
          price: '148.000',
          discount: '73',
          backAmount: '29',
          backAmountPrice: '6k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/49/75/99/2219ae33da6fb87ec3231dae0e752b3a.jpg.webp',
          name: 'Apple iPad mini (6th Gen) Wi-Fi, 2021',
          score: '4.95',
          quantity: '299',
          price: '12.490.000',
          discount: '17',
          backAmount: '312',
          backAmountPrice: '62k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/30/ee/5a/e2aed009bb558b5d2cfbbe157b428ba4.jpg.webp',
          name: 'Sách Muôn Kiếp Nhân Sinh (Bìa Mềm) - Nguyên Phong',
          score: '5',
          quantity: '16',
          price: '134.000',
          discount: '20',
          backAmount: '3',
          backAmountPrice: '666',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/64/1e/1a/60309a84a30a722425e56a3ad52eb9a0.png.webp',
          name: 'Máy lạnh Samsung Inverter 1.0HP AR09TYHQASINSV - Chỉ giao tại HCM',
          score: '4.7',
          quantity: '40',
          price: '5.478.000',
          discount: '9',
          backAmount: '695',
          backAmountPrice: '138k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/2c/3d/85/3fcc90a1300a79922ec58ef22afae47a.jpg.webp',
          name: 'Điện Thoại Nokia G11 4GB/64GB - Hàng Chính Hãng',
          score: '4.5',
          quantity: '43',
          price: '2.672.000',
          discount: '31',
          backAmount: '67',
          backAmountPrice: '13k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/43/dd/97/258137d331bf9359c814034a52388ff4.jpg.webp',
          name: 'Máy đọc sách All New Kindle Paperwhite 5 (11th Gen) - Hàng nhập khẩu',
          score: '4.95',
          quantity: '11',
          price: '2.800.000',
          discount: '5',
          backAmount: '70',
          backAmountPrice: '14k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/22/cb/a9/524a27dcd45e8a13ae6eecb3dfacba7c.jpg.webp',
          name: 'Rèn Luyện Tư Duy Phản Biện',
          score: '4.8',
          quantity: '1000+',
          price: '2.800.000',
          discount: '5',
          backAmount: '2',
          backAmountPrice: '328',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/22/cb/a9/524a27dcd45e8a13ae6eecb3dfacba7c.jpg.webp',
          name: 'Rèn Luyện Tư Duy Phản Biện',
          score: '4.8',
          quantity: '1000+',
          price: '66.000',
          discount: '33',
          backAmount: '2',
          backAmountPrice: '328',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/9c/1b/57/ffd2d24eefe918338dd64039fc9be957.jpg.webp',
          name: 'Rồi Hoa Sẽ Nở - 1',
          score: '3.6',
          quantity: '129',
          price: '90.000',
          discount: '15',
          backAmount: '2',
          backAmountPrice: '447',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/ec/45/40/d779c7b58bf0e74d45972e8a359e1d4e.png.webp',
          name: 'Apple iPhone 14',
          score: '4.95',
          quantity: '416',
          price: '19.250.000',
          discount: '23',
          backAmount: '481',
          backAmountPrice: '96k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/1a/1d/0a/f280cf83e7be6c502c54fe2f1b3a8b12.jpg.webp',
          name: 'Điện thoại Realme C55 (6GB/128GB) - Hàng chính hãng',
          score: '4.8',
          quantity: '23',
          price: '3.990.000',
          discount: '17',
          backAmount: '100',
          backAmountPrice: '20k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/42/0f/92/2f5a875401334239950b277660ccc79f.jpg.webp',
          name: 'Apple iPad Air (5th Gen) Wi-Fi, 2022',
          score: '4.95',
          quantity: '470',
          price: '14.190.000',
          discount: '25',
          backAmount: '350',
          backAmountPrice: '70k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/c0/f7/db/e98998e0d92de8981d1d8485ce96a3f8.jpg.webp',
          name: 'Máy lạnh Sharp Inverter 1 HP AH-X9XEW - Chỉ giao tại HCM',
          score: '4.6',
          quantity: '1000+',
          price: '6.370.000',
          discount: '20',
          backAmount: '159',
          backAmountPrice: '32k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/92/33/e2/5d9947f5ccb5481113c97aa6a5fab584.jpg.webp',
          name: 'Quạt Mini Đeo Cổ Không Cánh Tích Điện 5 Cấp Độ Màn Hình Đèn Led Quạt Điều Hòa Mini Thiết Kế Gọn Nhẹ Dung Lượng Pin Lớn Thích Hợp Khi Ra Ngoài Thể Dục Thể Thao',
          score: '4.7',
          quantity: '58',
          price: '249.000',
          discount: '50',
          backAmount: '6',
          backAmountPrice: '1k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/e0/c9/78/e028f9346e1922b0aadc750f272609c3.jpg.webp',
          name: 'Apple iPhone 12',
          score: '4.95',
          quantity: '1000+',
          price: '14.990.000',
          discount: '12',
          backAmount: '375',
          backAmountPrice: '75k',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/65/78/e7/2eacb9f887fc28779b15cf9ab6d0bf79.jpg.webp',
          name: 'Hành Tinh Của Một Kẻ Nghĩ Nhiều',
          score: '4.8',
          quantity: '1000+',
          price: '60.200',
          discount: '30',
          backAmount: '2',
          backAmountPrice: '299',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/7f/30/16/51d47c3c68c911d97350eb2374d6c408.jpg.webp',
          name: 'Đúng Việc (Tái Bản)',
          score: '4.95',
          quantity: '1000+',
          price: '58.000',
          discount: '39',
          backAmount: '1',
          backAmountPrice: '288',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/16/8f/ce/5131b0d2dab7e3a30e6fc3778852ce36.jpg.webp',
          name: 'Đúng Việc (Tái Bản)',
          score: '4.0',
          quantity: '2',
          price: '134.000',
          discount: '20',
          backAmount: '3',
          backAmountPrice: '666',
          productId: '1234'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/81/bc/7b/e816f29fc6e20711f8dc9da9bde3cfa0.jpg.webp',
          name: 'Định luật Murphy – Mọi bí mật tâm lý thao túng cuộc đời bạn',
          score: '4.7',
          quantity: '1000+',
          price: '88.000',
          discount: '26',
          backAmount: '2',
          backAmountPrice: '437',
          productId: '1234'
        }
      ]
    }
  },
  methods: {
    onClickProductDetail(productId) {
      this.$router.push(`/nha-sach-tiki/${productId}`);
    }
  }
}
</script>
<style lang="scss" scoped>
  .product-container {
    background: rgb(245, 245, 250);
    border-radius: 8px;
    margin-bottom: 32px;

    &__body {
      display: flex;
      flex-direction: column;
      -webkit-box-align: center;
      align-items: center;
      flex-shrink: 0;
      cursor: pointer;
      min-height: 78px;

      width: 1032px;

      .content {
        grid-template-columns: repeat(5, 1fr);
        display: grid;
        align-self: stretch;
        gap: 8px;
        background-color: rgb(245, 245, 250);
        border-top: 1px solid rgb(242, 242, 242);

        .product-item {
          text-decoration: none;
          display: flex;
          position: relative;
          cursor: pointer;
          width: 100%;
          height: 100%;
          border-radius: 4px;
          background: rgb(255, 255, 255);
          overflow: hidden;

          &:hover {
            box-shadow: rgba(0, 0, 0, 0.1) 0px 0px 20px;
            z-index: 1;
          }

          .styled-item {
            display: flex;
            color: rgb(36, 36, 36);
            text-decoration: none;
            flex-direction: column;
            -webkit-box-pack: justify;
            justify-content: space-between;
            -webkit-box-align: stretch;
            align-items: stretch;

            .thumbnail {
              flex-shrink: 0;
              width: 100%;
              height: auto;
              text-align: center;
              position: relative;

              .official-image {
                display: block;
                position: absolute;
                z-index: 2;

                top: 0px;
                left: 0px;
              }

              .thumbnail-wrapper {
                position: relative;
                width: 100%;
              }
            }

            .description-wrapper {
              padding: 0px 12px;

              .info {
                padding: 8px 0px;
                border-bottom: 1px solid rgb(235, 235, 240);
                width: 100%;

                .name {
                  display: -webkit-box;
                  -webkit-box-orient: vertical;
                  -webkit-line-clamp: 2;
                  overflow: hidden;
                  min-height: 36px;

                  font-weight: 400;
                  font-size: 12px;
                  line-height: 150%;
                  color: rgb(39, 39, 42);
                  margin: 0px;
                  word-break: break-word;
                }

                .rate-wrapper {
                  display: flex;
                  align-items: center;
                  min-height: 18px;

                  .full-rating {
                    display: flex;
                    align-items: center;
                    .score {
                      font-weight: 400;
                      font-size: 12px;
                      line-height: 150%;
                      color: rgb(128, 128, 137);
                    }
                  }

                  .sold-amount {
                    display: flex;
                    align-items: center;
                    color: rgb(128, 128, 137);
                    line-height: 150%;
                    font-size: 12px;
                    padding-left: 4px;

                    .divider {
                      width: 1px;
                      height: 9px;
                      background-color: rgb(199, 199, 199);
                    }

                    .quantity {
                      padding-left: 6px;
                    }
                  }
                }

                .price-discount {
                  text-align: left;
                  font-size: 16px;
                  line-height: 24px;
                  font-weight: 500;
                  margin-top: 6px;
                  color: rgb(56, 56, 61);
                  display: flex;
                  -webkit-box-align: center;
                  align-items: center;

                  &.has-discount {
                    color: rgb(255, 66, 78);
                  }

                  &__price {
                    text-align: left;
                    font-size: 16px;
                    line-height: 24px;
                    font-weight: 500;
                  }

                  &__discount {
                    padding: 0px 2px;
                    line-height: 16px;
                    font-size: 12px;
                    font-weight: 500;
                    margin-left: 4px;
                    margin-top: 3px;
                  }
                }

                .badge-under-price {
                  font-weight: 400;
                  font-size: 10px;
                  line-height: 150%;
                  min-height: 30px;

                  color: rgb(128, 128, 137);
                }

                .badge-under-rating {
                  display: flex;
                  gap: 4px;
                  flex-wrap: wrap;
                  margin-top: 6px;
                  min-height: 17px;
                }
              }
            }

            .badge-delivery {
              display: flex;
              padding: 8px 12px;
              gap: 4px;

              > span {
                display: -webkit-box;
                -webkit-box-orient: vertical;
                -webkit-line-clamp: 1;
                overflow: hidden;
                font-weight: 400;
                font-size: 12px;
                line-height: 16px;
                color: rgb(128, 128, 137);
              }
            }
          }
        }
      }

      .view-more-button {
        cursor: pointer;
        display: inline-block;
        width: 240px;
        margin-top: 12px;
        padding: 8px 12px;
        border-radius: 4px;
        border: 1px solid rgb(10, 104, 255);
        color: rgb(10, 104, 255);
        font-size: 16px;
        line-height: 150%;
        text-align: center;

        &:hover {
          background-color: rgba(0, 96, 255, 0.12) !important;
          opacity: 1 !important;
        }
      }
    }
  }
</style>
