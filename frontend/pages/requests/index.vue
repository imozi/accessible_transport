<script setup lang="ts">
definePageMeta({
  name: 'Заявки'
})

import { columns, payments } from '../../components/RequestsTable/columns'


</script>

<template>
  <PageWrapper>
    <template #top>
      <div class="flex justify-between">
        <Modal />
        <div class="relative w-full max-w-sm text-sm font-normal items-center shadow-lg shadow-[#0D21390D]">
          <UiInput id="search" type="text" placeholder="Поиск..." class="pl-10 " />
          <span class="absolute start-0 inset-y-0 flex items-center justify-center px-2">
            <Icon name="iconamoon:search" width="18" hidden="18" class="text-muted-foreground" />
          </span>
        </div>
      </div>
    </template>
    <template #content>
      <RequestsTable :columns="columns" :data="payments" />
    </template>
  </PageWrapper>
</template>