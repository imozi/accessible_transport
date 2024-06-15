<script setup lang="ts" generic="TData, TValue">
import type { ColumnDef, ColumnFiltersState } from '@tanstack/vue-table';
import {
  FlexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  useVueTable,
} from '@tanstack/vue-table';
import { valueUpdater } from '~/lib/utils';

const props = defineProps<{
  columns: ColumnDef<TData, TValue>[];
  data: TData[];
  fieldSearch: string;
  fieldSearchText: string;
  pending: boolean;
}>();

const columnFilters = ref<ColumnFiltersState>([]);
const rowSelection = ref({});
const isSelected = ref<boolean>(false);
const pageSizes = [10, 20, 30, 40, 50];
const selected = useSelectedRow()
const isAction = ref<boolean>(false)

const emit = defineEmits(['on:action'])

function handlePageSizeChange(n: string) {
  table.setPageSize(Number(n));
}

const table = useVueTable({
  get data() {
    return props.data;
  },
  get columns() {
    return props.columns;
  },
  getCoreRowModel: getCoreRowModel(),
  getPaginationRowModel: getPaginationRowModel(),
  getFilteredRowModel: getFilteredRowModel(),
  onColumnFiltersChange: (updaterOrValue) => valueUpdater(updaterOrValue, columnFilters),
  onRowSelectionChange: (updaterOrValue) => {
    valueUpdater(updaterOrValue, rowSelection);

    if (Object.keys(rowSelection.value).length) {
      isSelected.value = true
      selected.value.select = true

    } else {
      isSelected.value = false
      selected.value.select = false
    }


  },
  state: {
    get columnFilters() {
      return columnFilters.value;
    },
    get rowSelection() {
      return rowSelection.value;
    },
  },
});

watch(isAction, () => {
  if (isAction) {
    isAction.value = false
    emit('on:action')
  }
})

provide('table', table);
provide('isSelected', isSelected);
provide('isAction', isAction);
</script>

<template>
  <div class="flex items-baseline">
    <slot />
    <div class="relative w-full max-w-sm ml-auto text-sm font-normal items-center shadow-lg shadow-[#0D21390D]">
      <UiInput id="search" type="text" :placeholder="fieldSearchText" class="pl-10"
        :model-value="table.getColumn(`${props.fieldSearch}`)?.getFilterValue() as string | number"
        @update:model-value="table.getColumn(`${props.fieldSearch}`)?.setFilterValue($event)" />
      <span class="absolute start-0 inset-y-0 flex items-center justify-center px-2">
        <Icon name="iconamoon:search" width="18" hidden="18" class="text-muted-foreground" />
      </span>
    </div>
  </div>

<slot name="statistic" />

  <div class="table">
    <Loader v-if="pending" />
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
            <UiTableCell :colspan="columns.length" class="h-24 text-center"> Данных нет </UiTableCell>
          </UiTableRow>
        </template>
      </UiTableBody>
    </UiTable>
  </div>
  <div class="flex gap-x-4 items-center">
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

    <div class="ml-auto">
      <UiSelect @update:model-value="handlePageSizeChange">
        <UiSelectTrigger class="w-auto">
          <SelectValue :placeholder="`${table.getState().pagination.pageSize}`" />
        </UiSelectTrigger>
        <UiSelectContent>
          <UiSelectGroup>
            <UiSelectItem v-for="pageSize in pageSizes" :key="pageSize" :value="`${pageSize}`">{{ pageSize }}
            </UiSelectItem>
          </UiSelectGroup>
        </UiSelectContent>
      </UiSelect>
    </div>
  </div>
</template>

<style lang="scss">
.table {
  @apply relative block bg-white overflow-auto scrollbar-thumb-[#D1E0FF] scrollbar-thin scrollbar-thumb-rounded-xl scrollbar-track-rounded-xl scrollbar-corner-rounded-xl scrollbar-track-[#F7F9FA] border rounded-md shadow-lg shadow-[#0D21390D];
}
</style>
