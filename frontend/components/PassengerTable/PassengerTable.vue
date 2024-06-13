<script setup lang="ts">
import { columns } from './columns';
import type { Passenger } from '~/types';
const config = useRuntimeConfig();

const { data, pending, refresh } = await useFetch<Passenger[]>(`${config.public.BACKEND}/passenger/list`);
</script>

<template>
  <Table ref="table" :columns="columns" v-if="data" :data="data" field-search="second_name" @on:delete="refresh">
    <div class="flex gap-x-5">
      <RequestForm />
      <PassengerForm @on:created="refresh" />
    </div>
  </Table>
</template>

<style lang="scss"></style>
