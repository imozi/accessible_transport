<script setup lang="ts">
import { toTypedSchema } from '@vee-validate/zod';
import { string, object } from 'zod';
import { useToast } from '../ui/toast';
import type { Employee } from '~/types';

const config = useRuntimeConfig();
const { toast } = useToast();
const { setUser } = useStateEmployee();
const admin = {
  login: 'admin',
  password: 'admin12345',
};

const formSchema = toTypedSchema(
  object({
    login: string({ required_error: 'Поле не должно быть пустым' }).trim().min(1, 'Поле не должно быть пустым').default('admin'),
    password: string({ required_error: 'Поле не должно быть пустым' }).trim().min(1, 'Поле не должно быть пустым').default('admin12345'),
  }),
);

const { handleSubmit } = useForm({
  validationSchema: formSchema,
});
const isLoading = ref<boolean>(false);

const onSubmit = handleSubmit(async (values) => {
  isLoading.value = !isLoading.value;

  if (values.login === 'admin') {
    try {
      await new Promise((res, rej) => {
        setTimeout(() => {
          if (values.password === admin.password) {
            res({ ok: true });
            setUser({ user: admin.login });
            isLoading.value = !isLoading.value;
            navigateTo('/requests');
          } else {
            rej({ ok: false });
          }
        }, 1000);
      });
    } catch (error) {
      isLoading.value = !isLoading.value;
      toast({
        title: 'Ошибка!',
        description: 'Неверный логин / табельный номер или пароль',
        variant: 'destructive',
      });
    }
  } else {
    const employees = await $fetch<Employee[]>(`${config.public.BACKEND}/employee/list`);
    const employee = employees.find((item) => item.personnel_number === +values.login);

    if (!employee) {
      isLoading.value = !isLoading.value;
      toast({
        title: 'Ошибка!',
        description: 'Неверный логин / табельный номер или пароль',
        variant: 'destructive',
      });
    } else {
      if (values.password === `${employee.personnel_number}`) {
        isLoading.value = !isLoading.value;
        setUser(employee);
        navigateTo(`/${employee.personnel_number}`);
      } else {
        isLoading.value = !isLoading.value;
        toast({
          title: 'Ошибка!',
          description: 'Неверный логин / табельный номер или пароль',
          variant: 'destructive',
        });
      }
    }
  }
});
</script>

<template>
  <form class="auth-form" method="post" @submit="onSubmit">
    <div class="auth-form__title">
      <h2>Вход в систему</h2>
      <div class="auth-form__description">
        <p>мониторинга и распределения заявок от маломобильных пассажиров</p>
      </div>
    </div>

    <div class="auth-form__fields">
      <UiFormField v-slot="{ componentField }" name="login">
        <UiFormItem class="auth-form__item" v-auto-animate>
          <UiFormLabel>Логин или табельный номер</UiFormLabel>
          <UiFormControl>
            <UiInput class="auth-form__input" type="text" v-bind="componentField" />
          </UiFormControl>
          <UiFormMessage />
        </UiFormItem>
      </UiFormField>

      <UiFormField v-slot="{ componentField }" name="password">
        <UiFormItem class="auth-form__item" v-auto-animate>
          <UiFormLabel>Пароль</UiFormLabel>
          <UiFormControl>
            <UiInput class="auth-form__input" type="password" v-bind="componentField" />
          </UiFormControl>
          <UiFormMessage />
        </UiFormItem>
      </UiFormField>
    </div>
    <UiButton v-auto-animate="{ duration: 150 }" class="auth-form__submit" type="submit" :disabled="isLoading">
      <span v-if="!isLoading"> Войти </span>
      <span v-else>
        <LucideLoader2 class="w-4 h-4 mr-2 animate-spin" /> Пожалуйста подождите
      </span>
    </UiButton>
  </form>

  <div class="accounts text-muted-foreground text-sm p-4 bg-slate-50 rounded-md">
    
    <div class="accounts__row">
      <p><b>Зайти под администратором:</b></p>
      <div class="">
      <p>Логин: <b>admin</b></p>
      <p>Пароль: <b>admin12345</b></p>
    </div>
    </div>
    <div class="accounts__row">
      <p><b>Зайти под сотрудником если есть в базе:</b></p>
      <div class="">
      <p>Табельный номер любого сотрудника: <b>11998121</b></p>
      <p>Пароль совпадает с табельным номером: <b>11998121</b></p>
    </div>
    </div>
  </div>
</template>

<style lang="scss">
.auth-form {
  @apply w-full font-light flex flex-col gap-y-8 m-auto items-center;

  &__title {
    @apply scroll-m-20 text-2xl font-semibold tracking-tight text-center;
  }

  &__description {
    @apply font-normal text-sm text-muted-foreground;
  }

  &__fields {
    @apply flex flex-col gap-y-3 text-muted-foreground w-full max-w-[350px];
  }

  &__item {
    @apply flex flex-col gap-1;
  }

  &__input {
    @apply text-base font-normal text-black;
  }

  &__submit {
    @apply w-full max-w-[350px];

    & span {
      @apply flex items-center;
    }
  }
}

.accounts {
  @apply absolute left-5 top-5 flex flex-col gap-y-2;

  &__row {
    @apply flex flex-col gap-y-1;
  }
}
</style>
