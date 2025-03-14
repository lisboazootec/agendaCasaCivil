// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: {
    enabled: true,

    timeline: {
      enabled: true,
    },
  },

  modules: [
    '@nuxtjs/tailwindcss',
    '@nuxt/icon'
  ],

  css: [
    '@/assets/css/globals.css'
  ],

  // Configuração para evitar os warnings de componentes duplicados
  components: {
    dirs: [
      {
        path: '~/components/ui',
        pathPrefix: false,
        ignore: ['**/*/index.ts'] // Ignora os arquivos index.ts
      }
    ]
  },

  app: {
    head: {
      title: 'Sistema de Agendas',
      meta: [
        { name: 'description', content: 'Sistema para gerenciamento de agendas' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      ]
    }
  },

  runtimeConfig: {
    public: {
      apiBase: process.env.API_BASE || 'http://localhost:8000/api'
    }
  },

  compatibilityDate: '2025-03-13',
})