<script setup lang="ts">
import type { RequestApi } from '~/types';
import { useToast } from '../ui/toast/use-toast';
import { toTypedSchema } from '@vee-validate/zod';
import { string, object } from 'zod';

defineProps<{
  request: {
    id: number | string;
    status: string;
  };
}>();

const config = useRuntimeConfig();
const { toast } = useToast();
const { requestStatus, getStatusName, getStatusId } = useStateRequestStatus();
const isAction = inject<globalThis.Ref<boolean>>('isAction');
const isOpenPopover = ref<boolean>(false);
const isLoading = ref<boolean>(false);


const statusEmployee = ['Новая', 'Не подтверждена', 'В рассмотрении', 'Принята', 'Выявление', 'Лист ожидания', 'Отмена', 'Отказ', 'Не распределена', 'Назначена', 'Пассажир опаздывает', 'Инспектор опаздывает']

const filteredStatus = requestStatus.value.filter((item) => !statusEmployee.includes(item.status))

const currentRequest = {
  idRequest: '',
  status: 0,
};
const formSchema = toTypedSchema(
  object({
    status: string().transform((value) => +value),
  }),
);

const { handleSubmit, setFieldValue } = useForm({
  validationSchema: formSchema,
});

const onSubmit = handleSubmit(async (values) => {
  if (values.status === +currentRequest.status) {
    return;
  }

  isLoading.value = !isLoading.value;

  try {
    await $fetch<RequestApi>(`${config.public.BACKEND}/request/status/${currentRequest.idRequest}/change`, {
      body: { status: values.status },
      method: 'PATCH',
    });

    isAction!.value = true;
    isLoading.value = !isLoading.value;
    isOpenPopover.value = false;

    toast({
      title: `Статус заявки c id ${currentRequest.idRequest}`,
      description: `Успешно изменен на ${getStatusId(+values.status)?.status}`,
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
});

const onChangeStatus = (id: string | number, status: string) => {
  const statusId = getStatusName(status)?.id;
  isOpenPopover.value = true;
  currentRequest.idRequest = `${id}`;
  currentRequest.status = statusId!;
  setFieldValue('status', `${statusId}`);
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
      <UiDropdownMenuItem @click="onChangeStatus(request.id, request.status)">
        <LucidePencil class="mr-2 h-4 w-4" />
        <span>Изменить статус</span>
      </UiDropdownMenuItem>

    </UiDropdownMenuContent>
  </UiDropdownMenu>

  <UiDialog v-model:open="isOpenPopover">
    <UiDialogTrigger as-child></UiDialogTrigger>
    <UiDialogContent class="sm:max-w-[370px] p-0">
      <UiDialogHeader>
        <UiDialogTitle>Статус заявки {{ request.id }}</UiDialogTitle>
        <UiDialogDescription>Изменение статуса заявки</UiDialogDescription>
      </UiDialogHeader>
      <div class="grid gap-4 px-6 pb-4">
        <form class="status-form" method="post" @submit="onSubmit">
          <div class="status-form__fields">
            <UiFormField v-slot="{ componentField }" name="status">
              <UiFormItem>
                <UiFormLabel>Статус заявки</UiFormLabel>
                <UiSelect v-bind="componentField">
                  <UiFormControl>
                    <UiSelectTrigger>
                      <SelectValue placeholder="Выберите статус" />
                    </UiSelectTrigger>
                  </UiFormControl>
                  <UiSelectContent>
                    <UiSelectGroup>
                      <UiSelectItem v-for="status in filteredStatus" :key="status.id" :value="`${status.id}`"
                        >{{ status.status }}
                      </UiSelectItem>
                    </UiSelectGroup>
                  </UiSelectContent>
                </UiSelect>
                <UiFormMessage />
              </UiFormItem>
            </UiFormField>
          </div>
          <UiDialogFooter>
            <div class="flex gap-x-3">
              <UiDialogClose
                class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border bg-background hover:bg-accent h-10 px-4 py-2 text-[#3A76EE] hover:text-[#3A76EE] border-[#3976EE]"
                type="button"
              >
                Закрыть
              </UiDialogClose>
              <UiButton
                v-auto-animate="{ duration: 150 }"
                class="status-form__submit"
                type="submit"
                :disabled="isLoading"
              >
                <span v-if="!isLoading">Изменить</span>
                <span v-else> <LucideLoader2 class="w-4 h-4 mr-2 animate-spin" /> Изменения </span>
              </UiButton>
            </div>
          </UiDialogFooter>
        </form>
      </div>
    </UiDialogContent>
  </UiDialog>
</template>

<style lang="scss">
.status-form {
  @apply w-full;

  &__title {
    @apply font-bold text-lg text-[#172F5F] mb-3;
  }

  &__fields {
    @apply grid gap-y-5 mb-5;
  }

  & label {
    @apply text-[#8E8E8E] mb-1 block;

    & + button {
      @apply bg-[#F7F9FA] font-normal text-base;
    }
  }

  & input {
    @apply bg-[#F7F9FA] text-base;
  }

  &__submit {
    @apply min-w-40;

    & span {
      @apply flex items-center;
    }
  }
}
</style>
