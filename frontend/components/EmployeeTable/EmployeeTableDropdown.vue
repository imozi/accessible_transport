<script setup lang="ts">
import type { Employee } from '~/types';
import { useToast } from '../ui/toast/use-toast';
import { toTypedSchema } from '@vee-validate/zod';
import { string, object } from 'zod';
import { DateFormatter, getLocalTimeZone, parseDate, today } from '@internationalized/date';
import { toDate } from 'radix-vue/date';
import { cn } from '@/lib/utils';
import { workTime } from '~/data';

defineProps<{
  employee: {
    id: number | string;
    work_day: string;
    work_time: string;
    full_name: string;
  };
}>();

const config = useRuntimeConfig();
const { toast } = useToast();
const isAction = inject<globalThis.Ref<boolean>>('isAction')
const isOpenPopover = ref<boolean>(false);
const isLoading = ref<boolean>(false);
const placeholder = ref();
const currentEmployee = {
  id: '',
  work_day: '',
  work_time: '',
  full_name: ''
}
const df = new DateFormatter('ru-Ru', {
  dateStyle: 'short',
});

const value = computed({
  get: () => (values.work_day ? parseDate(values.work_day) : undefined),
  set: (val) => val,
});

const formSchema = toTypedSchema(
  object({
    work_time: string({ required_error: 'Выберите время работы' }).trim(),
    work_day: string({ required_error: 'Выберите день работы' }).refine((v) => v, {
      message: 'Выберите день работы',
    }),
  }),
);

const { handleSubmit, setFieldValue, values } = useForm({
  validationSchema: formSchema,
});

const onSubmit = handleSubmit(async (values) => {

  if(currentEmployee.work_day === values.work_day && currentEmployee.work_time === values.work_time) {
    return
  }
  
  isLoading.value = !isLoading.value;

  try {
    await $fetch(`${config.public.BACKEND}/employee/edit/${currentEmployee.id}`, {
      body: values,
      method: 'PATCH',
    });

    isAction!.value = true;
    isLoading.value = !isLoading.value;
    isOpenPopover.value = false;

    toast({
      title: `Данные сотрудника ${currentEmployee.full_name}`,
      description: `Успешно изменены`,
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

const onDelete = async (id: string | number) => {
  try {
    const employee = await $fetch<Employee>(`${config.public.BACKEND}/employee/delete/${id}`, { method: 'DELETE' });
    isAction!.value = true;

    toast({
      title: `Сотрудник ${employee.second_name} ${employee.first_name[0]}. ${employee.patronymic[0]}`,
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

const onChangeWorkDayTime = (id: string | number, work_day:string, work_time: string, full_name:string) => {
  isOpenPopover.value = true;
  currentEmployee.id = `${id}`
  currentEmployee.work_day = work_day
  currentEmployee.work_time = work_time
  currentEmployee.full_name = full_name
  setFieldValue('work_time', `${work_time}`);
  setFieldValue('work_day', `${work_day}`);
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
      <UiDropdownMenuItem @click="onChangeWorkDayTime(employee.id, employee.work_day, employee.work_time, employee.full_name)">
        <LucidePencil class="mr-2 h-4 w-4" />
        <span>Изменить дату и время работы</span>
      </UiDropdownMenuItem>
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

  <UiDialog v-model:open="isOpenPopover">
    <UiDialogTrigger as-child></UiDialogTrigger>
    <UiDialogContent class="sm:max-w-[450px] p-0">
      <UiDialogHeader>
        <UiDialogTitle>Сотрудник {{ employee.full_name }}</UiDialogTitle>
        <UiDialogDescription>Изменить день и время работы</UiDialogDescription>
      </UiDialogHeader>
      <div class="grid gap-4 px-6 pb-4">
        <form class="status-form" method="post" @submit="onSubmit">
          <div class="status-form__fields">

            <UiFormField name="work_day">
          <UiFormItem class="flex flex-col w-full">
            <UiFormLabel>Дата работы</UiFormLabel>
            <UiPopover>
              <PopoverTrigger as-child>
                <UiFormControl>
                  <UiButton
                    variant="outline"
                    :class="cn('ps-3 text-start font-normal justify-normal', !value && 'text-muted-foreground')"
                  >
                    <span>{{ value ? df.format(toDate(value)) : 'Выберите дату работы' }}</span>
                    <Icon class="ml-auto" name="ion:calendar-outline" />
                  </UiButton>
                  <input hidden />
                </UiFormControl>
              </PopoverTrigger>
              <UiPopoverContent class="p-0">
                <UiCalendar
                  v-model:placeholder="placeholder"
                  v-model="value"
                  calendar-label="Дата"
                  locale="ru-RU"
                  initial-focus
                  :min-value="today(getLocalTimeZone())"
                  @update:model-value="
                    (v) => {
                      if (v) {
                        setFieldValue('work_day', v.toString());
                      } else {
                        setFieldValue('work_day', undefined);
                      }
                    }
                  "
                />
              </UiPopoverContent>
            </UiPopover>
            <UiFormMessage />
          </UiFormItem>
        </UiFormField>

        <UiFormField v-slot="{ componentField }" name="work_time">
          <UiFormItem>
            <UiFormLabel>Время работы</UiFormLabel>
            <UiSelect v-bind="componentField">
              <UiFormControl>
                <UiSelectTrigger>
                  <SelectValue placeholder="Выберите время работы" />
                </UiSelectTrigger>
              </UiFormControl>
              <UiSelectContent>
                <UiSelectGroup>
                  <UiSelectItem v-for="item in workTime" :key="item.id" :value="`${item.time}`"
                    >{{ item.time }}
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
