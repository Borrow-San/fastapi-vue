<template>
  <div class="article-create">
    <h2>게시물 작성</h2>
    <form>
      <label>
        제목:<input type="text" v-model="title">
        <br>
        타입:
        <select v-model="type">
          <option value="">선택하세요</option>
          <option value="공지">공지</option>
          <option value="문의">문의</option>
          <option value="오류">오류</option>
          <option value="기타">기타</option>
        </select>
        <br>
        내용:<textarea v-model="text"></textarea>
        <br>
        첨부파일:<input type="file" ref="fileInput" @change="uploadFile">
        <div v-if="uploading">
          파일 업로드 중...
        </div>
        <div v-else-if="reference_url">
          업로드한 파일: {{ reference_url }}
        </div>
      </label>
    </form>
    <button @click.prevent="createArticle">작성하기</button>
  </div>
</template>

<script>
import authMixin from '@/mixins/authMixin';
import axios from 'axios';

export default {
  name: "article-create",
  mixins: [authMixin],
  data() {
    return {
      title: '',
      type: '',
      text: '',
      reference_url: '',
      uploading: false
    }
  },
  methods: {
    async uploadFile() {
      this.uploading = true;
      const formData = new FormData();
      formData.append('file', this.$refs.fileInput.files[0]);
      try {
        const response = await axios.post(
          `${process.env.VUE_APP_BACKEND_URL}/articles/uploadfile`,
          formData,
          {
            headers: {
              Authorization: `Bearer ${this.getToken()}`
            }
          }
        );
        this.reference_url = response.data.url;
        this.uploading = false;
      } catch (error) {
        console.error(error);
        this.uploading = false;
      }
    },
    async createArticle() {
      const payload = {
        title: this.title,
        type: this.type,
        text: this.text,
        reference_url: this.reference_url,
      };
      try {
        const response = await axios.post(
          `${process.env.VUE_APP_BACKEND_URL}/articles/register`,
          payload,
          {
            headers: {
              Authorization: `Bearer ${this.getToken()}`
            }
          }
        );
        console.log(response.data.msg);
        // 게시물 작성 완료 후 리다이렉트 등의 작업 수행
      } catch (error) {
        console.error(error);
      }
    },
  },
}
</script>

<style scoped>

</style>