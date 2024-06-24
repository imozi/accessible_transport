<script setup lang="ts">
import type { Analytics, RequestApi } from '~/types';
const config = useRuntimeConfig();
import { DateFormatter } from '@internationalized/date';
import type { GanttBarObject } from '@infectoone/vue-ganttastic';
import dayjs from 'dayjs';
import 'dayjs/locale/ru';

dayjs.locale('ru');

interface RequestAnalytics extends GanttBarObject {
  date_start: string;
  date_end: string;
}

type AnalyticsFormatedData = {
  employee: {
    id: number;
    full_name: string;
    date: string;
    lunch: string;
  };
  requests: RequestAnalytics[];
};

definePageMeta({
  name: 'Расписание',
});

useSeoMeta({
  title: 'Расписание',
});

const isOpenDialog = ref<boolean>(false);
const requestData = ref<RequestApi>();

const formatDate = (date: string) => {
  return new DateFormatter('ru-Ru', {
    dateStyle: 'short',
  }).format(new Date(date));
};

const { data } = await useFetch<Analytics[]>(`${config.public.BACKEND}/employee/analytics`);
const { data: requests, pending, refresh } = await useFetch<RequestApi[]>(`${config.public.BACKEND}/request/list`);
const formatedData = ref<AnalyticsFormatedData[] | null>();

const formatData = () => {
  if (!data) return;

  const temp = [] as AnalyticsFormatedData[];

  data.value?.forEach((item) => {
    const aData = { employee: {}, requests: [] as any } as AnalyticsFormatedData;
    const rawItem = toRaw(item);
    const requestsFormat = { ganttBarConfig: {} } as RequestAnalytics;

    const formatedDate = `${formatDate(rawItem.work_day)} ${rawItem.work_time}`;
    const formatLunchStart = rawItem.lunch_start.split(':');
    const formatLunchEnd = rawItem.lunch_end.split(':');

    aData.employee.id = rawItem.id;
    aData.employee.date = formatedDate;
    aData.employee.full_name = rawItem.full_name;
    aData.employee.lunch = `${formatLunchStart[0]}:${formatLunchStart[1]}:${formatLunchEnd[0]}:${formatLunchEnd[0]}`;

    requestsFormat.date_start = `${rawItem.work_day} ${formatLunchStart[0]}:${formatLunchStart[1]}`;
    requestsFormat.date_end = `${rawItem.work_day} ${formatLunchEnd[0]}:${formatLunchEnd[1]}`;
    requestsFormat.ganttBarConfig.id = `${rawItem.id}`;
    requestsFormat.ganttBarConfig.label = 'Обед';
    requestsFormat.ganttBarConfig.style = {
      background: '#fde68a ',
      fontSize: '10px',
      borderRadius: '2px',
      cursor: 'pointer',
    };

    aData.requests.push(requestsFormat);

    item.requests.forEach((request) => {
      const requestsFormat = { ganttBarConfig: {} } as RequestAnalytics;

      const formatDateStart = request.time_start.split(':');
      const formatDateEnd = request.time_end.split(':');

      requestsFormat.date_start = `${request.date} ${formatDateStart[0]}:${formatDateStart[1]}`;
      requestsFormat.date_end = `${request.date} ${formatDateEnd[0]}:${formatDateEnd[1]}`;

      requestsFormat.ganttBarConfig.id = `${item.id}:${request.id}`;
      requestsFormat.ganttBarConfig.label = `${request.id}`;
      requestsFormat.ganttBarConfig.style = {
        background: '#C7DAFF',
        fontSize: '8px',
        borderRadius: '2px',
        cursor: 'pointer',
      };

      aData.requests.push(requestsFormat);
    });

    temp.push(aData);
  });

  formatedData.value = temp;
};

onMounted(() => {
  formatData();
});

const onClickBar = async ({ bar, e }: { bar: GanttBarObject; e: MouseEvent }) => {
  const { id, label } = bar.ganttBarConfig;
  if (label === 'Обед') return;

  const data = await $fetch<RequestApi>(`${config.public.BACKEND}/request/${id.split(':')[1]}`);

  isOpenDialog.value = true;
  requestData.value = data;
};
</script>

<template>
  <PageWrapper>
    <h2 v-if="!data?.length" class="m-auto font-medium text-xl flex items-center gap-x-2">
      <Icon name="marketeq:diagram-bar-3" />
      Распределите заявки что бы увидеть диаграмму
    </h2>

    <template v-else>
      <ScheduleTable
        v-if="requests"
        :data="requests.filter((req) => req.status === 'Не распределена')"
        :pending="pending"
        :refresh="refresh"
      />

      <g-gantt-chart
        :chart-start="`${data[0].work_day} 00:00`"
        :chart-end="`${data[0].work_day} 23:59`"
        precision="hour"
        font="Nunito"
        bar-start="date_start"
        bar-end="date_end"
        label-column-title="Сотрудники"
        grid
        current-time-label="Текущее время"
        highlighted-units
        current-time
        @click-bar="onClickBar"
      >
        <g-gantt-row
          v-for="item of formatedData"
          :label="`${item.employee.full_name} ${item.employee.date}`"
          :bars="item.requests"
          highlight-on-hover
          :key="item.employee.id"
        />
      </g-gantt-chart>
    </template>
  </PageWrapper>
  <UiDialog v-model:open="isOpenDialog">
    <UiDialogTrigger as-child></UiDialogTrigger>
    <UiDialogContent class="sm:max-w-[700px] p-0">
      <UiDialogHeader>
        <UiDialogTitle>Заявка № {{ requestData?.id }}</UiDialogTitle>
        <UiDialogDescription
          >Назначена на {{ requestData?.employee?.map((e) => e.full_name).join(' ') }}
        </UiDialogDescription>
      </UiDialogHeader>
      <div class="grid gap-4 px-6 py-4 pb-4 text-muted-foreground relative">
        <p>
          <b>Пассажир:</b> {{ requestData?.passenger.first_name }} {{ requestData?.passenger.second_name[0] }}.
          {{ requestData?.passenger.patronymic[0] }}.
        </p>
        <p><b>Категория:</b> {{ requestData?.category }}</p>
        <p><b>Дата заявки:</b> {{ formatDate(requestData?.date as unknown as string) }}</p>
        <p>
          <b>Время:</b> {{ requestData?.time_start.split(':')[0] }}:{{ requestData?.time_start.split(':')[1] }} -
          {{ requestData?.time_end.split(':')[0] }}:{{ requestData?.time_end.split(':')[1] }}
        </p>
        <p><b>Маршрут:</b> {{ requestData?.from_station }} - {{ requestData?.to_station }}</p>
        <p class="absolute right-4 top-0 text-sm p-1 text-white rounded-sm bg-green-700">
          <b>Статус заявки:</b> {{ requestData?.status }}
        </p>
      </div>
    </UiDialogContent>
  </UiDialog>
</template>

<style lang="scss">
.g-gantt-bar-label {
  padding: 0;
}

.g-label-column-row {
  font-size: 10px;
  font-weight: 700;
  padding: 0 10px;
}

.g-gantt-tooltip {
  z-index: 100;
}

.g-grid-current-time-text {
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  width: max-content;
}

.g-label-column-header {
  font-size: 12px;
  font-weight: 700;
}
</style>
