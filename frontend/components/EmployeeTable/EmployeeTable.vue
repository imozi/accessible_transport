<script setup lang="ts">
import type { Employee } from '~/types';
import { columns } from './columns';

type EmployeeTableProps = {
  data: Employee[];
  pending: boolean;
  refresh: () => Promise<void>;
};

const props = defineProps<EmployeeTableProps>();
</script>

<template>
  <Table
    :pending="props.pending"
    :columns="columns"
    :data="props.data"
    field-search="second_name"
    field-search-text="Поиск по фамилии..."
    @on:action="props.refresh"
  >
    <EmployeeForm @on:created="refresh" />
  </Table>
</template>

<style lang="scss"></style>
