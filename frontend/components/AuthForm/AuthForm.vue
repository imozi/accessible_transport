<script setup lang="ts">
import { toTypedSchema } from '@vee-validate/zod'
import { string, object } from 'zod'


const formSchema = toTypedSchema(object({
  username: string({ required_error: 'Некорректный email' }).trim().email('Некорректный email'),
  password: string({ required_error: 'Поле не должно быть пустым' }).trim().min(1, 'Поле не должно быть пустым'),
}))

const { handleSubmit } = useForm({
  validationSchema: formSchema,
})
const isLoading = ref<boolean>(false)

const onSubmit = handleSubmit(async (values) => {

  isLoading.value = !isLoading.value

  new Promise((res, rej) => {
    setTimeout(() => {
      res(console.log(values))
      isLoading.value = !isLoading.value
    }, 3000);
  })

})
</script>

<template>
  <form class="auth-form" method="post" @submit="onSubmit">
    <UiFormField v-slot="{ componentField }" name="username">
      <UiFormItem v-auto-animate>
        <UiFormLabel>Email / short name</UiFormLabel>
        <UiFormControl>
          <UiInput type="email" placeholder="youremail@mail.ru / youremail" v-bind="componentField" />
        </UiFormControl>
        <UiFormMessage />
      </UiFormItem>
    </UiFormField>


    <UiFormField v-slot="{ componentField }" name="password">
      <UiFormItem v-auto-animate>
        <UiFormLabel>Пароль</UiFormLabel>
        <UiFormControl>
          <UiInput type="password" v-bind="componentField" />
        </UiFormControl>
        <UiFormMessage />
      </UiFormItem>
    </UiFormField>

    <UiButton v-auto-animate="{ duration: 150 }" class="auth-form__submit" type="submit" :disabled="isLoading">
      <span v-if="!isLoading">
        Войти
      </span>
      <span v-else>
        <LucideLoader2 class="w-4 h-4 mr-2 animate-spin" /> Пожалуйста подождите
      </span>
    </UiButton>
  </form>
</template>

<style lang="scss"> 
.auth-form {
  @apply w-full;


  &__submit {
    @apply w-full;

    & span {
      @apply flex items-center;
    }
  }
}
</style>