<template>
  <header>
    <nav class="header">
      <a href="#" class="nav-item"><img :src="imgUrl +'/bslogo.PNG'" class="logo"></a>
      <div>
        <a href="#" class="nav-item">서비스 소개</a>
        <a href="#" class="nav-item">이용방법</a>
        <a href="" class="nav-item">|</a>
        <router-link to="/login" class="nav-item">Log in</router-link>
      </div>
      <div class="sub-menu">
        <a href="https://github.com/Borrow-San"><img :src="imgUrl +'/git.png'" class="icon"></a>
        <a href="https://borrow-san.atlassian.net/wiki/home"><img :src="imgUrl +'/confluence.png'" class="icon"></a>
        <a href="https://velog.io/@boost_dev/series/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8"><img :src="imgUrl + '/veloglogo.jpeg'" class="icon"></a>
      </div>
    </nav>
  </header>
  <body>
    <a href="#" class="chatbot" v-if="chatbotButton == false"><img :src="imgUrl +'/chatbot.png'" @click="chatBg"  class="chatbot"></a>
    <div v-if="chatbotButton == true">
<<<<<<< HEAD
      <div class="chatBgWhite">
        <div class="chat-item" style="height:15%; padding-botton:3px;">
          <td><h5 class="modal-title">챗봇</h5></td>
          <td>
            <button type="button" @click="chatBg" style="display: flex; align-items:flex-end;">
              <span>x</span>
            </button>
          </td>
        </div>
        <div class="chat-body">
          {{ result }}
        </div>
        <tr class="chat-input" style="border: 100px green solid;">
          <td>
            <input type="text" v-model="inputData" style="width: 90%;">
          </td>
          <td>
            <button style="width: 50px;" @click="sendRequest">전송</button>
          </td>
        </tr>
      </div>
=======
      <Chatbot/>
>>>>>>> 7c5949420da77f392dc546ea9c286700d8d58b51
    </div>

    <main name="landing1">
      <div class="main-container-img" :style="{ 'background-image': 'url(' + imgUrl + '/detectimg.png)' }">
        <div class="head">
          <div class="head-f">
            Borrow-San
          </div>
        </div>
        <div class="sub-head" style="font-size: 2.5vw; color:black;">
          "인공지능을 활용한 효율적인 자원 관리를 위한 공유경제 서비스 자동화"
        </div>
        <div class="button-area">
          <button class="button-style"  :style="{ 'background-image': 'url(' + imgUrl + '/googleplay.png)' }"></button>
        </div>
      </div>
    </main>
    <main2 name="landing2">
<<<<<<< HEAD
      <div style="float: left; width: 50%; height:10%;">
=======
      <div class="main-container" style="float: left; width: 50%; height:10%;">
>>>>>>> 7c5949420da77f392dc546ea9c286700d8d58b51
        <div class="head2" >
          <div style="text-align:left;">바로우산?<button @click="scrollImg(), changeImg()">제공 서비스 확인</button></div>
          <tr style="width:100%;">
              <div class="sub-head2" @click="scrollImg(), changeImg()"  style="float: left; font-size: 1.5vw; color:green;">{{ai}}</div>
              <div class="head-l" style="float: left; font-size: 1.5vw; margin-right:5px;"> 이용한 공유경제 자동화 서비스</div>
          </tr>
        </div>
      </div>
<<<<<<< HEAD
      <div style="float: left; width: 50%; height:70vh;">
        <img :src="images[imageIndex]" style="width:100%; height:100%;">
=======
      <div style="float: left; width: 50%; height:10%;">
        <img :src="imgUrl +'/umb.jpg'" style="width:100%; height:100%;">
