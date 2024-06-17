<script setup lang="ts">
import type { Employee } from '~/types';

const { getUser } = useStateEmployee();

const user = getUser() as Employee;

if ((user as any as { user: string }).user) {
  navigateTo('/requests');
}

if (user.id) {
  navigateTo(`/${user.personnel_number}`);
}
</script>

<template>
  <div class="login" v-if="!user">
    <div class="login__wrapper">
      <div class="login__column login__overlay">
        <div class="login__title">
          <h1>Сервис мониторинга и&nbsp;распределения заявок от маломобильных пассажиров</h1>
        </div>
      </div>
      <div class="login__column login__form">
        <slot />
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.login {
  @apply w-full h-full;

  &__wrapper {
    @apply grid grid-cols-2 w-full h-full;
  }

  &__column {
    @apply p-5;
  }

  &__overlay {
    @apply bg-[#112448] flex;
  }

  &__title {
    @apply m-auto text-white font-medium text-2xl max-w-[400px] text-center;
  }

  &__form {
    @apply flex relative;
  }
}
</style>
