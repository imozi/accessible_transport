<script setup lang="ts">
import type { RequestApi } from '~/types';
import { columns  } from './columns';

type RequestTableProps = {
  data: RequestApi[]
}

const props = defineProps<RequestTableProps>()

</script>

<template>
  <Table ref="table" :columns="columns" :data="props.data" field-search="status"></Table>
</template>

<style lang="scss"></style>
