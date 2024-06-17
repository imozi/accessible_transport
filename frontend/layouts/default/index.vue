<script setup lang="ts">
import type { Employee } from '~/types';
const page = usePageName();

const { getUser } = useStateEmployee();

const user = getUser() as Employee;

if (!user.id && !(user as any as { user: string }).user) {
  navigateTo('/');
}

if (user.id) {
  navigateTo(`/${user.personnel_number}`);
}
</script>

<template>
  <div class="wrapper" v-if="user">
    <aside class="aside">
      <header class="aside__header">
        <h1>Сервис мониторинга и распределения заявок от маломобильных пассажиров</h1>
      </header>
      <User />
      <Menu />
    </aside>

    <main class="main">
      <div class="page">
        <h1>{{ page.title }}</h1>
        <Time />
      </div>
      <slot />
    </main>
  </div>
</template>

<style lang="scss">
.wrapper {
  @apply grid grid-cols-[340px_1fr] h-full;
}

.aside {
  @apply bg-[#172F5F] text-white p-8 flex flex-col gap-y-7;

  &__header {
    @apply font-bold text-sm uppercase;
  }
}

.main {
  @apply h-screen overflow-hidden overflow-y-scroll p-10 bg-[#F7F9FA] flex flex-col gap-y-8 scrollbar-thumb-[#D1E0FF] scrollbar-thin scrollbar-thumb-rounded-xl scrollbar-track-rounded-xl scrollbar-corner-rounded-xl scrollbar-track-[#F7F9FA];
}

.page {
  @apply flex justify-between;

  & h1 {
    @apply text-3xl font-bold;
  }

  &__content {
    @apply flex flex-col gap-y-8 flex-grow;
  }
}
</style>
