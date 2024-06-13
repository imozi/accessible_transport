<script setup lang="ts">
import { useToast } from '../ui/toast/use-toast';

defineProps<{
  passenger: {
    id: number | string;
  };
}>();

const config = useRuntimeConfig();
const { toast } = useToast();

const isDelete = inject<globalThis.Ref<boolean>>('isDelete')

const onDelete = async (id: string | number) => {
  try {
    await $fetch(`${config.public.BACKEND}/passenger/delete/${id}`, { method: 'DELETE' });
    isDelete!.value = true;

    toast({
      title: `Пассажир`,
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
        <LucidePencil class="mr-2 h-4 w-4" />
        <span>Редактировать</span>
      </UiDropdownMenuItem>
      <UiDropdownMenuSeparator />
      <UiDropdownMenuItem @click="onDelete(passenger.id)">
        <LucideDelete class="mr-2 h-4 w-4" />
        <span>Удалить</span>
      </UiDropdownMenuItem>
    </UiDropdownMenuContent>
  </UiDropdownMenu>
</template>
