<template>
  <div>
    <h2>관리자 생성</h2>
    <form>
      <label>
        이름:<input type="text" v-model="name">
      </label>
      <br>
      <label>
        비밀번호:<input type="password" v-model="password">
      </label>
      <br>
      <button @click.prevent="signup">생성하기</button>
      <p style="color:red">{{message}}</p>
    </form>
  </div>
</template>


<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  name: "admin-create",
  data() {
    return {
      password: '',
      name: '',
      message: '',
    }
  },
  methods: {
    async signup() {
      try {
        const cookieToken = Cookies.get('myToken'); // 쿠키에서 토큰을 가져옴
        if (!cookieToken) {
          this.message = '접근 권한이 없습니다.';
          return;
        }
        const response = await axios.post(
          `${process.env.VUE_APP_BACKEND_URL}/admins/register`,
          {
            admin_id: this.admin_id,
            password: this.password,
            name: this.name,
          },
          {
            headers: {
              'Token': `Bearer ${cookieToken}`, // 쿠키에 저장된 토큰을 헤더에 담기
              'Accept': 'application/json; charset=utf-8',
              'Content-Type': 'application/json; charset=utf-8'
            },
          },
        );
        this.message = response.data.msg;
      } catch (error) {
        console.error(error);
        this.message = error.response.data.detail;
      }
    }
  }
}
</script>

<style scoped>

</style>