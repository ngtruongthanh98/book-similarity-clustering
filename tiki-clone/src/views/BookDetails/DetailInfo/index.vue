<template>
<div class="detail-info">
   <div class="left">
      <div class="group">
         <h2 class="blockTitle__wrapper">Thông tin chi tiết</h2>
         <div class="content has-table">
            <table>
               <tbody>
                  <tr>
                     <td class="custom-item">Công ty phát hành</td>
                     <td class="item-content">Amazon</td>
                  </tr>
                  <tr>
                     <td class="custom-item">Kích thước</td>
                     <td class="item-content">14 x 20.5 cm</td>
                  </tr>
                  <tr>
                     <td class="custom-item">Dịch Giả / Tác giả</td>
                     <td class="item-content">{{ bookAuthor }}</td>
                  </tr>
                  <tr>
                     <td class="custom-item">Loại bìa</td>
                     <td class="item-content">Bìa mềm</td>
                  </tr>
                  <tr>
                     <td class="custom-item">Số trang</td>
                     <td class="item-content">244</td>
                  </tr>
                  <tr>
                     <td class="custom-item">Nhà xuất bản</td>
                     <td class="item-content">{{ publisher }}</td>
                  </tr>
               </tbody>
            </table>
         </div>
      </div>
      <div class="group">
         <h2 class="blockTitle__wrapper">Mô Tả Sản Phẩm</h2>
         <div class="content">
            <div class="toggleContent__wrapper">
               <div class="toggleContent__view" style="overflow: hidden; height: 480px;">
                  <p>“Vị chua chát của cái nghèo hòa trộn với vị ngọt ngào khi khám phá ra những điều khiến cuộc đời này đáng số một tác phẩm kinh điển của Brazil.”</p>
                  <p>- Booklist</p>
                  <p>“Một cách nhìn cuộc sống gần như hoàn chỉnh từ con mắt trẻ thơ… có sức mạnh sưởi ấm và làm tan nát cõi lòng, dù người đọc ở lứa tuổi nào.”</p>
                  <p>- The National</p>
                  <p>Hãy làm quen với Zezé, cậu bé tinh nghịch siêu hạng đồng thời cũng đáng yêu bậc nhất, với ước mơ lớn lên trở thành nhà thơ cổ thắt nơ bướm. Chẳng phải ai cũng công nhận khoản “đáng yêu” kia đâu nhé. Bởi vì, ở cái xóm ngoại ô nghèo ấy, nỗi khắc khổ bủa vây đã che mờ mắt người ta trước trái tim thiện lương cùng trí tưởng tượng tuyệt vời của cậu bé con năm tuổi.</p>
                  <p>Có hề gì đâu bao nhiêu là hắt hủi, đánh mắng, vì Zezé đã có một người bạn đặc biệt để trút nỗi lòng: cây cam ngọt nơi vườn sau. Và cả một người bạn nữa, bằng xương bằng thịt, một ngày kia xuất hiện, cho cậu bé nhạy cảm khôn sớm biết thế nào là trìu mến, thế nào là nỗi đau, và mãi mãi thay đổi cuộc đời cậu.<br>Mở đầu bằng những thanh âm trong sáng và kết thúc lắng lại trong những nốt trầm hoài niệm, Cây cam ngọt của tôi khiến ta nhận ra vẻ đẹp thực sự của cuộc sống đến từ những điều giản dị như bông hoa trắng của cái cây sau nhà, và rằng cuộc đời thật khốn khổ nếu thiếu đi lòng yêu thương và niềm trắc ẩn. Cuốn sách kinh điển này bởi thế không ngừng khiến trái tim người đọc khắp thế giới thổn thức, kể từ khi ra mắt lần đầu năm 1968 tại Brazil.</p>
                  <!-- <p><strong>Tác giả: </strong></p>
                  <p>JOSÉ MAURO DE VASCONCELOS (1920-1984) là nhà văn người Brazil. Sinh ra trong một gia đình nghèo ở ngoại ô Rio de Janeiro, lớn lên ông phải làm đủ nghề để kiếm sống. Nhưng với tài kể chuyện thiên bẩm, trí nhớ phi thường, trí tưởng tượng tuyệt vời cùng vốn sống phong phú, José cảm thấy trong mình thôi thúc phải trở thành nhà văn nên đã bắt đầu sáng tác năm 22 tuổi. Tác phẩm nổi tiếng nhất của ông là tiểu thuyết mang màu sắc tự truyện Cây cam ngọt của tôi. Cuốn sách được đưa vào chương trình tiểu học của Brazil, được bán bản quyền cho hai mươi quốc gia và chuyển thể thành phim điện ảnh. Ngoài ra, José còn rất thành công trong vai trò diễn viên điện ảnh và biên kịch.</p>
                  <p>Giá sản phẩm trên Tiki đã bao gồm thuế theo luật hiện hành. Bên cạnh đó, tuỳ vào loại sản phẩm, hình thức và địa chỉ giao hàng mà có thể phát sinh thêm chi phí khác như phí vận chuyển, phụ phí hàng cồng kềnh, thuế nhập khẩu (đối với đơn hàng giao từ nước ngoài có giá trị trên 1 triệu đồng).....</p> -->
                  <div class="gradient"></div>
               </div>
               <!-- <a class="btn-more" data-view-id="pdp_view_description_button">Xem Thêm Nội Dung</a> -->
            </div>
         </div>
      </div>
   </div>
   <div class="right">
      <div class="style__TrackingBrandAdWrapper-sc-1pkpslo-0 iKfXDw">
         <a href="//tka.tiki.vn/pixel/pixel?data=JMCfjc88FFkrXW1MY6cYIiWq4M4keQ7g9PeZKYrwIJt4KclHRB9DPZnMcPY6aKGy7RpyAz-Joptt5xraLHE1NZO8vObGbCKza5_mw1BbUDbKgB_lZL9urIeeX5cXV2_xXDYDCsvDkZgZlnlckGoaIpcrMUoLV7KUr_5ZyndiN__W2SLjt5qSxXcchNyDDgI2rPblvu984XUZU-lDzRKzcr2CoPTpnjm2BldnE7j35KEFiaQVZR5Fnh6LZ8FlnKs60mBYnMVcMwXiqIX6j-g9W2Ed-3eov9VPubBfpEQAX3oKwzaiYvXVg0kISTfBtAI5MlFT-mR8fpWyNRIhQJm2ZMdFv3cvWKzp3sli0h1xuSvQCFVw3j3Qa1pnowPL8hVoqyYnAMxD6O-1EnfAPCBxHdTXNJ5AZTLslwRmgEtZ-4s9KK8ayd3-0LUWV06d9nWAEEQKTg8ybWcg1ulpXCLnnjp-lIdRqOi7SySDPtDkw-w3C6oGGlCxJ0UmGvMkQbHJK2tQPhBTiH4hdEnwR-2EMKTkJ-H3CnYP3Fz134ldcaCPZkPrH6ODy_chAiJPiBotnwXguJ2K4K6rflnJpEGdbAQIx4gGpH4hWN-4062lP3hCeLxy1RxGNnueTBrl-PmcvqU_alOkkgKTAMp_x6GmPuV8prk_r1rNiHc-x25qt8ii50DTWO2xosB0FGIRJKw4METTW6nqRKTVgZidRsIqpOQ3BiF0KDEqZJuR4Jp7xlfnOLi-l64NP0mWb6m2qL4h9uHj8mYVaShMdrUab3DGmZWagfNJM6rmPJjlg2isr0jOX8mVd4gQsoIdZOLaqRMJUqlhvvVI44snPRLtf5ogW1C2NfeRWDSCtk9M5DsAK8yphnPFQz0SFLhNlq3iDw4YFe563r9dyf42V2hWc3m65wXJ3wyM7nG20YcBs8bsXLeT90er0FjEDrBQc0HWlw2m6wUGXNpfXC0x82rA9udg&amp;reqid=49NY74OaV1&amp;type=CLICK" target="_blank" rel="nofollow">
            <picture class="webpimg-container">
               <source type="image/webp" srcset="https://salt.tikicdn.com/cache/w1080/ts/tka/12/38/43/e03d71a9ded46b8027026c0e48720603.png.webp 1x, https://salt.tikicdn.com/cache/w1080/ts/tka/12/38/43/e03d71a9ded46b8027026c0e48720603.png.webp 2x">
               <img src="https://salt.tikicdn.com/ts/tka/12/38/43/e03d71a9ded46b8027026c0e48720603.png" alt="//tka.tiki.vn/pixel/pixel?data=JMCfjc88FFkrXW1MY6cYIiWq4M4keQ7g9PeZKYrwIJt4KclHRB9DPZnMcPY6aKGy7RpyAz-Joptt5xraLHE1NZO8vObGbCKza5_mw1BbUDbKgB_lZL9urIeeX5cXV2_xXDYDCsvDkZgZlnlckGoaIpcrMUoLV7KUr_5ZyndiN__W2SLjt5qSxXcchNyDDgI2rPblvu984XUZU-lDzRKzcr2CoPTpnjm2BldnE7j35KEFiaQVZR5Fnh6LZ8FlnKs60mBYnMVcMwXiqIX6j-g9W2Ed-3eov9VPubBfpEQAX3oKwzaiYvXVg0kISTfBtAI5MlFT-mR8fpWyNRIhQJm2ZMdFv3cvWKzp3sli0h1xuSvQCFVw3j3Qa1pnowPL8hVoqyYnAMxD6O-1EnfAPCBxHdTXNJ5AZTLslwRmgEtZ-4s9KK8ayd3-0LUWV06d9nWAEEQKTg8ybWcg1ulpXCLnnjp-lIdRqOi7SySDPtDkw-w3C6oGGlCxJ0UmGvMkQbHJK2tQPhBTiH4hdEnwR-2EMKTkJ-H3CnYP3Fz134ldcaCPZkPrH6ODy_chAiJPiBotnwXguJ2K4K6rflnJpEGdbAQIx4gGpH4hWN-4062lP3hCeLxy1RxGNnueTBrl-PmcvqU_alOkkgKTAMp_x6GmPuV8prk_r1rNiHc-x25qt8ii50DTWO2xosB0FGIRJKw4METTW6nqRKTVgZidRsIqpOQ3BiF0KDEqZJuR4Jp7xlfnOLi-l64NP0mWb6m2qL4h9uHj8mYVaShMdrUab3DGmZWagfNJM6rmPJjlg2isr0jOX8mVd4gQsoIdZOLaqRMJUqlhvvVI44snPRLtf5ogW1C2NfeRWDSCtk9M5DsAK8yphnPFQz0SFLhNlq3iDw4YFe563r9dyf42V2hWc3m65wXJ3wyM7nG20YcBs8bsXLeT90er0FjEDrBQc0HWlw2m6wUGXNpfXC0x82rA9udg&amp;reqid=49NY74OaV1&amp;type=CLICK" width="300" srcset="https://salt.tikicdn.com/cache/w1080/ts/tka/12/38/43/e03d71a9ded46b8027026c0e48720603.png 1x, https://salt.tikicdn.com/cache/w1080/ts/tka/12/38/43/e03d71a9ded46b8027026c0e48720603.png 2x" class="WebpImg__StyledImg-sc-h3ozu8-0 fWjUGo" style="width: 300px; overflow: hidden;">
            </picture>
         </a>
      </div>
   </div>
