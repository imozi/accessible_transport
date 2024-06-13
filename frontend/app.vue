<script setup lang="ts">
const config = useRuntimeConfig();

useStateMetroStation().fetch(`${config.public.BACKEND}/metro/stations`)
useStateCategories().fetch(`${config.public.BACKEND}/passenger/categories`)
</script>

<template>
  <NuxtLoadingIndicator />
  <NuxtLayout>
    <UiToaster />
    <NuxtPage />
  </NuxtLayout>
</template>
