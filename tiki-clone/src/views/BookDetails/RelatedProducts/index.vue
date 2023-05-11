<template>
  <div class="related-products">
    <div class="title">Sản Phẩm Tương Tự ({{ fullAlgorithmName }})</div>

    <div class="image-container">
      <div class="related-book" v-for="(ele, index) in firstSixItems" :key="index" @click="onClickProductDetail(ele.isbn)">
        <div class="image-item" style="width: 100%; height: 100%;">
          <div class="item__wrapper" style="padding: 12px;">
              <div style="width: 100%; height: 100%;">
                <div class="product-image__wrapper">
                    <div class="thumbnail-wrapper">
                      <img :alt="ele.bookTitle" :src="ele.imageURLL">
                    </div>
                </div>
                <div class="info">
                    <p class="price"><span>{{ ele.price || 150.000 }} <sup> ₫</sup></span></p>
                    <div class="book-title" style="max-height: 40px; height: auto;">
                      {{ ele.bookTitle }}
                    </div>
                    <div class="bottom" style="flex: unset;">
                      <div class="item-review">
                          <div style="display: flex;">
                            <div class="full-rating">
                                <div class="total" style="display: flex; align-items: center;">
                                  <span style="font-weight: 400; font-size: 12px; line-height: 16px; color: rgb(128, 128, 137);">{{ ele.rating || '3' }}</span>
                                  <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" size="14" color="#fdd836" height="14" width="14" xmlns="http://www.w3.org/2000/svg" style="color: rgb(253, 216, 54);">
                                      <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"></path>
                                  </svg>
                                </div>
                            </div>
                          </div>
                          <div style="display: flex; align-items: center; color: rgb(128, 128, 137); line-height: normal; font-size: 12px; padding-left: 4px;">
                            <div style="width: 1px; height: 9px; background-color: rgb(199, 199, 199);"></div>
                            <div data-view-id="pdp_quantity_sold" style="padding-left: 6px;">Đã bán {{ ele.sold || '1000+' }}</div>
                          </div>
                      </div>
                    </div>
                </div>
              </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { ALGORITHM_NAME } from '../../../constants'
import { getSimilarBooks, getBookDetails } from "../../../services/books"
// import store from '../../../store'

