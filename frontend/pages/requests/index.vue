<script setup lang="ts">
import type { RequestsTable } from '#build/components';

definePageMeta({
  name: 'Заявки'
})

</script>

<template>
  <PageWrapper>
    <RequestsTable />
  </PageWrapper>
</template>