// https://nuxt.com/docs/api/configuration/nuxt-config
import { createResolver } from '@nuxt/kit';
import vuetify from 'vite-plugin-vuetify';

const { resolve } = createResolver(import.meta.url);

export default defineNuxtConfig({
  app: {
    head: {
      titleTemplate: '%s - Pokemans',
      title: 'Pokemans',
      htmlAttrs: {
        lang: 'en',
      },
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { hid: 'description', name: 'description', content: '' },
        { name: 'format-detection', content: 'telephone=no' },
      ],
      link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
    },
  },
  ssr: false,

  css: [
    'vuetify/lib/styles/main.sass',
    '@mdi/font/css/materialdesignicons.min.css',
  ],

  runtimeConfig: {
    public: {
      baseURL: process.env.BASE_URL || 'http://localhost:8000/',
    },
  },

  hooks: {
    'vite:extendConfig': (config) => {
      config.plugins.push(
        vuetify({
          styles: { configFile: resolve('./styles/settings.scss') },
        })
      );
    },
  },

  plugins: [],

  components: true,

  modules: ['@pinia/nuxt'],

  build: {
    transpile: ['vuetify'],
  },
});
