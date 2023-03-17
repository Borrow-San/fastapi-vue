<template>
  <body>
    <nav id="App" class="header">
      <a href="#" class="nav-item"><img src="../assets/bslogo.png" class="logo"></a>
      <div>
        <a href="#" class="nav-item">서비스 소개</a>
        <a href="#" class="nav-item">이용방법</a>
        <a href="" class="nav-item">|</a>
        <router-link to="/login" class="nav-item">Log in</router-link>
      </div>
    </nav>
    <a href="#" class="chatbot" v-if="chatbotButton == false"><img src="../assets/chatbot.png" @click="chatBg"  class="chatbot"></a>
    <div v-if="chatbotButton == true">
      <div class="chatBgWhite">
        <div class="chat-item" style="height:15%; padding-botton:3px;">
          <td><h5 class="modal-title"></h5></td>
          <td>
            <button type="button" @click="chatBg" style="display: flex; align-items:flex-end;">
              <span>x</span>
            </button>
          </td>
        </div>
        <div class="chat-body">
          챗봇화면 
        </div>
        <tr class="chat-input" style="border: 100px green solid;">
          <td>
            <input type="text" style="width: 90%;">
          </td>
          <td>
            <button style="width: 50px;">전송</button>
          </td>
        </tr>
      </div>
    </div>
    
    <main name="landing1">
      <div class="main-container">
        <div class="head">
          <div class="head-f">
            Borrow-San
          </div>
        </div>
        <div class="sub-head" style="font-size: 2.5vw; color:black;">
          "인공지능을 활용한 효율적인 자원 관리를 위한 공유경제 서비스 자동화"
        </div>
        <div class="button-area">
          <button class="button-style"></button>
        </div>
      </div>
    </main>
    <main2 name="landing2">
      <div class="main-container" style="float: left; width: 50%; heignt:10%;">
        <div class="head2" >
          <div style="text-align:left;">바로우산?</div> 
          <tr>
            <td>
              <div class="sub-head2" style="font-size: 2vw;">ChatGPT</div>
              <div class="sub-head2">객체 인식</div>
              <div class="sub-head2">수요 예측 인공지능</div>
            </td>
            <td>
              <div class="head-l">을 이용한 공유경제 자동화 서비스</div>
            </td>
          </tr>
        </div>
      </div>
      <div style="float: left; width: 50%; heignt:10%;">
        <img src="../assets/umb.jpg" style="width:100%; heigh:100%;">
      </div>
    </main2>
    <main class="text-left" name="landing3">
      <div>이용방법</div>
    </main>
    <main2>
      <div id="app" style="float: left; width: 33%;">
        <div class="card-row">
          <div class="card">
            <img class="card-image" src="../assets/devsb.jpg">
            <div class="card-footer">
              <p class="card-text" style="font-size:20px; font-weight:bold; text-align:left;">박성배</p>
              <a href="https://github.com/Seongbae103" class="footer-items" style="color:black;"><img src="https://play-lh.googleusercontent.com/PCpXdqvUWfCW1mXhH1Y_98yBpgsWxuTSTofy3NGMo9yBTATDyzVkqU580bfSln50bFU" alt="" class="icon" style="float: left;"></a>
              <a href="https://velog.io/@boost_dev" class="footer-items" style="color:black;"><img src="data:image/jpeg;base64,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" alt="" class="icon" style="float: left;"></a>
            </div>
          </div>
        </div>
      </div>
      <div id="app" style="float: left; width: 33%;">
        <div class="card-row">
          <div class="card">
            <img class="card-image" src="../assets/devhy.jpg">
            <div class="card-footer">
              <p class="card-text" style="font-size:20px; font-weight:bold; text-align:left;">박하연</p>
              <a href="https://github.com/phayeon" class="footer-items" style="color:black;"><img src="https://play-lh.googleusercontent.com/PCpXdqvUWfCW1mXhH1Y_98yBpgsWxuTSTofy3NGMo9yBTATDyzVkqU580bfSln50bFU" alt="" class="icon" style="float: left;"></a>
            </div>
          </div>
        </div>
      </div>
      <div id="app" style="float: left; width: 33%;">
        <div class="card-row">
          <div class="card">
            <img class="card-image" src="">
            <div class="card-footer">
              <p class="card-text" style="font-size:20px; font-weight:bold; text-align:left;">이강산</p>
              <a href="https://github.com/gangsanlee2" class="footer-items" style="color:black;"><img src="https://play-lh.googleusercontent.com/PCpXdqvUWfCW1mXhH1Y_98yBpgsWxuTSTofy3NGMo9yBTATDyzVkqU580bfSln50bFU" alt="" class="icon" style="float: left;"></a>
            </div>
          </div>
        </div>
      </div>
    </main2>
  </body>
  <footer name="landing4" style="width:100%;"> 
    <div class="footer-container">
      <div class="footer-menu">
        <div class="first-box">
          <img src="../assets/footerlogo.png" class="logo">
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
        <div class="second-box" style="padding-right:2vw;">
          <a href="https://github.com/Borrow-San"><img src="../assets/git.png" class="icon"></a>
          <a href="https://borrow-san.atlassian.net/wiki/home"><img src="../assets/confluence.png" class="icon"></a>
          <a href="https://velog.io/@boost_dev/series/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8"><img src="data:image/jpeg;base64,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" class="icon"></a>
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

export default {
  name: 'infoMain',
  data (){
    return {
      chatbotButton : true,
      ai : ['ChatGPT', '객체 인식', '수요 예측']
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
  },
  components: {
    
  }
}
</script>

<style>
body {
  background-color: #E1E7E7;
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
  box-shadow: 0px 2px 4px 0px rgba(0,0,0,0.5);
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
  height: 100vh; 
  background-color: rgb(178, 255, 102);
  background-size: 100%;
  background-position: 46% 4%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.main-container{
  border: 1px solid none;
}
.main2{
  border: 1px solid none;
  height: 100vh;
  width: 100%;
  background-color : white;
  background-size: 175%;
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
}
.head-l{
  color : black;
  position: relative;
  text-align: left;
}
.sub-head{
  color: #1ed760;
  font-size: 18px;
  line-height: 24px;
  padding-bottom: 40px;
  text-align: center; 
}

.sub-head2{
  color: #1ed760;
  font-size: 1.5vw;
  line-height: 2vh;
  padding-bottom: 4vw;
  text-align: center; 
}
.text-left {
  padding-right: 60%;
  padding-top: 0px;
  color: black;
  font-size: 5vw;
}

.button-area {
  padding-left: 55%;
}
.button-style{
  padding: 1vw 5vw;
  background-image: url('../assets/googleplay.png');
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

</style>