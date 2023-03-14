const {defineConfig} = require('@vue/cli-service')

module.exports = defineConfig(
    {
        transpileDependencies: true,
        devServer: {
            host: '0.0.0.0',
            allowedHosts: ['phayeon.site'],
            proxy: {
                '^/api': {
                    target: 'http://phayeon.site:8000',
                    ws: true,
                    changeOrigin: true
                }
            },
            hot: true,
        }
    }
)
