<script setup lang="ts">
import type { Employee } from '~/types';
import { columns  } from './columns';

type EmployeeTableProps = {
  data: Employee[]
}

const props = defineProps<EmployeeTableProps>()

</script>

<template>
  <Table ref="table" :columns="columns" :data="props.data" field-search="full_name"></Table>
</template>

<style lang="scss"></style>
