const path = require('path');
const webpack = require('webpack');

module.exports = {
  resolve: {
    fallback: {
      "path": require.resolve("path-browserify"),
      "os": require.resolve("os-browserify/browser")
    }
  },
  node: {
    fs: 'empty'
  }
};