export default {
  modules: [
    '@nuxtjs/fontawesome',

    /* Used for boring standard HTTP stuff. */

    '@nuxtjs/redirect-module',
    '@nuxtjs/sitemap',

    /* Used to modify Bulma's colour palette. */

    '@nuxtjs/style-resources',
  ],
  ssr: false,
  target: 'static',
  head: {
    title: 'Memeforming',
    meta: [
      {
        charset: 'utf-8',
      },
      {
        name: 'viewport',
        content: 'width=device-width, initial-scale=1',
      },
    ],
  },
  redirect: [
    {
      from: '^/security.txt',
      to: '/.well-known/security.txt',
      statusCode: 301,
    },
  ],
  css: [
    "~assets/scss/main.scss",
  ],
  styleResources: {
    /* Allows global use of .scss files. */

    scss: [
      '~assets/scss/main.scss'
    ],
  },
  fontawesome: {
    component: 'fa',
    icons: {
      solid: [
        /* Footer. */

        'faFileAlt',
        'faUserShield',
        'faHeart',

        /* Light or dark mode. */

        'faLightbulb',
        'faMoon',
      ],
      brands: [
        'faChrome',
        'faGithub',
        'faApple',
        'faGoogle',
        'faSteam',
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
  buildModules: [
    /* Allow TypeScript building/sources. */

    '@nuxt/typescript-build',

    /* Support dark mode and adaptive colours. */

    '@nuxtjs/color-mode',
  ],
};
