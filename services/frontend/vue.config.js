const {defineConfig} = require('@vue/cli-service')
const Dotenv = require('dotenv-webpack');

module.exports = {
  transpileDependencies: true,
  devServer: {
    host: '0.0.0.0',
    allowedHosts: [process.env.VUE_APP_DOMAIN],
    hot: true,
  },
  configureWebpack: {
    plugins: [
      new Dotenv()
    ]
  }
};