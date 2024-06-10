<script setup lang="ts">
import type { Table } from '#build/components';
import { columns, requests } from './columns'
</script>

<template>
  <Table ref="table" :columns="columns" :data="requests" />
</template>

<style lang="scss"></style>