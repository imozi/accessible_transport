<script setup lang="ts">
usePageName().value.title = useRoute().meta.name
</script>

<template>
  <div class="">
    <slot name="top" />
  </div>
  <div class="page__content">
    <slot name="content" />
    <slot />

  </div>
</template>