>>>>>>> 7c5949420da77f392dc546ea9c286700d8d58b51
      </div>
    </main2>
    <main name="landing3" style="flex-direction: column;">
      <tr style="font-size: 4vw; color:black; font-weight:bold;">개발참가자</tr>
      <tr style="display:flex; justify-content: space-around; width:100%;">
        <td>
          <div id="app" style="float: left; width: 33%;">
            <div class="card-row">
              <div class="card">
                <img class="card-image" :src="imgUrl +'/devsb.jpg'">
                <div class="card-footer">
                  <p class="card-text" style="font-size:20px; font-weight:bold; text-align:left;">박성배</p>
                  <a href="https://github.com/Seongbae103" class="footer-items" style="color:black;"><img :src="imgUrl +'/git.png'" alt="" class="icon" style="float: left;"></a>
                  <a href="https://velog.io/@boost_dev" class="footer-items" style="color:black;"><img :src="imgUrl + '/veloglogo.jpeg'" alt="" class="icon" style="float: left;"></a>
                </div>
              </div>
            </div>
          </div>
          <div id="app" style="float: left; width: 33%;">
            <div class="card-row">
              <div class="card">
                <img class="card-image" :src="imgUrl +'/devhy.jpg'">
                <div class="card-footer">
                  <p class="card-text" style="font-size:20px; font-weight:bold; text-align:left;">박하연</p>
                  <a href="https://github.com/phayeon" class="footer-items" style="color:black;"><img :src="imgUrl +'/git.png'" alt="" class="icon" style="float: left;"></a>
                </div>
              </div>
            </div>
          </div>
          <div id="app" style="float: left; width: 33%;">
            <div class="card-row">
              <div class="card">
                <img class="card-image" :src="imgUrl +'/devgs.png'">
                <div class="card-footer">
                  <p class="card-text" style="font-size:20px; font-weight:bold; text-align:left;">이강산</p>
                  <a href="https://github.com/gangsanlee2" class="footer-items" style="color:black;"><img :src="imgUrl +'/git.png'" alt="" class="icon" style="float: left;"></a>
                </div>
              </div>
            </div>
          </div>
        </td>
      </tr>

    </main>
  </body>
  <footer name="landing4" style="width:100%;">
    <div class="footer-container">
      <div class="footer-menu">
        <div class="first-box">
          <img :src="imgUrl + '/footerlogo.PNG'" class="logo">
          <div class="column">
            <div class="footer-title">박성배</div>
              <a href="https://github.com/Seongbae103" class="footer-items">Github</a>
              <a href="https://velog.io/@boost_dev" class="footer-items">Velog</a>
          </div>
          <div class="column">
            <div class="footer-title">박하연</div>
              <a href="https://github.com/phayeon" class="footer-items">github</a>
          </div>
          <div class="column">
            <div class="footer-title">이강산</div>
              <a href="https://github.com/gangsanlee2" class="footer-items">github</a>
              <a href="" class="footer-items"></a>
              <a href="" class="footer-items"></a>
          </div>
        </div>
      </div>
      <div class="footer-middle"><i class="fa-solid fa-earth-africa" style="padding-right:2vw;">Borrow-San</i></div>
      <div class="footer-end">
        <div>
          <a href="https://borrow-san.atlassian.net/wiki/home" class="footer-end-item">Team Confluence</a>
          <a href="https://github.com/Borrow-San" class="footer-end-item">Team Github</a>
          <a href="https://velog.io/@boost_dev/series/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8" class="footer-end-item">Learning records</a>
        </div>
        <div style="padding-right:2vw;" >2022.11 - 2023.03 </div>
      </div>
    </div>
  </footer>


</template>

<script>
<<<<<<< HEAD
import axios from 'axios';
=======
import ChatbotPage from "@/views/chatbot/chatbot.vue";

>>>>>>> 7c5949420da77f392dc546ea9c286700d8d58b51

export default {
  name: 'InfoMain',
  data (){
    return {
      chatbotButton : false,
      ai : 'ChatGPT를',
      imgUrl: "https://bucket-aiacademy.s3.ap-northeast-2.amazonaws.com/borrowsan",
      images: ["https://bucket-aiacademy.s3.ap-northeast-2.amazonaws.com/borrowsan/chatimg.png",
              "https://bucket-aiacademy.s3.ap-northeast-2.amazonaws.com/borrowsan/detectimg.png",
              "https://bucket-aiacademy.s3.ap-northeast-2.amazonaws.com/borrowsan/fore.png"
              ],
      imageIndex : 0,
      inputData: '',
      result: ''
    }
  },
  methods : {
    chatBg(){
      if (this.chatbotButton == false){
        this.chatbotButton = true;
      }else{
        this.chatbotButton = false;
      }
    },
    scrollImg(){
      if (this.ai == 'ChatGPT를'){
        this.ai = '객체 인식을';
      }else if (this.ai == '객체 인식을'){
        this.ai= '수요 예측을'
      }else if (this.ai == '수요 예측을'){
        this.ai='ChatGPT를'
      }
    },
    changeImg(){
      this.imageIndex = (this.imageIndex + 1) % this.images.length
    },
    async sendRequest() {
      const response = await axios.post('http://borrowsan.shop/chatbot/gpt3', { inputData: this.inputData });
      this.result = response.data.result;
    },
  },
  components: {
<<<<<<< HEAD
=======
    Chatbot:ChatbotPage
>>>>>>> 7c5949420da77f392dc546ea9c286700d8d58b51
  }
}
</script>

<style>
body {
  background-color: #E1E7E7;
}

.sub-menu{
  padding-left: 10px;
  position: fixed;
  left: 96%;
  top: 60%;
  background-color: black;
  display: table-column;
  padding-bottom: 1px;
  border-radius: 5px;
}
.card-row {
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 380px;
  width: 100%;
  height: 500px;
}

.card {
  position: relative;
  background-color: #FFFFFF;
  height: 370px;
  width: 240px;
  margin: 10px;
  overflow: hidden;
  margin-right: 5%;
  box-shadow: 0px 2px 4px 0px rgba(0,0,0,0.5);
}

.card:hover{
  transform: scale(1.3);
}

.card-image {
  /* center horizontally overflown image */
  position: absolute;
  left: -9999px;
  right: -9999px;
  margin: auto;
  height: 220px;
  min-width: 100%;
}

