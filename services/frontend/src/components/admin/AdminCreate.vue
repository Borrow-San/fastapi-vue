<template>
  <div class="admin-create">
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
import authMixin from '@/mixins/authMixin';

export default {
  name: "admin-create",
  mixins: [authMixin],
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
        if (!this.checkToken()) {
          return;
        }
        const response = await axios.post(
          `${process.env.VUE_APP_BACKEND_URL}/admins/register`,
          {
            admin_id: this.admin_id, // $route.params.admin_id 사용
            password: this.password,
            name: this.name,
          }
        );
        this.message = response.data.msg;
      } catch (error) {
        console.error(error);
        this.message = error.response.data.detail;
      }
    },
  }
}
</script>

<style scoped>

</style>