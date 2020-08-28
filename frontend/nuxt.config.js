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
    build: {
        postcss: {
            preset: {
                features: {
                    customProperties: false,
                }
            }
        }
    },
    fontawesome: {
        icons: {
            brands: true,
        }
    },
};
