<script setup lang="ts">
import type { Employee } from '~/types';

const {params} = useRoute()
const config = useRuntimeConfig();

const {data:employee} = await useFetch<Employee>(`${config.public.BACKEND}/employee/${params.id}`);
const {data:requests} = await useFetch<Employee>(`${config.public.BACKEND}/employee/${params.id}/requests`);

</script>

<template>
  <PageWrapper v-if="employee" :title="employee.full_name">
  <pre>{{ requests }}</pre>
</PageWrapper>
</template>