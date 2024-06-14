<script setup lang="ts">
import type { Employee } from '~/types';
import { useToast } from '../ui/toast/use-toast';

defineProps<{
  employee: {
    id: number | string;
  };
}>();

const config = useRuntimeConfig();
const { toast } = useToast();

const isAction = inject<globalThis.Ref<boolean>>('isDelete')

const onDelete = async (id: string | number) => {
  try {
    const passanger = await $fetch<Employee>(`${config.public.BACKEND}/employee/delete/${id}`, { method: 'DELETE' });
      isAction!.value = true;

    toast({
      title: `Сотрудник ${passanger.second_name} ${passanger.first_name[0]}. ${passanger.patronymic[0]}`,
      description: 'Успешно удалён',
      variant: 'success',
    });
  } catch (error: unknown) {
    if (error instanceof Error)
      toast({
        title: `Ошибка`,
        description: error.message,
        variant: 'destructive',
      });
  }
};
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
        <NuxtLink :to="`/employees/${employee.id}`">Посмотреть заявки</NuxtLink>
      </UiDropdownMenuItem>
      <UiDropdownMenuSeparator />
      <UiDropdownMenuItem @click="onDelete(employee.id)">
        <LucideDelete class="mr-2 h-4 w-4" />
        <span>Удалить</span>
      </UiDropdownMenuItem>
    </UiDropdownMenuContent>
  </UiDropdownMenu>
</template>
