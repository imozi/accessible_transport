<script setup lang="ts">
import { columns } from './columns';
import type { Passenger } from '~/types';

type PassengerProps = {
  data: Passenger[];
  pending: boolean;
  refresh: () => Promise<void>;
};

const props = defineProps<PassengerProps>();
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
    <div class="flex gap-x-5">
      <RequestForm />
      <PassengerForm @on:created="props.refresh" />
    </div>
  </Table>
</template>

<style lang="scss"></style>
