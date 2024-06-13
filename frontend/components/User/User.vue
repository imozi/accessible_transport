<template>
  <div class="user">
    <div class="user__avatar">
      <UiAvatar size="sm" shape="square">
        <UiAvatarFallback>АД</UiAvatarFallback>
      </UiAvatar>
    </div>

    <div class="user__name">
      <p>Иванов Иван Иванович</p>
      <span>Администратор</span>
    </div>
  </div>
</template>

<style lang="scss">
.user {
  @apply flex gap-x-4;

  &__avatar {
    & > span {
      @apply bg-white;
    }
  }

  &__name {
    @apply flex flex-col justify-center;

    & > p {
      @apply uppercase font-semibold text-sm leading-[14px];
    }

    & > span {
      @apply text-xs text-muted leading-[12px];
    }
  }
}
</style>
