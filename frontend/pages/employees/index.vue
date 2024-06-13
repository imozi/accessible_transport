<script setup lang="ts">
import type { Employee } from '~/types';
const config = useRuntimeConfig();

definePageMeta({
  name: 'Сотрудники',
});


const { data, pending, refresh } = await useFetch<Employee[]>(`${config.public.BACKEND}/employee/list`);
</script>

<template>
  <PageWrapper>
    <Icon v-if="!data" name="eos-icons:bubble-loading" width="50" height="50"  class="text-[#112448] m-auto" />
    <EmployeeTable v-else :data="data" :pending="pending" :refresh="refresh" />
  </PageWrapper>
</template>
