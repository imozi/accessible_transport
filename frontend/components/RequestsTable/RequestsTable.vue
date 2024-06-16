<script setup lang="ts">
import type { RequestApi } from '~/types';
import { columns } from './columns';

type RequestTableProps = {
  data: RequestApi[];
  pending: boolean;
  refresh: () => Promise<void>;
};

const config = useRuntimeConfig();
const props = defineProps<RequestTableProps>();
const isDistribution = ref<boolean>(false);
const isShowStatistic = ref<boolean>(false);
const isOpen = ref(false);
let count = 0;
let statistic = {
  new: 0,
  notDistributed: 0,
  participationInDistribution: 0,
  total: 0,
};

const statisticTemp = {
  new: 0,
  notDistributed: 0,
  participationInDistribution: 0,
  total: 0,
};

onMounted(() => {
  if (props.data) {
    statistic.new = props.data.filter((item) => item.status === 'Новая').length;
    statistic.total = props.data.length;
    statistic.notDistributed = props.data.filter((item) => item.status === 'Не распределена').length;
    statistic.participationInDistribution = statistic.new + statistic.notDistributed;
  }
});

const onClickDistribution = async () => {
  if (count > 0) {
    statistic = {...statisticTemp};
    count = 0
  }

  isDistribution.value = true;
  isShowStatistic.value = false;
  await $fetch(`${config.public.BACKEND}/request/distribution`);
  await props.refresh();

  isDistribution.value = false;
  isShowStatistic.value = true;
  isOpen.value = false

  count+=1;

  if (props.data) {
    statisticTemp.new = props.data.filter((item) => item.status === 'Новая').length;
    statisticTemp.total = props.data.length;
    statisticTemp.notDistributed = props.data.filter((item) => item.status === 'Не распределена').length;
    statisticTemp.participationInDistribution = statisticTemp.new + statisticTemp.notDistributed;
  }
};

const onClickShowStatistic = () => {
  isShowStatistic.value = false;
};
</script>

<template>
  <Table
    :pending="props.pending"
    :columns="columns"
    :data="props.data"
    field-search="id"
    field-search-text="Поиск по id или статусу заявки..."
    @on:action="props.refresh"
  >
    <div class="distribution">
      <UiButton
        v-auto-animate="{ duration: 150 }"
        variant="outline"
        :class="`shadow-lg shadow-[#0D21390D] min-w-[230px] items-center gap-x-3 text-sm w-full max-w-60 text-[#3A76EE] hover:text-[#3A76EE]`"
        :disabled="isDistribution"
        @click="onClickDistribution"
      >
        <span v-if="!isDistribution" class="flex items-center gap-x-3">
          <Icon name="fluent-mdl2:timeline-delivery" />
          Распределение
        </span>
        <span v-else class="flex items-center gap-x-3">
          <LucideLoader2 class="w-4 h-4 mr-2 animate-spin" /> Идет распределение
        </span>
      </UiButton>
    </div>

    <template #statistic v-if="isShowStatistic">
      <div class="flex gap-x-5">
        <UiCollapsible v-model:open="isOpen" class="w-[450px] space-y-2">
          <div class="flex items-center justify-between space-x-4 px-4 py-2 rounded-md border">
            <h4 class="text-sm font-semibold">Статистика распределения</h4>
            <UiCollapsibleTrigger as-child>
              <UiButton variant="ghost" size="sm" class="w-9 h-auto p-0">
                <LucideChevronsUpDown width="16" height="16" />
                <span class="sr-only">Переключение</span>
              </UiButton>
            </UiCollapsibleTrigger>
          </div>
          <UiCollapsibleContent class="space-y-2">
            <p class="rounded-md border px-4 py-3 font-mono text-sm">Всего заявок: {{ data.length }}</p>
            <p class="rounded-md border px-4 py-3 font-mono text-sm">
              Участвовало в распределении: {{ statistic.participationInDistribution }}
            </p>
            <p class="rounded-md border px-4 py-3 font-mono text-sm">
              Распределенно всего заявок:
              {{
                statistic.participationInDistribution -
                (data.filter((item) => item.status === 'Не распределена').length +
                  data.filter((item) => item.status === 'Новая').length)
              }}
              из {{ statistic.participationInDistribution }}
            </p>
            <p class="rounded-md border px-4 py-3 font-mono text-sm">
              Распределенно новых заявок: {{ statistic.new - data.filter((item) => item.status === 'Новая').length }} из
              {{ statistic.new }}
            </p>
            <p class="rounded-md border px-4 py-3 font-mono text-sm" v-if="statistic.notDistributed">
              Распределенно не распределенных заявов:
              {{ statistic.notDistributed - data.filter((item) => item.status === 'Не распределена').length }} из
              {{ statistic.notDistributed }}
            </p>
            <p class="rounded-md border px-4 py-3 font-mono text-sm" v-else>
              Не распределенно заявов: {{ data.filter((item) => item.status === 'Не распределена').length }}
            </p>

            <span class="block px-4 py-1 text-xs text-muted-foreground" v-if="data.filter((item) => item.status === 'Не распределена').length"
              >Для {{ data.filter((item) => item.status === 'Не распределена').length }} не распределенных заявок не
              нашлось свободных сотрудников</span
            >
          </UiCollapsibleContent>
        </UiCollapsible>
        <UiButton v-if="isShowStatistic" variant="secondary" @click="onClickShowStatistic">Скрыть</UiButton>
      </div>
    </template>
  </Table>
</template>

<style lang="scss"></style>
