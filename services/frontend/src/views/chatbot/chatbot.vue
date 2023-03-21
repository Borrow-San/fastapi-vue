<template>
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
</template>

<script>
import axios from 'axios';

export default {
  name: 'ChatBot',
  data (){
    return {
      chatbotButton : true,
      inputData: '',
      result: ''
    }
  },
  methods: {
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
</style>