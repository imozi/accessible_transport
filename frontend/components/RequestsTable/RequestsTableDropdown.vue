<script setup lang="ts">
defineProps<{
  payment: {
    id: string
  }
}>()

function copy(id: string) {
  navigator.clipboard.writeText(id)
}
</script>

<template>
  <UiDropdownMenu>
    <UiDropdownMenuTrigger as-child>
      <UiButton variant="ghost" class="w-8 h-8 p-0">
        <span class="sr-only">Open menu</span>
        <LucideMoreHorizontal class="w-4 h-4" />
      </UiButton>
    </UiDropdownMenuTrigger>
    <UiDropdownMenuContent align="end">
      <UiDropdownMenuLabel>Действия</UiDropdownMenuLabel>
      <UiDropdownMenuItem>
        <LucidePencil class="mr-2 h-4 w-4" />
        <span>Редактировать</span>
      </UiDropdownMenuItem>
      <UiDropdownMenuSeparator />
      <UiDropdownMenuItem>
        <LucideDelete class="mr-2 h-4 w-4" />
        <span>Удалить</span>
      </UiDropdownMenuItem>

    </UiDropdownMenuContent>
  </UiDropdownMenu>
</template>