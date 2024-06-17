<script setup lang="ts">
import type { Employee, RequestApi } from '~/types';

const {params} = useRoute()
const config = useRuntimeConfig();

const {data:employee} = await useFetch<Employee>(`${config.public.BACKEND}/employee/${params.id}`);
const {data:requests, pending, refresh} = await useFetch<RequestApi[]>(`${config.public.BACKEND}/employee/${params.id}/requests`);

useSeoMeta({
  title: () => `Заявки | ${ employee.value?.full_name }`
})

</script>

<template>
  <PageWrapper v-if="employee" :title="employee.full_name">
    <Icon v-if="!requests" name="eos-icons:bubble-loading" width="50" height="50"  class="text-[#112448] m-auto" />
  <CurrentEmployeeTable v-else :data="requests" :pending="pending" :refresh="refresh" />
</PageWrapper>
</template>