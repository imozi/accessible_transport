<script setup lang="ts" generic="TData">
import { toTypedSchema } from '@vee-validate/zod';
import { string, object } from 'zod';
import { useToast } from '../ui/toast/use-toast';
import type { ModalProps, Passenger } from '~/types';
import type { Table } from '@tanstack/vue-table';
import { genders, categories } from '~/data';

import { DateFormatter, getLocalTimeZone, parseDate, today } from '@internationalized/date'
import { toDate } from 'radix-vue/date'
import { cn } from '@/lib/utils'

const { toast } = useToast();

const selected = useSelectedRow();
const table = inject<Table<TData>>('table');
const isDisabled = ref<boolean>(false);
const isLoading = ref<boolean>(false);
const open = ref(false);
const placeholder = ref()

const df = new DateFormatter('ru-Ru', {
  dateStyle: 'long',
})

const value = computed({
  get: () => values.date ? parseDate(values.date) : undefined,
  set: val => val,
})

const formSchema = toTypedSchema(
  object({
    first_name: string({ required_error: 'Поле не должно быть пустым' }).trim(),
    second_name: string({ required_error: 'Поле не должно быть пустым' }).trim(),
    patronymic: string({ required_error: 'Поле не должно быть пустым' }).trim(),
    gender: string({ required_error: 'Пол не выбран' }),
    category: string({ required_error: 'Поле не должно быть пустым' }).trim(),
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
    is_pacemaker: string()
      .default('false')
      .transform((value) => Boolean(value)),
    description: string()
      .trim()
      .optional()
      .transform((value) => {
        if (value) {
          return value;
        } else {
          return null;
        }
      }),
    date: string().refine(v => v, { message: 'A date of birth is required.' }),
  }),
);

const maskPhone = reactive({
  mask: (value: string) => (value.startsWith('8') ? '8 ### ### ## ##' : '+7 ### ### ## ##'),
});

const { handleSubmit, setValues, setFieldValue, values } = useForm({
  validationSchema: formSchema,
});

const onSubmit = handleSubmit(async (values) => {
  isLoading.value = !isLoading.value;

  new Promise((res, rej) => {
    setTimeout(() => {
      res(console.log(values));
      isLoading.value = !isLoading.value;
      open.value = !open.value;
      selected.value.select = !selected.value.select;

      if (table) {
        const { rows } = table.getFilteredSelectedRowModel();

        rows.forEach((row) => row.toggleSelected());
      }

      toast({
        title: `Заявка на пассажира: ${values.second_name} ${values.first_name[0]}.${values.patronymic[0]}`,
        description: 'Успешно создана!',
        variant: 'success',
      });
    }, 1000);
  });
});

const modal: ModalProps = {
  props: {
    textTrigger: 'Новая заявка',
    title: 'Новая заявка',
    description: 'создание новой заявки',
    icon: 'ic:baseline-plus',
    variant: 'default',
    isDisable: true,
  },
};

const openModal = () => {
  if (!table) {
    return;
  }

  const { rows } = table.getFilteredSelectedRowModel();

  if (rows.length) {
    const { first_name, second_name, patronymic, category, phone, gender, is_pacemaker }: Passenger = rows[0]
      .original as Passenger;

    setValues({
      first_name,
      second_name,
      patronymic,
      phone,
      category: `${category}`,
      gender,
      is_pacemaker: `${is_pacemaker}`,
    });

    isDisabled.value = !isDisabled.value;
  }
};

onBeforeRouteLeave(() => {
  if (table) {
    const { rows } = table.getFilteredSelectedRowModel();

    rows.forEach((row) => row.toggleSelected());
  }
});
</script>

