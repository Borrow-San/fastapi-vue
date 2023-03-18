import { createApp } from 'vue'
import App from './App.vue'
import { router } from '@/router/index'
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:8000'

axios.interceptors.request.use(
  function (config) {
    config.headers.Authorization = `Bearer ${localStorage.getItem('accessToken')}`;
    return config;
  },
  function (error) {
    return Promise.reject(error);
  }
);

createApp(App).use(router).mount('#src')