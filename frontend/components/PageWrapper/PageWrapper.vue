<script setup lang="ts">

const props = defineProps<{title?: string}>()
const name = useRoute().meta.name

if(props.title)
usePageName().value.title = props.title;

if (name)
usePageName().value.title = name;
</script>

<template>
  <div class="page__content">
    <slot />
  </div>
</template>