.card-footer {
  position: absolute;
  bottom: 0;
  height: 130px;
  padding: 10px 15px;
  font-family: Helvetica;
}
.card-text {
  font-size: 14px;
  font-weight: 100;
  color: rgba(0, 0, 0, 0.7);
}
.card-title {
  font-family: Serif;
}
.card-author {
  font-size: 14px;
  color: #BAB096;
}

#app {
  font-family: Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

head {
  position: fixed;
  width: 100%;
}

body{
  margin: 0px;
  font-family: Helvetica, Arial, sans-serif;
  color: white;
  width: 100%;
}

a{
  text-decoration: none;
  color: white;
}
a:hover{
  color: #1ed760;
}

.logo{
  width: 13vw;
  height: 7vh;
}

nav{
  height: 8vh;
  background-color: rgb(178, 255, 102);
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-around;
}

.nav-item{
 padding: 7vw 1vh;
 color: black;
 font-weight: 700;
}

main{
  padding-right: 60%;
  height: 100vh;
  width: 100%;
  background-color: rgb(178, 255, 102);
  background-size: 100%;
  background-position: 46% 4%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.main-container{
  border: 1px solid black;
  width: 100vw;
}

.main-container-img{
  width: 100%;
  height: 50%;
  background-size: 100%;
}
.main2{
  height: 100vh;
  width: 100%;
  background-color : white;
  background-size: 100%;
  background-position: 46% 4%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-right: 60%;
}

.head{
  font-size: 8vw;
  line-height: 14vh;
  color: #1ed760;
  font-weight: 900;
  position: relative;
  left: 0vw;
  padding-bottom: 8vh;
}
.head2{
  font-size: 2vw;
  line-height: 14vh;
  color: black;
  font-weight: 900;
  position: relative;
  left: 1vw;
  padding-bottom: 8vh;
}
.head-f{
  color : black;
  position: relative;
  left: -2.5em;
  bottom: 200px;
}
.head-l{
  color : black;
  position: relative;
  text-align: left;
}
.sub-head{
  text-align: center;
  margin-top: 300px;
  margin-bottom: 10px;
}

.sub-head2{
  text-align: center;
  margin-bottom: 10px;
}
.text-left {
  padding-right: 80%;

  padding-top: 0px;
  color: black;
  font-size: 5vw;
}

.button-area {
  padding-left: 55%;

}
.button-style{
  padding: 1vw 5vw;
  background-size: 120%;
  background-repeat: no-repeat;
  background-position: center;
}

.button-style:hover{
  transform: scale(1.07);
    background-color: #2de26d;
}


footer{
  height: 530px;
  background-color: black;
  width: 100vw;
  display: flex;
  justify-content: center;
}

.footer-container{
  max-width: 100%;
  width: 100%;
  padding-top: 8vh;
  padding-bottom: 5vh;
}

.footer-menu{
  display: flex;
  justify-content: space-between;
  height: 34vh;
}

.first-box{
  width: 60%;
  display: flex;
  justify-content: space-between;
}

.second-box{
  width: 40%;
  display: flex;
  justify-content: flex-end;
}

.column{
  display: flex;
  flex-direction: column;
  padding: 0 5vw;
}

.footer-title{
  color: white;
  font-size : 20px;
  font-weight: 900;
  margin: 20px 0px;
}

.footer-items{
  padding-bottom: 1.5vh;
  padding-top: 2vh;
  font-size: 1vw;
}

.icon{
  width: 54px;
  height: 54px;
  background-color: white;
  border-radius: 50%;
  margin-right: 15px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 24px;
}
<<<<<<< HEAD
.icon:hover{
  transform: scale(1.08);
}
.chatbot{
  border-radius: 50%;
  background-color: white;
  color: black;
  position: fixed;
  right: 15px;
  bottom: 15px;
  width: 80px;
  height: 80px;
  z-index: 99;

}

.chat-item{
  display: flex;
  justify-content: space-between;
}
.chat-body{
  display: flex;
  justify-items: center;
  right: 1px;
  height: 65%;
  width: 100%;
  border: 1px solid black ;
}

.chat-input{
  display: flexbox;
  align-content: center;
  width: 100%;
  border-radius: 5px;
  margin-top: 90%;
}

.chatBgWhite {
  height: 30%;
  width: 30%;
  position: fixed;
  color: black;
  background: white;
  bottom: 0;
  right: 0;
  border-radius: 8px;
  padding: 10px 5px;
  border: 1px solid red ;
}
=======

>>>>>>> 7c5949420da77f392dc546ea9c286700d8d58b51

.footer-middle{
  color: #919496;
  display: flex;
  justify-content: flex-end;
  font-size: 2vw;
}

.footer-end{
  color: #919496;
  display: flex;
  justify-content: space-between;
  margin-top: 1.2vw;
}

.footer-end-item{
  margin-right: 2vw;
  color: #919496;
}

</style>