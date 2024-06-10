<script setup lang="ts">
import { toTypedSchema } from '@vee-validate/zod';
import { string, object } from 'zod';

const formSchema = toTypedSchema(
  object({
    first_name: string().min(0).trim().optional(),
    second_name: string().min(0).trim().optional(),
    patronymic: string().min(0).trim().optional(),
    genders: string().min(0).trim().optional(),
    description: string().min(0).trim().optional(),
  }),
);

const { handleSubmit } = useForm({
  validationSchema: formSchema,
});
const isLoading = ref<boolean>(false);

const onSubmit = handleSubmit(async (values) => {
  isLoading.value = !isLoading.value;

  new Promise((res, rej) => {
    setTimeout(() => {
      res(console.log(values));
      isLoading.value = !isLoading.value;
    }, 3000);
  });
});
</script>

<template>
  <form class="request-form" method="post" @submit="onSubmit">
    <UiFormField v-slot="{ componentField }" name="first_name">
      <UiFormItem v-auto-animate>
        <UiFormLabel>Фамилия</UiFormLabel>
        <UiFormControl>
          <UiInput type="text" v-bind="componentField" />
        </UiFormControl>
        <UiFormMessage />
      </UiFormItem>
    </UiFormField>

    <UiFormField v-slot="{ componentField }" name="second_name">
      <UiFormItem v-auto-animate>
        <UiFormLabel>Имя</UiFormLabel>
        <UiFormControl>
          <UiInput type="text" v-bind="componentField" />
        </UiFormControl>
        <UiFormMessage />
      </UiFormItem>
    </UiFormField>

    <UiFormField v-slot="{ componentField }" name="patronymic">
      <UiFormItem v-auto-animate>
        <UiFormLabel>Отчество</UiFormLabel>
        <UiFormControl>
          <UiInput type="text" v-bind="componentField" />
        </UiFormControl>
        <UiFormMessage />
      </UiFormItem>
    </UiFormField>

    <UiDialogFooter class="p-8">
      <UiDialogClose>
        <UiButton variant="outline" class="text-[#3A76EE] hover:text-[#3A76EE] border-[#3976EE]" type="button">
          Закрыть без сохранения
        </UiButton>
      </UiDialogClose>
      <UiButton v-auto-animate="{ duration: 150 }" class="request-form__submit" type="submit" :disabled="isLoading">
        <span v-if="!isLoading"> Сохранить </span>
        <span v-else> <LucideLoader2 class="w-4 h-4 mr-2 animate-spin" /> Пожалуйста подождите </span>
      </UiButton>
    </UiDialogFooter>
  </form>
</template>

<style lang="scss">
.request-form {
  @apply w-full;

  &__submit {
    @apply w-full;

    & span {
      @apply flex items-center;
    }
  }
}
</style>
