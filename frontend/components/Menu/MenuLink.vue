<script setup lang="ts">

type MenuItemProps = {
  props: {
    name: string,
    icon: string,
    link: string
  },
  activeClass: string
}

const { props } = defineProps<MenuItemProps>()
</script>


<template>
  <NuxtLink :to="props.link" :active-class="activeClass">
    <Icon :name="props.icon" />
    <span>{{ props.name }}</span>
  </NuxtLink>
</template>
