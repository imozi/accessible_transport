<script setup lang="ts">
import { columns, passengers } from './columns';
</script>

<template>
  <Table ref="table" :columns="columns" :data="passengers" field-search="second_name">
    <div class="flex gap-x-5">
      <PassengerForm />
      <RequestForm />
    </div>
  </Table>
</template>

<style lang="scss"></style>
