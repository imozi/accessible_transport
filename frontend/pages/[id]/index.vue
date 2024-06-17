<script setup lang="ts">
import type { Employee, RequestApi } from '~/types';
const page = usePageName();

definePageMeta({
  layout: 'employee',
});


const config = useRuntimeConfig();

const { getUser } = useStateEmployee();
const employee = getUser() as Employee

useSeoMeta({
  title: () => `Заявки | ${employee.full_name}`
})

const { data, pending, refresh } = await useFetch<RequestApi[]>(`${config.public.BACKEND}/employee/${(employee as Employee).id}/requests/`)

const exit = () => {
  const { removeUser } = useStateEmployee();
  removeUser();
  navigateTo('/', { replace: true });
};

</script>

<template>
  <PageWrapper v-if="employee" :title="employee.full_name">
    <div class="employee__wrapper">
      <div class="employee__row">
        <div class="employee__title">
          <h1>{{ page.title }}</h1>
        </div>
        <UiButton @click="exit" class="w-full max-w-[200px] flex gap-x-3">
          <Icon name="system-uicons:exit-left" />
          Выйти из аккаунта
        </UiButton>
      </div>
      <Icon v-if="!data" name="eos-icons:bubble-loading" width="50" height="50" class="text-[#112448] m-auto" />
      <CurrentEmployeeSingleTable v-else :data="data" :pending="pending" :refresh="refresh" />
    </div>
  </PageWrapper>
</template>

<style lang="scss">
.employee {

  @apply w-full h-full;

  & .page__content {
    @apply w-full h-full;
  }

  &__row {
    @apply flex items-center justify-between;
  }

  &__wrapper {
    @apply w-full h-full p-20 flex flex-col gap-y-5;
  }

  &__title {
    @apply text-3xl font-bold;
  }
}
</style>
