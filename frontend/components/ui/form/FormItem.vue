<script lang="ts" setup>
import { type HTMLAttributes, provide } from 'vue'
import { useId } from 'radix-vue'
import { FORM_ITEM_INJECTION_KEY } from './injectionKeys'
import { cn } from '@/lib/utils'

const props = defineProps<{
  class?: HTMLAttributes['class']
}>()

const id = useId()
provide(FORM_ITEM_INJECTION_KEY, id)
</script>

<template>
  <div :class="cn('', props.class)">
    <slot />
  </div>
</template>
