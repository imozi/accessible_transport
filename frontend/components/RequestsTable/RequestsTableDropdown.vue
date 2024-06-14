<script setup lang="ts">
import type { RequestApi } from '~/types';
import { useToast } from '../ui/toast/use-toast';
import { DateFormatter } from '@internationalized/date';
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
let idRequest = '';
const formSchema = toTypedSchema(
  object({
    status: string().transform((value) => +value),
  }),
);

const { handleSubmit, setFieldValue } = useForm({
  validationSchema: formSchema,
});

const onSubmit = handleSubmit(async (values) => {
  isLoading.value = !isLoading.value;

  try {
    await $fetch<RequestApi>(`${config.public.BACKEND}/request/status/${idRequest}/change`, {
      body: { status: values.status },
      method: 'PATCH',
    });

    isAction!.value = true;
    isLoading.value = !isLoading.value;
    isOpenPopover.value = false;

    toast({
      title: `Статус заявки c id ${idRequest}`,
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

  // new Promise((res, rej) => {
  //   setTimeout(() => {

  //     res(console.log(values))
  //     isLoading.value = !isLoading.value;
  //     isOpenPopover.value = false;

  //     toast({
  //       title: `Статус заявки c id ${idRequest}`,
  //       description: `Успешно изменен на ${getStatusId(+values.status)?.status}`,
  //       variant: 'success',
  //     });

  //     idRequest = ''

  //   }, 1000);
  // })
});

const onDelete = async (id: string | number) => {
  try {
    const request = await $fetch<RequestApi>(`${config.public.BACKEND}/request/delete/${id}`, { method: 'DELETE' });
    isAction!.value = true;

    const formatDate = new DateFormatter('ru-Ru', {
      dateStyle: 'short',
    }).format(new Date(request.date));

    toast({
      title: `Заявка c id: ${id} на ${formatDate}`,
      description: 'Успешно удалена',
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

const onChangeStatus = (id: string | number, status: string) => {
  const statusId = getStatusName(status)?.id;
  isOpenPopover.value = true;
  idRequest = `${id}`;
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

      <UiDropdownMenuSeparator />
      <UiDropdownMenuItem @click="onDelete(request.id)">
        <LucideDelete class="mr-2 h-4 w-4" />
        <span>Удалить</span>
      </UiDropdownMenuItem>
    </UiDropdownMenuContent>
  </UiDropdownMenu>

  <UiPopover :open="isOpenPopover">
    <UiPopoverTrigger as-child>
      <div class="relative left-[-100px]"></div>
    </UiPopoverTrigger>
    <UiPopoverContent class="w-50">
      <div class="p-2">
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
                      <UiSelectItem v-for="status in requestStatus" :key="status.id" :value="`${status.id}`"
                        >{{ status.status }}
                      </UiSelectItem>
                    </UiSelectGroup>
                  </UiSelectContent>
                </UiSelect>
                <UiFormMessage />
              </UiFormItem>
            </UiFormField>
            <div class="flex gap-x-3">
              <UiButton variant="ghost" class="status-form__cancel" type="button">Закрыть </UiButton>
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
          </div>
        </form>
      </div>
    </UiPopoverContent>
  </UiPopover>
</template>

<style lang="scss">
.status-form {
  @apply w-full;

  &__title {
    @apply font-bold text-lg text-[#172F5F] mb-3;
  }

  &__fields {
    @apply grid gap-y-5;
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
