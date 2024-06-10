<script setup lang="ts">
usePageName().value.title = useRoute().meta.name
</script>

<template>
  <div class="page__content">
    <slot />
  </div>
</template>