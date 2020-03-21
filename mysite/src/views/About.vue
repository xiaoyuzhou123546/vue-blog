<template>
  <div class="edit">
    <div class="edit-title" >
      <h4>请输入标题:</h4>
      <input class="input-title" v-model="title" type="text" placeholder="标题不能重复" >
    </div>
    <MyEditor @change="handleAge"/>

    <button id="menu" @click="submit" >提交</button>
  </div>
</template>
<script>
import MyEditor from '@/components/MyEditor.vue'
export default {
  name:'About',
  components:{
    MyEditor
  },
  data(){
    return {
      title:'',
      content:''
    }
  },
  methods:{
   handleAge(e){
     this.content = e
     console.log(e)
   },
   submit(){
    //  console.log(this.title,this.content)
     this.$axios.post('http://127.0.0.1:5000/blog',{       // 还可以直接把参数拼接在url后边
        title:this.title,
        content:this.content,
        auth:'lezi'
    }).then(res=>{
      console.log('提交信息',res.data.result)
      alert('提交成功')
    })
     
   }

  }
}
</script>

<style  scoped>
.edit{
  padding: 80px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.edit-title{
  display:flex;
  align-items:center;
  margin: 30px 0;
}
.input-title{
  margin-left: 18px;
  width: 300px;
  height: 30px;
}
/* 提交按钮 */
#menu{
  margin-top: 100px;
}
</style>
