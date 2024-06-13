<script setup lang="ts">
import type { Passenger } from '~/types';
const config = useRuntimeConfig();

definePageMeta({
  name: 'Пассажиры',
});


const { data, pending, refresh } = await useFetch<Passenger[]>(`${config.public.BACKEND}/passenger/list`);
</script>

<template>
  <PageWrapper>
    <Icon v-if="!data" name="eos-icons:bubble-loading" width="50" height="50"  class="text-[#112448] m-auto" />
    <PassengerTable v-else :data="data" :pending="pending" :refresh="refresh" />
  </PageWrapper>
</template>
