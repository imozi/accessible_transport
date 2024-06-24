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
  <Table
    :pending="props.pending"
    :columns="columns"
    :data="props.data"
    field-search="id"
    field-search-text="Поиск по id или статусу заявки..."
    @on:action="props.refresh"
  >

  <template #statistic>
      <div class="flex gap-x-5">
        <p class="text-muted-foreground">Всего не распределенных заявок: {{ data.length }}</p>
      </div>
    </template>

  </Table>
</template>

<style lang="scss"></style>
