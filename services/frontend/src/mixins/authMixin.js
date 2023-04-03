import axios from 'axios';
import Cookies from 'js-cookie';

axios.interceptors.request.use(
  (config) => {
    const token = Cookies.get('myToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default {
  methods: {
    checkToken() {
      const cookieToken = Cookies.get('myToken');
      if (!cookieToken) {
        this.$data.message = '접근 권한이 없습니다.';
        window.alert(this.$data.message); // 알림 창 띄우기
        this.$router.push('/login'); // 로그인 페이지로 이동
        return false;
      }
      return true;
    },
    getToken() {
      return Cookies.get('myToken');
    },
  },
};