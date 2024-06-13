<script setup lang="ts">
import type { ModalProps } from '~/types';

const { props } = defineProps<ModalProps>();
const open = defineModel<boolean>('open');
const emit = defineEmits(['update:open']);
const isSelected = inject<boolean>('isSelected');
</script>

<template>
  <UiDialog v-model:open="open">
    <UiDialogTrigger as-child>
      <UiButton :variant="props.variant ? props.variant : 'outline'"
        :class="`shadow-lg shadow-[#0D21390D] items-center gap-x-3 text-sm w-full max-w-60 ${props.variant ? '' : 'text-[#3A76EE] hover:text-[#3A76EE]'}`"
        :disabled="!isSelected && props.isDisable">
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
