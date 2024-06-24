<script setup lang="ts">
import type { RequestApi } from '~/types';
const config = useRuntimeConfig();

definePageMeta({
  name: 'Заявки',
});

useSeoMeta({
  title: 'Заявки',
});

const { data, pending, refresh } = await useFetch<RequestApi[]>(`${config.public.BACKEND}/request/list`);
</script>

<template>
  <PageWrapper>
    <Icon v-if="!data" name="eos-icons:bubble-loading" width="50" height="50" class="text-[#112448] m-auto" />
    <RequestsTable v-else :data="data" :pending="pending" :refresh="refresh" />
  </PageWrapper>
</template>
