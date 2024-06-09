<script setup lang="ts">

</script>

<template>
  <UiDialog>
    <UiDialogTrigger as-child>
      <UiButton variant="outline" class="shadow-lg shadow-[#0D21390D] text-[#3A76EE] items-center gap-x-3 text-sm w-full max-w-60 hover:text-[#3A76EE]">
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
        <p>
          This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling will move the modal as needed.
        </p>
        <hr>
        <p>
          This is some placeholder content to show the scrolling behavior for modals. Instead of repeating the text in the modal, we use an inline style to set a minimum height, thereby extending the length of the overall modal and demonstrating the overflow scrolling. When content becomes longer than the height of the viewport, scrolling will move the modal as needed.
        </p>
      </div>
      <UiDialogFooter  class="p-8">
        <UiDialogClose>
        <UiButton variant="outline" class="text-[#3A76EE] hover:text-[#3A76EE] border-[#3976EE]" type="button">
          Закрыть без сохранения
        </UiButton>
        </UiDialogClose>
        <UiButton type="submit">
          Сохранить
        </UiButton>
      </UiDialogFooter>
    </UiDialogScrollContent>
  </UiDialog>
</template>