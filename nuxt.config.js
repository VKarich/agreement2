export default {
  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: 'Deelly.app',
    meta: [
      { charset: 'text/html; charset=UTF-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [
  ],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [
    { src: '~/plugins/vue-numeral-filter.js', ssr: false }
  ],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    '@nuxtjs/moment'
  ],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    '@nuxtjs/bulma',
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
    '@nuxt/content',
    'nuxt-buefy',
    '@nuxtjs/moment',
    [
      '@nuxtjs/yandex-metrika',
      {
        id: '76596280',
        webvisor: true,
        clickmap:true,
        // useCDN:false,
        trackLinks:true,
        accurateTrackBounce:true,
      }
    ],
  ],

  // Axios module configuration (https://go.nuxtjs.dev/config-axios)
  axios: {},

  // Content module configuration (https://go.nuxtjs.dev/config-content)
  content: {},

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {
    postcss: {
      preset: {
        features: {
          customProperties: false
        }
      }
    }
  }
}
