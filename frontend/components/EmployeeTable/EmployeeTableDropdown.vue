<script setup lang="ts">
defineProps<{
  request: {
    id: number | string;
  };
}>();
</script>

<template>
  <UiDropdownMenu>
    <UiDropdownMenuTrigger as-child>
      <UiButton variant="ghost" class="w-8 h-8 p-0">
        <span class="sr-only">Открыть меню</span>
        <LucideMoreHorizontal class="w-4 h-4" />
      </UiButton>
    </UiDropdownMenuTrigger>
    <UiDropdownMenuContent align="end">
      <UiDropdownMenuLabel>Действия</UiDropdownMenuLabel>
      <UiDropdownMenuItem>
        <LucideTableProperties class="mr-2 h-4 w-4" />
        <NuxtLink :to="`/employees/${request.id}`">Посмотреть заявки</NuxtLink>
      </UiDropdownMenuItem>
      <UiDropdownMenuSeparator />
      <UiDropdownMenuItem>
        <LucideDelete class="mr-2 h-4 w-4" />
        <span>Удалить</span>
      </UiDropdownMenuItem>
    </UiDropdownMenuContent>
  </UiDropdownMenu>
</template>
