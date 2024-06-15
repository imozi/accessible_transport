<script setup lang="ts">
import type { RequestApi } from '~/types';
import { columns } from './columns';

type RequestTableProps = {
  data: RequestApi[];
  pending: boolean;
  refresh: () => Promise<void>;
};

const props = defineProps<RequestTableProps>();



</script>

<template>
  <Table :pending="props.pending" :columns="columns" :data="props.data" field-search="id"
    field-search-text="Поиск по id заявки или фамилии пассажира..." @on:action="props.refresh">
  </Table>
</template>

<style lang="scss"></style>
