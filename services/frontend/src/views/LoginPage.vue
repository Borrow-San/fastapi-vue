<template>
  <div class="login-page">
    <div class="form-wrapper">
      <router-link to="/"><img :src="imgUrl +'/bslogo.PNG'" style="width:80%;"></router-link><br>
      <h2>관리자 로그인</h2>
      <form>
        <div class="form-group">
          <label for="admin-id">아이디</label>
          <input type="text" id="admin-id" v-model="id" required>
        </div>
        <div class="form-group">
          <label for="password">비밀번호</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <div class="form-group">
          <button type="submit" @click.prevent="login">로그인</button>
        </div>
        <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  name: 'loginPage',
  data() {
    return {
      imgUrl: 'https://bucket-lqr64n.s3.ap-northeast-2.amazonaws.com',
      id: '',
      password: '',
      errorMessage: '',
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post(
          `${process.env.VUE_APP_BACKEND_URL}/admins/login`,
          {
            admin_id: this.id,
            password: this.password,
          },
          {
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': Cookies.get('csrftoken'),
            },
          },
        );

        if (response.status === 200) {
          console.log(response.data); // 로그인 결과 확인
          const token = response.data.msg; // JWT 토큰 값 가져오기
          const now = new Date();
          const expires = new Date(now.getTime() + 30 * 60 * 1000);
          Cookies.set('myToken', token, { expires: expires, secure: false, sameSite: 'strict' }); // 토큰을 쿠키에 저장 (30분간 유지)
          axios.defaults.headers.common['Authorization'] = `Bearer ${token}`; // 토큰을 header 에 저장
          this.$router.push('/admin'); // /admin 페이지로 이동
        } else {
          console.error(response);
          this.errorMessage = '아이디 또는 비밀번호가 잘못되었습니다.';
        }
      } catch (error) {
        console.error(error);
        this.errorMessage = '아이디 또는 비밀번호가 잘못되었습니다.';
      }
    },
  },
};
</script>

<style scoped>
.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f6f6f6;
}

.form-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 400px;
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
}

.form-group {
  display: flex;
  flex-direction: column;
  width: 100%;
  margin-bottom: 20px;
}

.form-group label {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 5px;
}

.form-group input[type="text"],
.form-group input[type="password"] {
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 100%;
}

.form-group button[type="submit"] {
  background-color: #007bff;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

.error-message {
  color: red;
  margin-top: 10px;
  font-size: 16px;
}
</style>