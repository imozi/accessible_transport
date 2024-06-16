<script setup lang="ts" generic="TData">
import { toTypedSchema } from '@vee-validate/zod';
import { string, object } from 'zod';
import { useToast } from '../ui/toast/use-toast';
import type { ModalProps } from '~/types';
import { genders, workTime } from '~/data';
import { DateFormatter, getLocalTimeZone, parseDate, today } from '@internationalized/date';
import { toDate } from 'radix-vue/date';
import { cn } from '@/lib/utils';

const config = useRuntimeConfig();
const { toast } = useToast();

const isLoading = ref<boolean>(false);
const open = ref(false);
const emit = defineEmits(['on:created']);
const placeholder = ref();

const df = new DateFormatter('ru-Ru', {
  dateStyle: 'short',
});

const value = computed({
  get: () => (values.work_day ? parseDate(values.work_day) : undefined),
  set: (val) => val,
});

const formSchema = toTypedSchema(
  object({
    first_name: string({ required_error: 'Поле не должно быть пустым' }).trim(),
    second_name: string({ required_error: 'Поле не должно быть пустым' }).trim(),
    patronymic: string({ required_error: 'Поле не должно быть пустым' }).trim(),
    gender: string({ required_error: 'Пол не выбран' }),
    personnel_number: string({ required_error: 'Поле не должно быть пустым' })
      .min(8, 'Должен быть 8 цифр')
      .max(8, 'Должен быть 8 цифр')
      .trim()
      .transform((value) => +value),
    phone: string({ required_error: 'Некорректный номер телефона' })
      .refine(
        (value) => {
          if ((value.startsWith('+7') && value.length < 16) || (value.startsWith('8') && value.length < 15)) {
            return false;
          }

          if (!value.length || value.length < 15) {
            return false;
          }

          return true;
        },
        { message: 'Некорректный номер телефона' },
      )
      .transform((value) => value.split(' ').slice(1).join('')),
    work_time: string({ required_error: 'Выберите время работы' }).trim(),
    work_day: string({ required_error: 'Выберите день работы' }).refine((v) => v, {
      message: 'Выберите дату поездки',
    }),
  }),
);

const maskPhone = reactive({
  mask: (value: string) => (value.startsWith('8') ? '8 ### ### ## ##' : '+7 ### ### ## ##'),
});

const { handleSubmit, setFieldValue, values } = useForm({
  validationSchema: formSchema,
});

const onSubmit = handleSubmit(async (values) => {
  isLoading.value = !isLoading.value;

  try {
    await $fetch(`${config.public.BACKEND}/employee/create`, { body: values, method: 'POST' });

    isLoading.value = false;
    open.value = !open.value;
    emit('on:created');

    toast({
      title: `Сотрудник: ${values.second_name} ${values.first_name[0]}.${values.patronymic[0]}`,
      description: 'Успешно создан!',
      variant: 'success',
    });
  } catch (error: unknown) {
    isLoading.value = false;
    if (error instanceof Error)
      toast({
        title: `Ошибка`,
        description: error.message,
        variant: 'destructive',
      });
  }
});

const modal: ModalProps = {
  props: {
    textTrigger: 'Новый сотрудник',
    title: 'Новый сотрудник',
    description: 'создание нового сотрудника',
    icon: 'ic:baseline-plus',
  },
};
</script>

<template>
  <Modal :props="modal.props" v-model:open="open">
    <form class="employees-form" method="post" @submit="onSubmit">
      <div class="employees-form__title">
        <h2>Сотрудник</h2>
      </div>
      <div class="employees-form__fields">
        <UiFormField v-slot="{ componentField }" name="second_name">
          <UiFormItem>
            <UiFormLabel>Фамилия</UiFormLabel>
            <UiFormControl>
              <UiInput type="text" v-bind="componentField" />
            </UiFormControl>
            <UiFormMessage />
          </UiFormItem>
        </UiFormField>

        <UiFormField v-slot="{ componentField }" name="phone">
          <UiFormItem>
            <UiFormLabel>Телефон</UiFormLabel>
            <UiFormControl>
              <UiInput type="text" v-bind="componentField" v-maska="maskPhone" />
            </UiFormControl>
            <UiFormMessage />
          </UiFormItem>
        </UiFormField>

        <UiFormField v-slot="{ componentField }" name="first_name">
          <UiFormItem>
            <UiFormLabel>Имя</UiFormLabel>
            <UiFormControl>
              <UiInput type="text" v-bind="componentField" />
            </UiFormControl>
            <UiFormMessage />
          </UiFormItem>
        </UiFormField>

        <UiFormField v-slot="{ componentField }" name="personnel_number">
          <UiFormItem>
            <UiFormLabel>Табельный номер</UiFormLabel>
            <UiFormControl>
              <UiInput type="text" v-bind="componentField" />
            </UiFormControl>
            <UiFormMessage />
          </UiFormItem>
        </UiFormField>

        <UiFormField v-slot="{ componentField }" name="patronymic">
          <UiFormItem>
            <UiFormLabel>Отчество</UiFormLabel>
            <UiFormControl>
              <UiInput type="text" v-bind="componentField" />
            </UiFormControl>
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

        <UiFormField v-slot="{ componentField }" name="gender">
          <UiFormItem>
            <UiFormLabel>Пол</UiFormLabel>
            <UiSelect v-bind="componentField">
              <UiFormControl>
                <UiSelectTrigger>
                  <SelectValue placeholder="Выберите пол" />
                </UiSelectTrigger>
              </UiFormControl>
              <UiSelectContent>
                <UiSelectGroup>
                  <UiSelectItem v-for="gender in genders" :key="gender.id" :value="`${gender.value}`"
                    >{{ gender.name }}
                  </UiSelectItem>
                </UiSelectGroup>
              </UiSelectContent>
            </UiSelect>
            <UiFormMessage />
          </UiFormItem>
        </UiFormField>

        <UiFormField name="work_day">
          <UiFormItem class="flex flex-col w-[360px]">
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
      </div>

      <UiDialogFooter class="mb-5">
        <UiDialogClose
          class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border bg-background hover:bg-accent h-10 px-4 py-2 text-[#3A76EE] hover:text-[#3A76EE] border-[#3976EE]"
          type="button"
        >
          Закрыть без сохранения
        </UiDialogClose>
        <UiButton v-auto-animate="{ duration: 150 }" class="passanger-form__submit" type="submit" :disabled="isLoading">
          <span v-if="!isLoading">Сохранить</span>
          <span v-else> <LucideLoader2 class="w-4 h-4 mr-2 animate-spin" /> Пожалуйста подождите </span>
        </UiButton>
      </UiDialogFooter>
    </form>
  </Modal>
</template>

<style lang="scss">
.employees-form {
  @apply w-full;

  &__title {
    @apply font-bold text-lg text-[#172F5F] mb-3;
  }

  &__fields {
    @apply grid grid-cols-2 gap-x-5 gap-y-5 mb-14;
  }

  & label {
    @apply text-[#8E8E8E] mb-1 block;

    & + button {
      @apply bg-[#F7F9FA] font-normal text-base;
    }
  }

  & input,
  textarea {
    @apply bg-[#F7F9FA] text-base;
  }

  &__submit {
    @apply min-w-60;

    & span {
      @apply flex items-center;
    }
  }
}
</style>
