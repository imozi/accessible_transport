<script setup lang="ts">
import type { HTMLAttributes } from 'vue'
import { cn } from '@/lib/utils'

const props = defineProps<{ class?: HTMLAttributes['class'] }>()
</script>

<template>
  <div
    :class="
      cn(
        'flex gap-x-5 justify-end',
        props.class,
      )
    "
  >
    <slot />
  </div>
</template>
