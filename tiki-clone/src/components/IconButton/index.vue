<template>
    <div
    class="icon-button"
    :class="[
      isActive ? 'is-active' : '',
      className
    ]"
  >
    <img class="icon" :src="isActive ? imageUrlActive : imageUrl" alt="Home icon" width="24" height="24">
    <div class="button-name">{{ buttonName }}</div>
  </div>
</template>
<script>
export default {
  props: {
    imageUrl: {
      type: String,
      default: ''
    },
    imageUrlActive: {
      type: String,
      default: ''
    },
    buttonName: {
      type: String,
      default: ''
    },
    isActive: {
      type: Boolean,
      default: false
    },
    className: {
      type: String,
      default: ''
    }
  }
}
</script>
<style lang="scss">
  .icon-button {
    display: flex;
    padding: 8px 16px;
    border-radius: 8px;
    cursor: pointer;

    &:hover {
      background-color: rgba(39, 39, 42, 0.12);
    }

    &.is-active {
      .button-name {
        color: #0a68ff;
        font-weight: 500;
      }

      &:hover {
        background-color: rgba(0, 96, 255, 0.12);
      }
    }

    .icon {
      margin-right: 4px;
    }

    .button-name {
      font-weight: 400;
      font-size: 14px;
      line-height: 150%;
      color: rgb(128, 128, 137);
    }
  }
</style>
