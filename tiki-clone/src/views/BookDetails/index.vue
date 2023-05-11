<template>
  <div class="book-details-page">
    <div class="breadcrumb-wrapper">
        <div class="breadcrumb-container">
          <va-breadcrumbs
              separator=">"
              class="custom-breadcrumb"
              >
              <va-breadcrumbs-item label="Trang chủ" class="homepage-breadcrumb" @click="onClickGotoHome"/>
              <va-breadcrumbs-item label="Nhà sách Tiki" class="bookstore-breadcrumb" @click="onClickGotoBookstore" />
              <va-breadcrumbs-item :label="bookData.bookTitle" class="book-breadcrumb" />
          </va-breadcrumbs>
        </div>
    </div>
    <div class="book-details-page__body">
        <div class="book-main">
          <div class="product-image-styles">
            <div class="inner-wrapper">
              <div class="group-images">
                <div class="thumbnail" data-view-id="pdp_main_view_gallery">
                    <div class="imagelens__wrapper">
                      <div class="container">
                        <img :src="bookData.imageURLL" :alt="bookData.bookTitle" class="WebpImg__StyledImg-sc-h3ozu8-0 fWjUGo" style="width: 444px; height: 444px; z-index: 0;">
                      </div>
                    </div>
                </div>
                <div class="image-badges" style="position: initial;"></div>
              </div>
              <div class="product-actions">
                <div class="product-share">Chia sẻ:</div>
                <img src="https://frontend.tikicdn.com/_desktop-next/static/img/pdp_revamp_v2/social-facebook.svg" alt="social-facebook" class="icon left">
                <img src="https://frontend.tikicdn.com/_desktop-next/static/img/pdp_revamp_v2/social-messenger.svg" alt="social-messenger" class="icon">
                <img src="https://frontend.tikicdn.com/_desktop-next/static/img/pdp_revamp_v2/social-pinterest.svg" alt="social-pinterest" class="icon">
                <img src="https://frontend.tikicdn.com/_desktop-next/static/img/pdp_revamp_v2/social-twitter.svg" alt="social-twitter" class="icon">
                <img src="https://frontend.tikicdn.com/_desktop-next/static/img/pdp_revamp_v2/social-copy.svg" alt="social-copy" class="icon last">
              </div>
            </div>

            <div class="product-image-styles__separator"></div>

            <div class="product-content">
              <div class="header">
                <div class="brand">
                    <span class="brand-and-author no-after">
                      <h6>Tác giả:&nbsp;<a data-view-id="pdp_details_view_author" data-view-index="0" href="/author/jose-mauro-de-vasconcelos.html">{{ bookData.bookAuthor }}</a></h6>
                    </span>
                </div>
                <h1 class="title">{{ bookData.bookTitle }}</h1>
                <div class="below-title">
                    <div style="display: flex;">
                      <div class="review-box">
                          <div style="display: flex;">
                            <div style="position: relative;">
                                <div style="display: flex; align-items: center;">
                                  <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" size="16" color="#c7c7c7" height="16" width="16" xmlns="http://www.w3.org/2000/svg" style="color: rgb(199, 199, 199);">
                                      <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"></path>
                                  </svg>
                                  <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" size="16" color="#c7c7c7" height="16" width="16" xmlns="http://www.w3.org/2000/svg" style="color: rgb(199, 199, 199);">
                                      <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"></path>
                                  </svg>
                                  <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" size="16" color="#c7c7c7" height="16" width="16" xmlns="http://www.w3.org/2000/svg" style="color: rgb(199, 199, 199);">
                                      <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"></path>
                                  </svg>
                                  <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" size="16" color="#c7c7c7" height="16" width="16" xmlns="http://www.w3.org/2000/svg" style="color: rgb(199, 199, 199);">
                                      <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"></path>
                                  </svg>
                                  <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" size="16" color="#c7c7c7" height="16" width="16" xmlns="http://www.w3.org/2000/svg" style="color: rgb(199, 199, 199);">
                                      <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"></path>
                                  </svg>
                                </div>
                                <div style="width: 100%; white-space: nowrap; position: absolute; left: 0px; top: 0px; overflow: hidden;">
                                  <div v-html="starNumber"></div>
                                </div>
                            </div>
                          </div>
                          <a class="number" data-view-id="pdp_main_view_review">(Xem 12546 đánh giá)</a>
                          <div class="divider"></div>
                      </div>
                      <div data-view-id="pdp_quantity_sold" class="quantity-sold">Đã bán 5000+</div>
                    </div>
                </div>
              </div>

              <div class="body">
                <div class="price-and-icon">
                  <div class="new-price-container">
                      <div class="product-price has-discount">
                        <div class="product-price__current-price">72.000 ₫</div>
                        <div class="product-price__list-price">108.000 ₫</div>
                        <div class="product-price__discount-rate">-33%</div>
                      </div>
                  </div>
                  <div class="widget-wrapper">
                      <div id="thuong-asa" class="astra-box"><img height="16" width="13" src="https://salt.tikicdn.com/ts/upload/df/e2/b4/063c4d55ca380f818547f00f5175d39f.png" alt="asa" class="astra-icon"><span class="astra-text">Thưởng 0,36 ASA (≈ 72đ)</span><span class="astra-tooltip"></span></div>
                      <img src="https://salt.tikicdn.com/ts/upload/43/01/71/d74d0e9e37a9bb14f35dcc0c816d2038.gif" class="image-new">
                  </div>
                </div>

                <div class="delivery-zone">
                  <div data-view-id="pdp_main_change_address" class="delivery-zone__heading">
                      <div><span>Giao đến </span><span class="address">Q. 1, P. Bến Nghé, Hồ Chí Minh</span> - <span class="address-change">Đổi địa chỉ</span></div>
                  </div>
                  <div class="delivery-zone__inner">
                      <div class="shipping-info">
                        <div class="shipping-info__inner">
                            <div class="shipping-info__item ">
                              <div class="shipping-info__item__header">
                                  <div class="shipping-info__item__header__logo" style="width: 32px;"><img src="https://salt.tikicdn.com/ts/upload/85/45/34/2fc25c6a660d84a41a6bf9276ce160ba.png" alt="" height="14" width="32"></div>
                                  <div class="divider"></div>
                                  <div class="shipping-info__item__header__highlight">Trước 16:00 hôm nay</div>
                              </div>
                              <div class="shipping-info__item__fee">
                                  <div class="shipping-info__item__fee_name">Vận chuyển: 25.000đ</div>
                              </div>
                            </div>
                            <div class="shipping-info__item ">
                              <div class="shipping-info__item__header">
                                  <div class="shipping-info__item__header__logo" style="width: 32px;"><img src="https://salt.tikicdn.com/ts/upload/67/e4/c2/02b5400b39bb3371e06d33c1e9f4d854.png" alt="" height="14" width="32"></div>
                                  <div class="divider"></div>
                                  <div class="shipping-info__item__header__highlight">Ngày mai, trước 23:00</div>
                              </div>
                              <div class="shipping-info__item__fee">
                                  <div class="shipping-info__item__fee_name">Vận chuyển: 14.000đ</div>
                              </div>
                            </div>
                        </div>
                      </div>
                  </div>
                </div>

                <va-counter
                  v-model="counterValue"
                  :min="0"
                  :max="100"
                  :step="1"
                  margins="0"
                  color="#262824"
                />

                <div class="add-to-cart">
                  <div class="group-button"><button type="button" class="btn btn-add-to-cart" data-view-id="pdp_add_to_cart_button">Chọn mua</button></div>
                </div>
              </div>
            </div>
          </div>
        </div>


        <RelatedProducts algoName="louvain" :isbn="bookData.isbn"/>

        <RelatedProducts algoName="leiden" :isbn="bookData.isbn"/>

        <RelatedProducts algoName="girvan_newman" :isbn="bookData.isbn"/>

        <DetailInfo :publisher="bookData.publisher" :bookAuthor="bookData.bookAuthor" />
    </div>
  </div>
