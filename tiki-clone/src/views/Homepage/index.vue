<template>
  <div class="home-page">
    <div class="home-page__body">
      <Sidebar />

      <div class="main">
        <PromotionContainer />
        <FeaturedCollection />
        <GoodPriceToday />
        <HomeBrand />
        <GoodPriceBrand />
        <HightlightList />
        <TodayRecommend />

        <PageFooterInner class="custom-footer"/>

      </div>


    </div>
  </div>
</template>

<script>
import Sidebar from './Sidebar/index.vue'
import PromotionContainer from './PromotionContainer/index.vue'
import FeaturedCollection from './FeaturedCollection/index.vue'
import GoodPriceToday from './GoodPriceToday/index.vue'
import HomeBrand from './HomeBrand/index.vue'
import GoodPriceBrand from './GoodPriceBrand/index.vue'
import HightlightList from './HightlightList/index.vue'
import TodayRecommend from './TodayRecommend/index.vue'
import PageFooterInner from '../../components/PageFooterInner/index.vue'

export default {
  components: {
    Sidebar,
    PromotionContainer,
    FeaturedCollection,
    GoodPriceToday,
    HomeBrand,
    GoodPriceBrand,
    HightlightList,
    TodayRecommend,
    PageFooterInner
  }
}
</script>
<style lang="scss" scoped>
  .home-page {
    background-color: #f5f5fa;
    min-height: calc(100vh - 80px - 8px);
    padding-top: 16px;

    display: flex;
    justify-content: center;

    &__body {
      display: flex;
      width: 1392px;

      .main {
        width: 100%;
        height: 100%;
        margin-left: 24px;

        .custom-footer {
          margin-top: 0;
        }
      }
    }
  }
</style>
