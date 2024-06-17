<script setup lang="ts">
const { getUser } = useStateEmployee();
import type { Employee } from '~/types';

const user = getUser() as Employee;

if (!user.id) {
  navigateTo(`/`);
}

if ((user as any as { user: string }).user) {
  navigateTo(`/requests`);
}
</script>

<template>
  <div class="employee" v-if="user.id">
    <slot />
  </div>
</template>

<style lang="scss"></style>
