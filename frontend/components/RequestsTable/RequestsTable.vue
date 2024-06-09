<script setup lang="ts" generic="TData, TValue">
import type { ColumnDef } from '@tanstack/vue-table'
import {
  FlexRender,
  getCoreRowModel,
  getPaginationRowModel,
  useVueTable,
} from '@tanstack/vue-table'

const props = defineProps<{
  columns: ColumnDef<TData, TValue>[]
  data: TData[]
}>()

const table = useVueTable({
  get data() { return props.data },
  get columns() { return props.columns },
  getCoreRowModel: getCoreRowModel(),
  getPaginationRowModel: getPaginationRowModel(),
})

table.setPageSize(20)
</script>

<template>
  <div class="table">
    <UiTable class="table__container">
      <UiTableHeader>
        <UiTableRow v-for="headerGroup in table.getHeaderGroups()" :key="headerGroup.id">
          <UiTableHead v-for="header in headerGroup.headers" :key="header.id">
            <FlexRender v-if="!header.isPlaceholder" :render="header.column.columnDef.header"
              :props="header.getContext()" />
          </UiTableHead>
        </UiTableRow>
      </UiTableHeader>
      <UiTableBody>
        <template v-if="table.getRowModel().rows?.length">
          <UiTableRow v-for="row in table.getRowModel().rows" :key="row.id"
            :data-state="row.getIsSelected() ? 'selected' : undefined">
            <UiTableCell v-for="cell in row.getVisibleCells()" :key="cell.id">
              <FlexRender :render="cell.column.columnDef.cell" :props="cell.getContext()" />
            </UiTableCell>
          </UiTableRow>
        </template>
        <template v-else>
          <UiTableRow>
            <UiTableCell :colspan="columns.length" class="h-24 text-center">
              No results.
            </UiTableCell>
          </UiTableRow>
        </template>
      </UiTableBody>
    </UiTable>
  </div>
  <div class="flex gap-x-4 items-center justify-start">
    <span class="flex items-center gap-1">
      <div>Страница</div>
      <strong>
        {{ table.getState().pagination.pageIndex + 1 }} из
        {{ table.getPageCount() }}
      </strong>
    </span>
    <div class="flex gap-x-2">
      <UiButton variant="outline" size="sm" :disabled="!table.getCanPreviousPage()" @click="table.previousPage()">
      Предыдущая
    </UiButton>
    <UiButton variant="outline" size="sm" :disabled="!table.getCanNextPage()" @click="table.nextPage()">
      Следующая
    </UiButton>
    </div>
  </div>
</template>

<style lang="scss">
.table {
  @apply block overflow-auto scrollbar-thumb-[#172F5F] scrollbar-thin scrollbar-thumb-rounded-xl scrollbar-track-rounded-xl scrollbar-corner-rounded-xl scrollbar-track-[#D1E0FF] border rounded-md shadow-lg shadow-[#0D21390D];
}
</style>