</div>
</template>
<script>
export default {
   props: {
      publisher: {
         type: String,
         default: ''
      },
      bookAuthor: {
         type: String,
         default: ''
      },
   }
}
</script>
<style lang="scss" scoped>
  .detail-info {
    display: flex;
    margin-top: 16px;

    .left {
      flex: 1 1 0%;

      .group {
        margin-bottom: 16px;
        border-radius: 4px;
        background-color: rgb(255, 255, 255);

        .blockTitle__wrapper {
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

        .content {
          width: 920px;
          padding: 0px 16px 16px;
          display: inline-block;
          color: rgb(36, 36, 36);
          text-align: justify;
          border-radius: 4px;

          table {
            max-width: 100%;
            border-collapse: collapse;
            border-spacing: 0px;
            line-height: 21px;
            width: 100% !important;

            .custom-item {
               width: 220px;
               vertical-align: top;
               color: rgb(79, 79, 79);
               font-size: 13px;
               font-weight: 500;
               background: rgb(239, 239, 239);
               padding: 10px 15px;
            }

            .item-content {
               vertical-align: top;
               color: rgb(79, 79, 79);
               font-size: 13px;
               font-weight: 500;
               padding: 10px 15px;
            }
          }

          .toggleContent__wrapper {
            .toggleContent__view {
              p {
                margin-top: 5px;
                margin-bottom: 12px;
                line-height: 21px;
                word-break: break-word;
              }
            }
          }
        }
      }
    }

    .right {
      margin-left: 8px;
    }
  }
</style>
