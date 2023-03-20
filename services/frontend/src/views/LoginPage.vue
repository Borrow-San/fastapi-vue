<template>
  <div class="loginPage">
    <router-link to="/"><img :src="imgUrl +'/bslogo.PNG'" style="width:80%;"></router-link><br>
    아이디: <input class="id"/><br>
    비밀번호: <input class="password"/><br>
    <router-link to="/admin">아이디/비밀번호 찾기</router-link>
    <router-link to="/admin">로그인</router-link>
  </div>
</template>

<script>
export default {
  name: 'loginPage',
  data(){
    return {
      imgUrl: "https://bucket-lqr64n.s3.ap-northeast-2.amazonaws.com"
    }
  }
}
</script>

<style>
.loginPage {
  width: 40%;
  margin: 0 auto;
  padding: 2%;
  background-color: #f5f5f5;
  box-shadow: 0 0 10px rgba(0,0,0,0.3);
  border-radius: 5px;
  font-family: Arial, sans-serif;
  text-align: center;
}

.loginPage a {
  text-decoration: none;
  color: #444;
}

.loginPage a:hover {
  color: #666;
}

.loginPage input {
  padding: 2%;
  margin-bottom: 2%;
  margin-top: 3%;
  width: 95%;
  border: none;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(0,0,0,0.3);
}

.loginPage input:focus {
  outline: none;
  box-shadow: 0 0 5px rgba(0,0,255,0.5);
}

.loginPage .id {
  margin-top: 20px;
}

.loginPage .password {
  margin-bottom: 20px;
}

.loginPage button {
  background-color: #3498db;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.loginPage button:hover {
  background-color: #2980b9;
}
</style>