<template>
  <div class="article-create">
    <h2>게시물 작성</h2>
    <from>
      <label>
        제목:<input type="text" v-model="title">
      </label>
    </from>
  </div>
</template>

<script>
export default {
  name: "article-create",
  data() {
    return {
      title: '',
      type: '',
      text: '',
      reference_url: ''
    }
  },
  methods: {
    async createArticle() {
    }
  }
}
</script>

<style scoped>

</style>