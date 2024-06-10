<script setup lang="ts">

</script>

<template>
  <UiDialog>
    <UiDialogTrigger as-child>
      <UiButton variant="outline"
        class="shadow-lg shadow-[#0D21390D] text-[#3A76EE] items-center gap-x-3 text-sm w-full max-w-60 hover:text-[#3A76EE]">
        <Icon name="ic:baseline-plus" />
        Новая заявка
      </UiButton>
    </UiDialogTrigger>
    <UiDialogScrollContent class="sm:max-w-[800px]">
      <UiDialogHeader>
        <UiDialogTitle>Новая заявка</UiDialogTitle>
        <UiDialogDescription>создание новой заявки</UiDialogDescription>
      </UiDialogHeader>
      <div class="flex flex-col gap-y-8 p-8">
        <slot />
      </div>
    </UiDialogScrollContent>
  </UiDialog>
</template>