// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  app: {
    rootId: "dashboard",
  },
  ssr: false,
  modules: [
    "@nuxt/eslint",
    "@nuxtjs/tailwindcss",
    "@formkit/auto-animate/nuxt",
    "@vee-validate/nuxt",
    "shadcn-nuxt",
    "radix-vue/nuxt",
    "nuxt-lucide-icons",
    "nuxt-icon",
    "nuxt-time",
  ],
  tailwindcss: {
    cssPath: "~/assets/scss/styles.scss",
  },
  shadcn: {
    prefix: "Ui",
  },
});