</template>

<script>
import RelatedProducts from "./RelatedProducts/index.vue"
import DetailInfo from "./DetailInfo/index.vue"

import { getBookDetails } from "../../services/books"

export default {
  components: {
    RelatedProducts,
    DetailInfo
  },
  data() {
    return {
      productName: 'Cây Cam Ngọt Của Tôi',
      bookData: {},
      starNumber: '',
      bookId: '',
      counterValue: 0
    }
  },
  watch: {
    async '$route.params.productId'(newProductId) {
      try {
        const res = await this.getBookDetails(newProductId);
        this.bookId = res.data.isbn
        this.bookData = res.data;

        const rating = parseFloat(this.bookData.avg_rating);
        const numStars = Math.round(rating);
        const stars = [];

        for (let i = 0; i < numStars; i++) {
          stars.push(
            '<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" size="16" color="#fdd836" height="16" width="16" xmlns="http://www.w3.org/2000/svg" style="color: rgb(253, 216, 54);">' +
            '<path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"></path>' +
            '</svg>'
          );
        }

        this.starNumber = stars.join('');
      } catch (err) {
        console.error(err);
      }
    }
  },
  async mounted() {
    const bookId = this.$route.params.productId;
    this.bookId = this.$route.params.productId;


    try {
      const res = await this.getBookDetails(bookId);
      this.bookId = res.data.isbn
      this.bookData = res.data;

      const rating = parseFloat(this.bookData.avg_rating);
      const numStars = Math.round(rating);
      const stars = [];

      for (let i = 0; i < numStars; i++) {
        stars.push(
          '<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" size="16" color="#fdd836" height="16" width="16" xmlns="http://www.w3.org/2000/svg" style="color: rgb(253, 216, 54);">' +
          '<path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"></path>' +
          '</svg>'
        );
      }

      this.starNumber = stars.join('');
    } catch (err) {
      console.error(err);
    }
  },
  methods: {
    getBookDetails,
    onClickGotoHome() {
      this.$router.push({ name: 'home' });
    },
    onClickGotoBookstore() {
      this.$router.push({ name: 'tiki-bookstore' });
    }
  }
}
</script>
<style lang="scss">
  .book-details-page {
    .breadcrumb-wrapper {
      background-color: rgb(245, 245, 250);

      .breadcrumb-container {
        width: 1270px;
        height: 40px;
        padding-left: 15px;
        padding-right: 15px;
        margin-right: auto;
        margin-left: auto;

        .custom-breadcrumb {
          height: 100%;

          color: rgb(128, 128, 137);
          font-size: 14px;
          line-height: 20px;
          font-weight: 300;
          white-space: nowrap;

          .homepage-breadcrumb, .bookstore-breadcrumb {
            margin-right: 5.5px;

            &:hover {
              text-decoration: underline;
              cursor: pointer;
            }
          }

          .bookstore-breadcrumb {
            margin-left: 8.5px;
          }

          .book-breadcrumb {
            margin-left: 8.5px;
            color: rgb(56, 56, 61);
          }
        }
      }
    }

    &__body {
      width: 1270px;
      padding-left: 15px;
      padding-right: 15px;
      margin-right: auto;
      margin-left: auto;

      .book-main {
        .product-image-styles {
          display: flex;
          margin-bottom: 16px;
          background-color: rgb(255, 255, 255);
          border-radius: 4px;

          .inner-wrapper {
            padding: 16px 0px 16px 16px;
            position: relative;

            .group-images {
              display: flex;
              flex-direction: column;
              position: relative;

              .thumbnail {
                text-align: center;
                position: relative;

                .imagelens__wrapper {
                  position: relative;
                  display: flex;
                  -webkit-box-pack: center;
                  justify-content: center;
                  -webkit-box-align: center;
                  align-items: center;
                  width: 444px;
                  height: 444px;
                  cursor: pointer;

                  .container {
                    position: relative;
                    display: flex;
                    width: 444px;
                    height: 444px;
                  }
                }
              }
            }

            .image-badges {

            }

            .product-actions {
              display: flex;
              margin-top: 24px;
              -webkit-box-align: center;
              align-items: center;

              .product-share {
                font-size: 15px;
                line-height: 24px;
                color: rgb(36, 36, 36);
              }

              .icon {
                width: 28px;
                height: 28px;
                margin-right: 8px;
                cursor: pointer;
              }

              .left {
                margin-left: 8px;
              }

              .last {
                margin-right: 0px;
              }
            }
          }

          &__separator {
            margin: 0px 12px;
            width: 1px;
            background: rgb(242, 242, 242);
            flex-shrink: 0;
          }
        }

        .product-content {
          flex: 1 1 0%;

          .header {
            padding: 16px 28px 16px 0px;
            position: relative;

            .brand {
              display: flex;
              margin-top: 8px;

              > span {
                display: flex;
                -webkit-box-align: baseline;
                align-items: baseline;

                > h6 {
                  margin: 0px;
                  color: rgb(36, 36, 36);
                  font-size: 13px;
                  font-weight: 400;
                  line-height: 20px;
                }
              }

              a {
                text-decoration: none;
                background-color: transparent;
              }

            }

            .title {
              margin: 0px 0px 4px;
              color: rgb(36, 36, 36);
              font-size: 24px;
              font-weight: 300;
              line-height: 32px;
              word-break: break-word;
            }

            .below-title {
              display: flex;
              -webkit-box-align: center;
              align-items: center;
              margin-top: 4px;
              -webkit-box-pack: justify;
              justify-content: space-between;

              .review-box {
                display: flex;
                -webkit-box-align: center;
                align-items: center;

                .number {
                  display: block;
                  cursor: pointer;
                  margin-left: 8px;
                  color: rgb(120, 120, 120);
                  font-size: 15px;
                  line-height: 24px;
                }

                .divider {
                  width: 1px;
                  height: 12px;
                  background-color: rgb(199, 199, 199);
                  margin-left: 8px;
                  margin-right: 8px;
                }
              }

              .quantity-sold {
                font-size: 15px;
                line-height: 24px;
                color: rgb(120, 120, 120);
              }
            }
          }

          .body {
            .price-and-icon {
              .new-price-container {

                .product-price {
                  padding-top: 12px;
                  display: flex;
                  align-items: flex-end;
                  color: rgb(56, 56, 61);

                  &.has-discount {
                    color: rgb(255, 66, 78);
                  }

                  &__current-price {
                    font-size: 32px;
                    line-height: 40px;
                    margin-right: 8px;
                    font-weight: 500;
                  }

                  &__list-price {
                    color: rgb(128, 128, 137);
                    text-decoration: line-through;
                    font-size: 14px;
                    line-height: 20px;
                  }

                  &__discount-rate {
                    font-weight: 500;
                    margin-left: 4px;
                    color: rgb(255, 66, 78);
                    margin-top: 3px;
                    line-height: 18px;
                    font-size: 14px;
                    padding: 0px 4px;
                  }
                }


              }

              .widget-wrapper {
                display: flex;
                -webkit-box-align: center;
                align-items: center;
                margin-top: 10px;
                width: fit-content;

                .astra-box {
                  border-radius: 4px;
                  background-color: rgb(242, 240, 254);
                  display: flex;
                  width: fit-content;
                  -webkit-box-align: center;
                  align-items: center;
                  padding: 4px 8px;
                  border: 0.5px solid rgb(198, 188, 248);
                  margin: 0px;
                  cursor: pointer;

                  .astra-icon {
                    margin-right: 7px;
                  }

                  .astra-text {
                    font-size: 14px;
                    line-height: 20px;
                    color: rgb(64, 45, 161);
                    font-weight: 400;
                  }

                  .astra-tooltip {
                    background-image: url(https://frontend.tikicdn.com/_desktop-next/static/img/icons/question-blue.svg);
                    width: 10px;
                    height: 10px;
                    background-size: 10px 10px;
                    margin-left: 4px;
                  }
                }

                .image-new {
                  max-width: 42px;
                  margin-left: 8px;
                  cursor: pointer;
                }

              }
            }

            .delivery-zone {
              background-color: rgb(255, 255, 255);
              margin: 16px 0px 0px;
              border-top: 1px solid rgb(242, 242, 242);

              &__heading {
                display: flex;
                padding: 12px 0px;
                -webkit-box-pack: justify;
                justify-content: space-between;
                cursor: pointer;

                > div > .address {
                  text-decoration: underline;
                  font-size: 15px;
                  line-height: 24px;
                  font-weight: 500;
                  white-space: nowrap;
                  overflow: hidden;
                  text-overflow: ellipsis;
                }

                > div > .address-change {
                  color: rgb(11, 116, 229);
                  font-size: 16px;
                  line-height: 24px;
                  font-weight: 500;
                  flex-shrink: 0;
                }
              }

              &__inner {
                .shipping-info {
                  margin-bottom: 12px;

                  &__inner {
                    display: flex;
                    width: 491px;
                  }

                  &__item {
                    border: 1px solid rgb(238, 238, 238);
                    border-radius: 12px;
                    padding: 8px;
                    position: relative;
                    margin-right: 12px;
                    z-index: 1;
                    font-size: 13px;
                    line-height: 20px;
                    color: rgb(120, 120, 120);
                    flex: 1 1 0%;

                    &__header {
                      display: flex;
                      -webkit-box-align: center;
                      align-items: center;
                      height: 20px;
                      font-size: 14px;

                      &__logo {
                        width: 32px;
                      }

                      .divider {
                        content: " ";
                        width: 1px;
                        height: 8px;
                        margin: 0px 4px;
                        background-color: rgb(235, 235, 240);
                      }

                      &__highlight {
                        color: rgb(0, 171, 86);
                        font-weight: 500;
                      }
                    }

                    &__fee {
                      display: flex;
                      margin-bottom: 2px;

                      &__name {
                        font-weight: 400;
                        font-size: 14px;
                        line-height: 20px;
                        color: rgb(56, 56, 61);
                      }
                    }
                  }
                }
              }
            }

            .add-to-cart {
              display: flex;
              flex-direction: column;
              margin: 16px 0px 0px;
              padding: 16px 0px;
              border-top: 1px solid rgb(242, 242, 242);

              .qty-and-message {
                display: flex;
                align-items: flex-end;

                .quantity-input-wrapper {
                  > p {
                    font-size: 15px;
                    line-height: 1.6;
                    margin: 0px 0px 10px;
                  }

                  .group-input {
                    display: flex;
                    -webkit-box-align: center;
                    align-items: center;
                    margin-top: 8px;
                  }
                }
              }

              .group-button {
                margin-top: 16px;
                flex: 1 1 0%;
                display: flex;

                .btn {
                  cursor: pointer;
                  display: flex;
                  -webkit-box-align: center;
                  align-items: center;
                  -webkit-box-pack: center;
                  justify-content: center;
                  min-width: 190px;
                  width: 100%;
                  max-width: 300px;
                  height: 48px;
                  font-size: 15px;
                  line-height: 24px;
                  font-weight: 500;
                  text-transform: capitalize;
                  border: none;
                  border-radius: 4px;
                  outline: none;

                  &:hover {
                    opacity: 0.8;
                  }
                }

                .btn-add-to-cart {
                  color: rgb(255, 255, 255);
                  background-color: rgb(255, 57, 69);
                }

              }
            }
          }
        }
      }
    }
  }
</style>
