export default {
    modules: [
        '@nuxtjs/sitemap',
        '@nuxtjs/redirect-module',
    ],
    mode: 'spa',
    target: 'static',
    redirect: [
        {
            from: '^/security.txt',
            to: '/.well-known/security.txt',
            statusCode: 301
        },
    ],
};