<template>
  <Modal :props="modal.props" @update:open="openModal" v-model:open="open">
    <form class="request-form" method="post" @submit="onSubmit">
      <div class="request-form__title">
        <h2>Пассажир</h2>
      </div>
      <div class="request-form__fields">
        <UiFormField v-slot="{ componentField }" name="second_name">
          <UiFormItem>
            <UiFormLabel>Фамилия</UiFormLabel>
            <UiFormControl>
              <UiInput type="text" v-bind="componentField" :disabled="isDisabled" />
            </UiFormControl>
            <UiFormMessage />
          </UiFormItem>
        </UiFormField>

        <UiFormField v-slot="{ componentField }" name="phone">
          <UiFormItem>
            <UiFormLabel>Телефон</UiFormLabel>
            <UiFormControl>
              <UiInput type="text" v-bind="componentField" v-maska="maskPhone" :disabled="isDisabled" />
            </UiFormControl>
            <UiFormMessage />
          </UiFormItem>
        </UiFormField>

        <UiFormField v-slot="{ componentField }" name="first_name">
          <UiFormItem>
            <UiFormLabel>Имя</UiFormLabel>
            <UiFormControl>
              <UiInput type="text" v-bind="componentField" :disabled="isDisabled" />
            </UiFormControl>
            <UiFormMessage />
          </UiFormItem>
        </UiFormField>

        <UiFormField v-slot="{ componentField }" name="category">
          <UiFormItem>
            <UiFormLabel>Категория</UiFormLabel>
            <UiSelect v-bind="componentField" :disabled="isDisabled">
              <UiFormControl>
                <UiSelectTrigger>
                  <SelectValue placeholder="Выберите категорию" />
                </UiSelectTrigger>
              </UiFormControl>
              <UiSelectContent>
                <UiSelectGroup>
                  <UiSelectItem v-for="category in categories" :key="category.id" :value="`${category.id}`">{{
                    category.code }}
                  </UiSelectItem>
                </UiSelectGroup>
              </UiSelectContent>
            </UiSelect>
            <UiFormMessage />
          </UiFormItem>
        </UiFormField>

        <UiFormField v-slot="{ componentField }" name="patronymic">
          <UiFormItem>
            <UiFormLabel>Отчество</UiFormLabel>
            <UiFormControl>
              <UiInput type="text" v-bind="componentField" :disabled="isDisabled" />
            </UiFormControl>
            <UiFormMessage />
          </UiFormItem>
        </UiFormField>

        <UiFormField v-slot="{ componentField }" name="is_pacemaker">
          <UiFormItem>
            <UiFormLabel>Наличие ЭКС</UiFormLabel>
            <UiSelect v-bind="componentField" :disabled="isDisabled">
              <UiFormControl>
                <UiSelectTrigger>
                  <SelectValue placeholder="Нет" />
                </UiSelectTrigger>
              </UiFormControl>
              <UiSelectContent>
                <UiSelectGroup>
                  <UiSelectItem value="false">Нет </UiSelectItem>

                  <UiSelectItem value="true">Да </UiSelectItem>
                </UiSelectGroup>
              </UiSelectContent>
            </UiSelect>
            <UiFormMessage />
          </UiFormItem>
        </UiFormField>

        <UiFormField v-slot="{ componentField }" name="gender">
          <UiFormItem>
            <UiFormLabel>Пол</UiFormLabel>
            <UiSelect v-bind="componentField" :disabled="isDisabled">
              <UiFormControl>
                <UiSelectTrigger>
                  <SelectValue placeholder="Выберите пол" />
                </UiSelectTrigger>
              </UiFormControl>
              <UiSelectContent>
                <UiSelectGroup>
                  <UiSelectItem v-for="gender in genders" :key="gender.id" :value="`${gender.value}`">{{ gender.name }}
                  </UiSelectItem>
                </UiSelectGroup>
              </UiSelectContent>
            </UiSelect>
            <UiFormMessage />
          </UiFormItem>
        </UiFormField>
      </div>

      <UiFormField v-slot="{ componentField }" name="description">
        <UiFormItem>
          <UiFormLabel>Комментарий</UiFormLabel>
          <UiFormControl>
            <UiTextarea placeholder="Введите комментарий" class="resize-none mb-7" v-bind="componentField" />
          </UiFormControl>
          <UiFormMessage />
        </UiFormItem>
      </UiFormField>

      <hr />

      <div class="request-form__trip pt-6">
        <div class="request-form__title">
          <h2>Поездка</h2>
        </div>

        <div class="request-form__trip-fields">
          <UiFormField name="date">
            <UiFormItem class="flex flex-col">
              <UiFormLabel>Дата</UiFormLabel>
              <UiPopover>
                <PopoverTrigger as-child>
                  <UiFormControl>
                    <UiButton variant="outline" :class="cn(
                      'ps-3 text-start font-normal justify-normal',
                      !value && 'text-muted-foreground',
                    )">
                      <span>{{ value ? df.format(toDate(value)) : "Выберите дату" }}</span>
                      <Icon class="ml-auto" name="ion:calendar-outline" />

                    </UiButton>
                    <input hidden>
                  </UiFormControl>
                </PopoverTrigger>
                <UiPopoverContent class="w-auto p-0">
                  <UiCalendar v-model:placeholder="placeholder" v-model="value" calendar-label="Дата" locale="ru-RU"
                    initial-focus :min-value="today(getLocalTimeZone())" @update:model-value="(v) => {
                      if (v) {
                        setFieldValue('date', v.toString())
                      }
                      else {
                        setFieldValue('date', undefined)
                      }

                    }" />
                </UiPopoverContent>
              </UiPopover>
              <UiFormMessage />
            </UiFormItem>
          </UiFormField>

        </div>
      </div>

      <UiDialogFooter class="mb-5">
        <UiDialogClose
          class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border bg-background hover:bg-accent h-10 px-4 py-2 text-[#3A76EE] hover:text-[#3A76EE] border-[#3976EE]"
          type="button">
          Закрыть без сохранения
        </UiDialogClose>
        <UiButton v-auto-animate="{ duration: 150 }" class="passanger-form__submit" type="submit" :disabled="isLoading">
          <span v-if="!isLoading"> Сохранить </span>
          <span v-else>
            <LucideLoader2 class="w-4 h-4 mr-2 animate-spin" /> Пожалуйста подождите
          </span>
        </UiButton>
      </UiDialogFooter>
    </form>
  </Modal>
</template>

<style lang="scss">
.request-form {
  @apply w-full;

  &__title {
    @apply font-bold text-lg text-[#172F5F] mb-3;
  }

  &__fields {
    @apply grid grid-cols-2 gap-x-5 gap-y-5 mb-5;
  }

  & label {
    @apply text-[#8E8E8E] mb-1 block;

    &+button {
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
