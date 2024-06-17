<script setup lang="ts">
definePageMeta({
  layout: 'login',
});

useSeoMeta({
  title: 'Вход'
})

</script>

<template>
  <AuthForm class="max-w-[500px]" />
</template>
