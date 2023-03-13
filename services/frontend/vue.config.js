const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    host: '0.0.0.0',
    allowedHosts: ['phayeon.site', '3.35.189.127'],
    proxy: {
      '^/api': {
        target: 'http://phayeon.site:8000',
        ws: true,
        changeOrigin: true
      }
    },
    hot: true
  }
})