<template>
  <div class="tiki-bookstore-page">
    <div class="breadcrumb-wrapper">
      <div class="breadcrumb-container">
        <va-breadcrumbs
          separator=">"
          class="custom-breadcrumb"
        >
          <va-breadcrumbs-item label="Trang chủ" class="homepage-breadcrumb" @click="onClickGotoHome"/>
          <va-breadcrumbs-item label="Nhà sách Tiki" class="bookstore-breadcrumb" />
        </va-breadcrumbs>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  methods: {
    onClickGotoHome() {
      this.$router.push({ name: 'home' });
    }
  }
}
</script>
<style lang="scss" scoped>
  .tiki-bookstore-page {
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

          .homepage-breadcrumb {
            margin-right: 5.5px;

            &:hover {
              text-decoration: underline;
              cursor: pointer;
            }
          }

          .bookstore-breadcrumb {
            margin-left: 8.5px;
            color: rgb(56, 56, 61);
          }
        }
      }
    }
  }
</style>
