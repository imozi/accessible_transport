<script setup lang="ts">
import { columns, requests } from './columns';
</script>

<template>
  <Table ref="table" :columns="columns" :data="requests" field-search="passenger"></Table>
</template>

<style lang="scss"></style>
