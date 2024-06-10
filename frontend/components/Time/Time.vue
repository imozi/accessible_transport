<script setup lang="ts">
type DateTime = {
  time: number;
  interval: NodeJS.Timeout | null;
};

const datetime = reactive<DateTime>({
  time: Date.now(),
  interval: null,
});

onMounted(() => {
  datetime.interval = setInterval(() => {
    datetime.time = Date.now();
  }, 1000);
});

onUnmounted(() => {
  if (datetime.interval) {
    clearInterval(datetime.interval);
  }
});
</script>

<template>
  <NuxtTime class="time" :datetime="datetime.time" hour="numeric" minute="numeric" second="numeric" />
</template>

<style lang="scss">
.time {
  @apply text-2xl font-light;
}
</style>
