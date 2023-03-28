<template>
  <div>
    <h2>관리자 삭제</h2>
    <form>
      <label>
        ID:<input type="text" v-model="admin_id">
      </label>
      <br>
      <button @click.prevent="deleteAdmin">삭제하기</button>
      <p style="color:red">{{message}}</p>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  name: "admin-delete",
  data() {
    return {
      admin_id: '',
      message: '',
    }
  },
  methods: {
    async deleteAdmin() {
      try {
        const cookieToken = Cookies.get('myToken'); // 쿠키에서 토큰을 가져옴
        if (!cookieToken) {
          this.message = '접근 권한이 없습니다.';
          return;
        }
        const response = await axios.delete(
          `${process.env.VUE_APP_BACKEND_URL}/admins/delete`,
          {
            data: {
              admin_id: this.admin_id,
            },
            headers: {
              'Token': `Bearer ${cookieToken}`,
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