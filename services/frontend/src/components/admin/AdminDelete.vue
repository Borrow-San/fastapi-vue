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
import authMixin from '@/mixins/authMixin';

export default {
  name: "admin-delete",
  mixins: [authMixin],
  data() {
    return {
      admin_id: '',
      message: '',
    }
  },
  methods: {
    async deleteAdmin() {
      try {
        if (!this.checkToken()) { // checkToken() 함수 호출
          return;
        }
        const response = await axios.delete(
          `${process.env.VUE_APP_BACKEND_URL}/admins/delete`,
          {
            data: {
              admin_id: this.admin_id,
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