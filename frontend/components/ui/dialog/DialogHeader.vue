<script setup lang="ts">
import type { HTMLAttributes } from 'vue'
import { cn } from '@/lib/utils'

const props = defineProps<{
  class?: HTMLAttributes['class']
}>()
</script>

<template>
  <div
    :class="cn('flex flex-col p-7 bg-[#C7DAFF] rounded-t-md gap-y-1.5 text-center sm:text-left', props.class)"
  >
    <slot />
  </div>
</template>
