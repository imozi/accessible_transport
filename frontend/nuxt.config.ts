// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  app: {
    rootId: 'dashboard',
  },
  runtimeConfig: {
    public: {
      BACKEND: process.env.BASE_URL_BACKEND
    }
  },
  ssr: false,
  modules: [
    '@nuxt/eslint',
    '@nuxtjs/tailwindcss',
    '@formkit/auto-animate/nuxt',
    '@vee-validate/nuxt',
    'shadcn-nuxt',
    'radix-vue/nuxt',
    'nuxt-lucide-icons',
    'nuxt-icon',
    'nuxt-time',
  ],
  tailwindcss: {
    cssPath: '~/assets/scss/styles.scss',
  },
  shadcn: {
    prefix: 'Ui',
  },
});
