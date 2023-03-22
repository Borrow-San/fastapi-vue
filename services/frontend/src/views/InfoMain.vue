<template>
  <header style="width:100%">
    <nav>
      <a href="#" class="nav-item"><img :src="imgUrl +'/bslogo.PNG'" class="logo"></a>
      <div style="background-color: black; border-radius: 10px;">
        <a href="https://github.com/Borrow-San" target="_blank" class="nav-item" style="float: left;"><img :src="imgUrl +'/git.png'" class="icon"></a>
        <a href="https://velog.io/@boost_dev/series/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8" target="_blank" class="nav-item" style="float: left;"><img :src="imgUrl + '/veloglogo.jpeg'" class="icon"></a>
      </div>
    </nav>
  </header>
  <body>
    <a href="#" class="chatbot" v-if="chatbotButton == false"><img :src="imgUrl +'/chatbot.png'" @click="chatBg"  class="chatbot"></a>
    <div v-if="chatbotButton == true">
      <div class="chatBgWhite">
        <div class="chat-item" style="display:flex; top:1px; height:15%; padding-botton:3px;">
          <h5 class="modal-title">챗봇</h5>
            <button type="button" @click="chatBg" style="height:30px;">
              <span>x</span>
            </button>
        </div>
        <div class="chat-body">
          {{ result }}
        </div>
        <div class="chat-input">
          <div>
            <input type="text" v-model="inputData">
          </div>
          <div>
            <button @click="sendRequest">전송</button>
          </div>
        </div>
      </div>
    </div>

    <main name="landing1" style="width:100%">
      <div class="main-container-img" :style="{ 'background-image': 'url(' + imgUrl + '/detectimg.png)' }">
        <div class="head">
          <div class="head-f">
            Borrow-San
          </div>
        </div>
        <div class="sub-head" style="font-size: 2.5vw; color:black;">
          "효율적인 자원 관리를 위한 인공지능 기반 공유경제 서비스 자동화"
        </div>
      </div>
    </main>
    <main2 name="landing2">
      <div style="float: left; width: 50%; height:10%;">
        <div class="head2">
          <div style="text-align:left;">바로우산?</div>
          <tr style="width:100%;">
            <a href="https://velog.io/@boost_dev/%EB%B0%94%EB%A1%9C%EC%9A%B0%EC%82%B0-%EC%A0%84%EC%B2%B4-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%A7%84%ED%96%89" target="_blank"><img :src="imgUrl +'/landing01.png'" style="width:100%;" @mouseover="changeImg(1)"></a>
            <a href="https://velog.io/@boost_dev/%EB%B0%94%EB%A1%9C%EC%9A%B0%EC%82%B0-YOLOv5%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%9C-%EC%9A%B0%EC%82%B0-%EC%9D%B8%EC%8B%9D" target="_blank"><img :src="imgUrl +'/landing02.png'" style="width:100%;" @mouseover="changeImg(2)"></a>
            <a href="https://velog.io/@boost_dev/KoGPT2-%ED%8C%8C%EC%9D%B8%ED%8A%9C%EB%8B%9D%EC%9D%84-%ED%86%B5%ED%95%9C-%EC%84%9C%EB%B9%84%EC%8A%A4%EC%9A%A9-%EC%B1%97%EB%B4%87" target="_blank"><img :src="imgUrl +'/landing03.png'" style="width:100%;" @mouseover="changeImg(3)"></a>
            <a href="https://velog.io/@boost_dev/%EB%B0%94%EB%A1%9C%EC%9A%B0%EC%82%B0-%EC%88%98%EC%9A%94%EC%98%88%EC%B8%A1-%EB%AA%A8%EB%8D%B8" target="_blank"><img :src="imgUrl +'/landing04.png'" style="width:100%;" @mouseover="changeImg(4)"></a>
          </tr>
        </div>
      </div>
      <div style="float: left; width: 40%; height:15%; padding-left:50px; padding-top:125px;"><img :src="imgUrl + sampleImg" style="width:100%; height:100%;"></div>
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
                  <a href="https://github.com/Seongbae103" target="_blank" class="footer-items" style="color:black;"><img :src="imgUrl +'/git.png'" alt="" class="icon" style="float: left;"></a>
                  <a href="https://velog.io/@boost_dev" target="_blank" class="footer-items" style="color:black;"><img :src="imgUrl + '/veloglogo.jpeg'" alt="" class="icon" style="float: left;"></a>
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
                  <a href="https://github.com/phayeon" target="_blank" class="footer-items" style="color:black;"><img :src="imgUrl +'/git.png'" alt="" class="icon" style="float: left;"></a>
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
                  <a href="https://github.com/gangsanlee2" target="_blank" class="footer-items" style="color:black;"><img :src="imgUrl +'/git.png'" alt="" class="icon" style="float: left;"></a>
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
          <a href="#"><img :src="imgUrl + '/footerlogo.PNG'" class="logo"></a>
          <div class="column">
            <div class="footer-title">박성배</div>
              <a href="https://github.com/Seongbae103" class="footer-items" target="_blank">Github</a>
              <a href="https://velog.io/@boost_dev" class="footer-items" target="_blank">Velog</a>
          </div>
          <div class="column">
            <div class="footer-title">박하연</div>
              <a href="https://github.com/phayeon" class="footer-items" target="_blank">github</a>
          </div>
          <div class="column">
            <div class="footer-title">이강산</div>
              <a href="https://github.com/gangsanlee2" target="_blank" class="footer-items">github</a>
              <a href="" class="footer-items"></a>
              <a href="" class="footer-items"></a>
          </div>
        </div>
      </div>
      <div class="footer-middle"><i class="fa-solid fa-earth-africa" style="padding-right:2vw;">Borrow-San</i></div>
      <div class="footer-end">
        <div>
          <a href="https://borrow-san.atlassian.net/wiki/home" target="_blank" class="footer-end-item">Team Confluence</a>
          <a href="https://github.com/Borrow-San" target="_blank" class="footer-end-item">Team Github</a>
          <a href="https://velog.io/@boost_dev/series/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8" target="_blank" class="footer-end-item">Learning records</a>
        </div>
        <div style="padding-right:2vw;" >2022.11 - 2023.03 </div>
      </div>
    </div>
  </footer>


