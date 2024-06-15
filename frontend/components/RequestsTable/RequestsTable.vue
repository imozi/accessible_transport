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
  <div class="distribution">
    <UiButton variant="outline"
        :class="`shadow-lg shadow-[#0D21390D] items-center gap-x-3 text-sm w-full max-w-60 text-[#3A76EE] hover:text-[#3A76EE]`"
      >
        <Icon name="fluent-mdl2:timeline-delivery" />
        Распределение
      </UiButton>
  </div>
  
  </Table>
</template>

<style lang="scss"></style>
