<script setup lang="ts">
type ModalProps = {
  props: {
    textTrigger: string;
    title: string;
    description?: string;
    icon?: string;
  };
};

const { props } = defineProps<ModalProps>();
const open = defineModel<boolean>('open');
const emit = defineEmits(['update:open']);

const openModal = (value: boolean) => {
  if (value) {
    emit('update:open');
  }
};
</script>

<template>
  <UiDialog @update:open="openModal" v-model:open="open">
    <UiDialogTrigger as-child>
      <UiButton
        variant="outline"
        class="shadow-lg shadow-[#0D21390D] text-[#3A76EE] items-center gap-x-3 text-sm w-full max-w-60 hover:text-[#3A76EE]"
      >
        <Icon v-if="props.icon" :name="props.icon" />
        {{ props.textTrigger }}
      </UiButton>
    </UiDialogTrigger>
    <UiDialogScrollContent class="sm:max-w-[800px]">
      <UiDialogHeader>
        <UiDialogTitle>{{ props.title }}</UiDialogTitle>
        <UiDialogDescription>{{ props.description }}</UiDialogDescription>
      </UiDialogHeader>
      <div class="flex flex-col gap-y-8 p-8">
        <slot />
      </div>
    </UiDialogScrollContent>
  </UiDialog>
</template>
