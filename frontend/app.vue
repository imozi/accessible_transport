<script setup lang="ts">
const config = useRuntimeConfig();

useStateMetroStation().fetch(`${config.public.BACKEND}/metro/stations`);
useStateCategories().fetch(`${config.public.BACKEND}/passenger/categories`);
useStateRequestStatus().fetch(`${config.public.BACKEND}/request/status`);

onMounted(() => {
  const root = document.querySelector('#dashboard');
  root?.classList.add('loaded');
});
</script>

<template>
  <NuxtLoadingIndicator :height="6" />
  <NuxtLayout>
    <UiToaster />
    <NuxtPage />
  </NuxtLayout>
</template>
