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
  }
})

const value = ref('')
</script>

<template>
  <div style="max-width: 300px;">
    <va-input
      v-model="value"
      class="mb-6"
      :label="label"
      :placeholder="placeholder"
    />
  </div>
</template>

<style lang="scss" scoped>

</style>
