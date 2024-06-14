<template>
  <div class="loader-wrapper">
    <div class="loader"></div>
  </div>
</template>

<style lang="scss">
.loader-wrapper {
  @apply w-full h-full absolute z-50 bg-white/70;
}

.loader {
  position: absolute;
  width: 8px;
  height: 40px;
  border-radius: 4px;
  display: block;
  margin: 20px auto;
  background: currentColor;
  color: #112448;
  box-sizing: border-box;
  animation: animloader 0.3s 0.3s linear infinite alternate;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.loader::after,
.loader::before {
  content: '';
  width: 8px;
  height: 40px;
  border-radius: 4px;
  background: currentColor;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  left: 20px;
  box-sizing: border-box;
  animation: animloader 0.3s 0.45s linear infinite alternate;
}

.loader::before {
  left: -20px;
  animation-delay: 0s;
}

@keyframes animloader {
  0% {
    height: 48px;
  }

  100% {
    height: 4px;
  }
}
</style>
