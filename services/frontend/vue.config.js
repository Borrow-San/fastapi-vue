const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    host: '0.0.0.0',
    allowedHosts: ["www.borrowsan.shop", "borrowsan.shop"],
    proxy: {
      '/api': {
        target: 'http://borrowsan.shop:8000',
        ws: true,
        changeOrigin: true
      }
    },
    hot: true
  }
})