</template>

<script>
import axios from 'axios';

export default {
  name: 'InfoMain',
  data (){
    return {
      chatbotButton : false,
      ai : 'ChatGPT를',
      imgUrl: "https://bucket-aiacademy.s3.ap-northeast-2.amazonaws.com/borrowsan",
      sampleImg: '/sample01.png',
      inputData: '',
      result: '',
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
    changeImg(i){
      if (i == 1){
        this.sampleImg = '/sample01.png'
      }else if(i == 2){
        this.sampleImg = '/sample02.png'
      }else if(i == 3){
        this.sampleImg = '/sample03.png'
      }else if(i == 4){
        this.sampleImg = '/sample04.png'
      }
    },
    async sendRequest() {
      const response = await axios.post('http://borrowsan.shop/chatbot/gpt3', { inputData: this.inputData });
      this.result = response.data.result;
    },
  },
  components: {
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
  top: 50%;
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
.

#app {
  font-family: Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
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
  position: absolute;
  top:0px;
  height: 8vh;
  background-color: rgb(178, 255, 102);
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-around;
}

.nav-item{
  padding: 1vw 1vh;
  color: black;
  font-weight: 700;
  border-radius: 10px;
}

.nav-item:hover {
  transform: scale(1.07);
}

main{
  height: 100vh;
  width: 100%;
  background-color: rgb(178, 255, 102);
  background-size: 100%;
  background-position: 46% 4%;
  display: flex;
  align-items: center;
  justify-content: center;
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
  height: 4%;
}

.chat-body{
  height: 65%;
  width: 90%;
  position: absolute;
  top: 50px;
  bottom: 50px;
  border: 1px solid gray;
  overflow-y: scroll;
  padding-top: 40%;
}

.chat-input{
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    display: flex;
    justify-content: space-around;
    align-items: center;
    background-color: #f2f2f2;
    padding: 10px 0px;
}

.chat-input input[type="text"] {
  flex-grow: 1;
  margin-right: 5px;
  border-radius: 5px;
  border: none;
  padding: 5px;
  font-size: 16px;
}

.chat-input button {
  border-radius: 5px;
  border: none;
  padding: 5px 10px;
  font-size: 16px;
  padding-right: 20px;
  width: 80px;
  color: white;
  background-color: #007bff;
  cursor: pointer;
}

.chat-input button:hover {
  background-color: #0062cc;
}

.chatBgWhite {
  background-color: white;
  padding: 20px;
  border: 1px solid #888;
  height: 90%;
  width: 30%;
  position: fixed;
  border-radius: 8px;
  right: 0;
}

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

.box{
  border: 2px solid red ;
  margin: 1%;
}

.sticky {
  position: sticky;
  top: 0;
  width: 100%;
  height: 100vh;
}

.slide-container {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
}

.slide {
  position: absolute;
  display: none;
  z-index: 0;
}

.slide.enabled {
  display: block;
}
</style>