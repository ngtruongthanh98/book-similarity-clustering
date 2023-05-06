<template>
  <div class="product-container">
    <div class="product-container__body">
      <div class="content">

        <div v-for="(ele, index) in productList" :key="index" class="product-item" @click="onClickProductDetail(ele.isbn)">
          <div v-if="!isLoading" class="styled-item">
            <div class="thumbnail">
              <!-- <img class="official-image" src="https://salt.tikicdn.com/ts/upload/5d/4c/f7/0261315e75127c2ff73efd7a1f1ffdf2.png" alt="Official" width="68" height="14"> -->

              <div class="thumbnail-wrapper">
                <img :src="ele.imageURLL" alt="Product image" width="183" height="183">
              </div>

            </div>

            <div class="description-wrapper">
              <div class="info">
                <div class="name">{{ ele.bookTitle }}</div>

                <div class="rate-wrapper">
                  <div class="full-rating">
                    <span class="score">{{ ele.score || 4 }}</span>

                    <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" size="14" color="#fdd836" height="14" width="14" xmlns="http://www.w3.org/2000/svg" style="color: rgb(253, 216, 54);"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"></path></svg>
                  </div>

                  <div class="sold-amount">
                    <div class="divider"></div>
                    <div class="quantity">Đã bán {{ ele.quantity || '1000+' }}</div>
                  </div>
                </div>

                <div class="price-discount has-discount">
                  <div class="price-discount__price">{{ ele.price || '150.000' }} ₫</div>
                  <div class="price-discount__discount">-{{ele.discount || 25}}%</div>
                </div>

                <div class="badge-under-price">
                  Tặng tới {{ ele.backAmount || 4 }} ASA ({{ ele.backAmountPrice || 345 }} ₫)
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
          <VaSkeleton v-else />
        </div>
      </div>

      <!-- <div class="view-more-button">
        Xem Thêm
      </div> -->

      <div class="pagination-container">
        <va-pagination
          v-model="currentPage"
          :pages="5428"
          :visible-pages="4"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { getBookByPage } from '../../../services/books'

export default {
  data() {
    return {
      currentPage: 1,
      productList: [],
      isLoading: false
    }
  },
  watch: {
    async currentPage(newValue) {
      try {
        this.isLoading = true

        const res = await this.getBookByPage(newValue)
        this.productList = res.data

        this.isLoading = false
      } catch (error) {
        console.log(error);
      }
    }
  },
  async mounted() {
    try {
      this.isLoading = true

      const res = await this.getBookByPage(this.currentPage)
      this.productList = res.data

      this.isLoading = false
    } catch (error) {
      console.log(error);
    }
  },
  methods: {
    getBookByPage,
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
    margin-left: 8px;

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
        margin-bottom: 16px;

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

      .pagination-container {
        width: 100%;
        margin-top: 16px;

        display: flex;
        justify-content: center;
      }
    }
  }
</style>
