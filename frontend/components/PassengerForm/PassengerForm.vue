<script setup lang="ts">
import { toTypedSchema } from '@vee-validate/zod';
import { string, object } from 'zod';
import { useToast } from '../ui/toast/use-toast';
import { genders } from '~/data';
import type { ModalProps } from '~/types';

const config = useRuntimeConfig();
const { toast } = useToast();
const { categories } = useStateCategories();
const formSchema = toTypedSchema(
  object({
    first_name: string({ required_error: 'Поле не должно быть пустым' }).trim(),
    second_name: string({ required_error: 'Поле не должно быть пустым' }).trim(),
    patronymic: string({ required_error: 'Поле не должно быть пустым' }).trim(),
    gender: string({ required_error: 'Пол не выбран' }),
    category: string({ required_error: 'Поле не должно быть пустым' })
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
  }),
);
const maskPhone = reactive({
  mask: (value: string) => (value.startsWith('8') ? '8 ### ### ## ##' : '+7 ### ### ## ##'),
});
const { handleSubmit } = useForm({
  validationSchema: formSchema,
});
const isLoading = ref<boolean>(false);
const open = ref(false);
const emit = defineEmits(['on:created'])

const onSubmit = handleSubmit(async (values) => {
  isLoading.value = true;

  try {
    await $fetch(`${config.public.BACKEND}/passenger/create`, { body: values, method: 'POST' });

    isLoading.value = false;
    open.value = !open.value;
    emit('on:created')

    toast({
      title: `Пассажир ${values.second_name} ${values.first_name[0]}.${values.patronymic[0]}`,
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
    textTrigger: 'Новый пассажир',
    title: 'Новый пассажир',
    description: 'создание нового пассажира',
    icon: 'ic:baseline-plus',
  },
};
</script>

<template>
  <Modal :props="modal.props" v-model:open="open">
    <form class="passanger-form" method="post" @submit="onSubmit">
      <div class="passanger-form__fields">
        <UiFormField v-slot="{ componentField }" name="second_name">
          <UiFormItem class="passanger-form__item">
            <UiFormLabel>Фамилия</UiFormLabel>
            <UiFormControl>
              <UiInput type="text" v-bind="componentField" />
            </UiFormControl>
            <UiFormMessage />
          </UiFormItem>
        </UiFormField>

        <UiFormField v-slot="{ componentField }" name="phone">
          <UiFormItem class="passanger-form__item">
            <UiFormLabel>Телефон</UiFormLabel>
            <UiFormControl>
              <UiInput type="text" v-bind="componentField" v-maska="maskPhone" />
            </UiFormControl>
            <UiFormMessage />
          </UiFormItem>
        </UiFormField>

        <UiFormField v-slot="{ componentField }" name="first_name">
          <UiFormItem class="passanger-form__item">
            <UiFormLabel>Имя</UiFormLabel>
            <UiFormControl>
              <UiInput type="text" v-bind="componentField" />
            </UiFormControl>
            <UiFormMessage />
          </UiFormItem>
        </UiFormField>

        <UiFormField v-slot="{ componentField }" name="category">
          <UiFormItem class="passanger-form__item">
            <UiFormLabel>Категория</UiFormLabel>
            <UiSelect v-bind="componentField">
              <UiFormControl>
                <UiSelectTrigger>
                  <SelectValue placeholder="Выберите категорию" />
                </UiSelectTrigger>
              </UiFormControl>
              <UiSelectContent>
                <UiSelectGroup>
                  <UiSelectItem v-for="category in categories" :key="category.id" :value="`${category.id}`"
                    >{{ category.code }}
                  </UiSelectItem>
                </UiSelectGroup>
              </UiSelectContent>
            </UiSelect>
            <UiFormMessage />
          </UiFormItem>
        </UiFormField>

        <UiFormField v-slot="{ componentField }" name="patronymic">
          <UiFormItem class="passanger-form__item">
            <UiFormLabel>Отчество</UiFormLabel>
            <UiFormControl>
              <UiInput type="text" v-bind="componentField" />
            </UiFormControl>
            <UiFormMessage />
          </UiFormItem>
        </UiFormField>

        <UiFormField v-slot="{ componentField }" name="is_pacemaker">
          <UiFormItem class="passanger-form__item">
            <UiFormLabel>Наличие ЭКС</UiFormLabel>
            <UiSelect v-bind="componentField">
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
          <UiFormItem class="passanger-form__item">
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
      </div>

      <UiFormField v-slot="{ componentField }" name="description">
        <UiFormItem class="passanger-form__item mb-10">
          <UiFormLabel>Комментарий</UiFormLabel>
          <UiFormControl>
            <UiTextarea placeholder="Введите комментарий" class="resize-none" v-bind="componentField" />
          </UiFormControl>
          <UiFormMessage />
        </UiFormItem>
      </UiFormField>

      <UiDialogFooter class="mb-5">
        <UiDialogClose
          class="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border bg-background hover:bg-accent h-10 px-4 py-2 text-[#3A76EE] hover:text-[#3A76EE] border-[#3976EE]"
          type="button"
        >
          Закрыть без сохранения
        </UiDialogClose>
        <UiButton v-auto-animate="{ duration: 150 }" class="passanger-form__submit" type="submit" :disabled="isLoading">
          <span v-if="!isLoading"> Сохранить </span>
          <span v-else> <LucideLoader2 class="w-4 h-4 mr-2 animate-spin" /> Пожалуйста подождите </span>
        </UiButton>
      </UiDialogFooter>
    </form>
  </Modal>
</template>

<style lang="scss">
.passanger-form {
  @apply w-full;

  &__fields {
    @apply grid grid-cols-2 gap-x-5 gap-y-5 mb-5;
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
