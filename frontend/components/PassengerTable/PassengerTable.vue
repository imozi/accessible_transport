<script setup lang="ts">
import { passengers } from '~/data';
import { columns } from './columns';
</script>

<template>
  <Table ref="table" :columns="columns" :data="passengers" field-search="second_name">
    <div class="flex gap-x-5">
      <RequestForm />
      <PassengerForm />
    </div>
  </Table>
</template>

<style lang="scss"></style>
