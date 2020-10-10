export default {
  modules: [
    '@nuxtjs/sitemap',
    '@nuxtjs/redirect-module',
    '@nuxtjs/bulma',
    '@nuxtjs/fontawesome',
  ],
  mode: 'spa',
  target: 'static',
  redirect: [
    {
      from: '^/security.txt',
      to: '/.well-known/security.txt',
      statusCode: 301,
    },
  ],
  css: [
    "~layouts/global.css",
  ],
  fontawesome: {
    component: 'fa',
    icons: {
      solid: [
        'faBalanceScale',
        'faHeart',
        'faLock',
        'faHome',
        'faAddressCard',
        'faFileAlt',
        'faUserShield',
        'faGamepad',
        'faBug',
        'faPaintBrush',
      ],
      brands: [
        'faGithub',
        'faDiscord',
      ],
    }
  },
  build: {
    postcss: {
      preset: {
        features: {
          customProperties: false,
        }
      }
    }
  },
  buildModules: ['@nuxt/typescript-build'],
};
