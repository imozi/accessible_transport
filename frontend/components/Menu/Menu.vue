<script setup lang="ts">
const menuData = useStateMenu();

const logaut = { icon: 'system-uicons:exit-left', name: 'Выйти из аккаунта'};

const exit = () => {
  const { removeUser } = useStateEmployee();
  removeUser();
  navigateTo('/', { replace: true });
};
</script>

<template>
  <ul class="menu">
    <li class="menu__item" v-for="menuItem of menuData" :key="menuItem.id">
      <MenuLink class="menu__link" active-class="menu__link--current" :props="menuItem" />
    </li>
    <li class="menu__item mt-auto">
      <UiButton variant="ghost" class="menu__link justify-start" active-class="menu__link--current" @click="exit">
        <Icon :name="logaut.icon" />
        {{ logaut.name }}
      </UiButton>
    </li>
  </ul>
</template>

<style lang="scss">
.menu {
  @apply text-[#D1E0FF] flex-grow flex flex-col;

  &__item {
    @apply flex text-sm;
  }

  &__link {
    @apply flex items-center flex-grow py-3 px-4 rounded-lg leading-none gap-x-4 transition hover:bg-[#112448] hover:text-white;

    & > svg {
      @apply text-[#6580B8];
    }

    &--current {
      @apply bg-[#112448] text-white;

      & > svg {
        @apply text-white;
      }
    }
  }
}
</style>
