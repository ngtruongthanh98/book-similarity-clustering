<script setup>
import { ref } from 'vue'

defineProps({
  label: {
    type: String,
    default: ''
  },
  placeholder: {
    type: String,
    default: ''
  },
  class: {
    type: String,
    default: ''
  }
})

const value = ref('')
</script>

<template>
  <va-input
    v-model="value"
    :class="class"
    :label="label"
    :placeholder="placeholder"
  />
</template>

<style lang="scss" scoped>

</style>