export default {
  props: {
    algoName: {
      type: String,
      default: ''
    },
    isbn: {
        type: String,
        default: '0195153448'
    },
  },
  data() {
    return {
      fullAlgorithmName: '',
      similarBooksList: [],
      firstSixItems: [],
      RELATED_PRODUCTS_LIST: [
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/24/bb/95/4d5ac1d595f8b1a73f3e7122f388d271.jpg.webp',
          name: 'Bộ 4 tác phẩm Mario Puzo - Những chuyện ly kỳ bên ngoài thế giới ngầm (Cuốn Lẻ và Combo)',
          rating: '3',
          sold: '5',
          price: '200.000',
          productId: 'agha'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/24/bb/95/4d5ac1d595f8b1a73f3e7122f388d271.jpg.webp',
          name: 'Bộ 4 tác phẩm Mario Puzo - Những chuyện ly kỳ bên ngoài thế giới ngầm (Cuốn Lẻ và Combo)',
          rating: '3',
          sold: '5',
          price: '200.000',
          productId: 'wwhjq'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/24/bb/95/4d5ac1d595f8b1a73f3e7122f388d271.jpg.webp',
          name: 'Bộ 4 tác phẩm Mario Puzo - Những chuyện ly kỳ bên ngoài thế giới ngầm (Cuốn Lẻ và Combo)',
          rating: '3',
          sold: '5',
          price: '200.000',
          productId: 'wgjrwq'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/24/bb/95/4d5ac1d595f8b1a73f3e7122f388d271.jpg.webp',
          name: 'Bộ 4 tác phẩm Mario Puzo - Những chuyện ly kỳ bên ngoài thế giới ngầm (Cuốn Lẻ và Combo)',
          rating: '3',
          sold: '5',
          price: '200.000',
          productId: 'sgjrwq'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/24/bb/95/4d5ac1d595f8b1a73f3e7122f388d271.jpg.webp',
          name: 'Bộ 4 tác phẩm Mario Puzo - Những chuyện ly kỳ bên ngoài thế giới ngầm (Cuốn Lẻ và Combo)',
          rating: '3',
          sold: '5',
          price: '200.000',
          productId: 'gwwjr'
        },
        {
          imageUrl: 'https://salt.tikicdn.com/cache/280x280/ts/product/24/bb/95/4d5ac1d595f8b1a73f3e7122f388d271.jpg.webp',
          name: 'Bộ 4 tác phẩm Mario Puzo - Những chuyện ly kỳ bên ngoài thế giới ngầm (Cuốn Lẻ và Combo)',
          rating: '3',
          sold: '5',
          price: '200.000',
          productId: 'sfsf'
        }
      ]
    }
  },
  async mounted() {
    if (this.algoName === 'leiden') {
      this.fullAlgorithmName = ALGORITHM_NAME.leiden
    }

    if (this.algoName === 'louvain') {
      this.fullAlgorithmName = ALGORITHM_NAME.louvain
    }

    if (this.algoName === 'girvan_newman') {
      this.fullAlgorithmName = ALGORITHM_NAME.girvan_newman
    }

    console.log('this.isbn: ', this.isbn);


    const res = await this.getSimilarBooks(this.isbn, this.algoName)
    console.log('res: ', res);
    this.similarBooksList = res.data

    this.firstSixItems = this.similarBooksList.slice(0, 6);

  },
  methods: {
    getSimilarBooks,
    getBookDetails,
    async onClickProductDetail(productId) {
      console.log('productId: ', productId);

      this.$router.push(`/nha-sach-tiki/${productId}`);
    }
  }
}
</script>
<style lang="scss" scoped>
  .related-products {
    margin-top: 16px;
    // padding: 12px 16px;
    background: #ffffff;
    border-radius: 8px;
    min-height: 278px;
    width: 1240px;

    .title {
      color: rgb(51, 51, 51);
      font-size: 20px;
      font-weight: 400;
      line-height: 32px;
      padding: 8px 16px;
      text-transform: capitalize;
      display: flex;
      -webkit-box-pack: justify;
      justify-content: space-between;
      -webkit-box-align: center;
      align-items: center;
      margin: 0px;
    }

    .image-container {
      background-color: rgb(255, 255, 255);
      border-radius: 4px;
      min-height: 293px;


      display: grid;
      overflow: auto;
      position: relative;
      grid-template-columns: repeat(6, 1fr);
      column-gap: 0px;

      .related-book {
        width: 176px;
        cursor: pointer;
      }

      .image-item {
        .item__wrapper {
          position: relative;
          display: flex;
          flex-direction: column;
          -webkit-box-align: center;
          align-items: center;
          width: 100%;
          height: 100%;
          padding: 12px;
          background-color: rgb(255, 255, 255);

          &:hover {
            box-shadow: rgba(0, 0, 0, 0.1) 0px 0px 20px;
            z-index: 1;
          }

          .product-image__wrapper {
            position: relative;
            width: 100%;

            .thumbnail-wrapper {
              position: relative;
              width: 100%;
              // padding-bottom: 100%;

              img {
                position: relative;
                width: 176px;
                height: 176px;
                // padding-bottom: 100%;
              }
            }
          }

          .info {
            padding: 8px 0px;
            margin: 0px 12px;
            min-height: 94px;

            .price {
              text-align: left;
              font-size: 16px;
              line-height: 24px;
              font-weight: 500;
              color: rgb(56, 56, 61);
              margin: 2px 0px 0px;
              display: flex;
              -webkit-box-align: center;
              align-items: center;

              sup {
                top: -0.5em;
              }
            }

            .book-title {
              position: relative;
              display: -webkit-box;
              -webkit-box-orient: vertical;
              -webkit-line-clamp: 2;
              max-height: 40px;
              min-height: 32px;
              margin: 0px;
              width: 100%;
              color: rgb(36, 36, 36);
              font-size: 12px;
              font-weight: 400;
              font-style: normal;
              font-stretch: normal;
              line-height: 16px;
              letter-spacing: 0.1px;
              text-align: left;
              text-overflow: ellipsis;
              overflow: hidden;
              word-break: break-word;


              margin: 0px;
              font-weight: 400;
              font-size: 12px;
            }

            .bottom {
              margin: 0px;
              font-weight: 400;
              font-size: 12px;

              .item-review {
                display: flex;
                -webkit-box-align: center;
                align-items: center;
                align-self: stretch;
                margin-top: 3px;
              }
            }
          }
        }
      }
    }


  }
</style>
