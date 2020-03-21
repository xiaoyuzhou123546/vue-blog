<template>
  <div id="app">
    <div id="nav">
      <div class="nav_left">标题</div>
      <div class="nav_right" v-show="barBool"  >
        <router-link ref="link" v-for="item in link_array" :key="item.name" :to="item.url">{{item.name}}</router-link>
      </div>    
    </div>
    <router-view  />
    <h1>现在是公共页面</h1>
    <div class="site-bottom" >
      copyingright:小宇宙
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return {
      link_array:[{
        name:'首页',
        url:'/'
      },{
        name:'博客',
        url:'/blog'
      },{
        name:'下载',
        url:'/download'
      },{
        name:'工作',
        url:'/workers'
      },{
        name:'编辑',
        url:'/about'
      },],
      barBool:true,
      goodstr:{}
    }
  },
  // created:vue生命周期中的钩子函数，在这个时间点，data中的数据已经注入到响应式系统中
created(){
    this.$axios.get('http://127.0.0.1:5000/',{       // 还可以直接把参数拼接在url后边
        params:{}
    }).then(res=>{
      console.log(res)
        this.goodstr = res.data;
    })
}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #666;
  padding-top: 20px;
}

#nav {
  /* padding: 30px; */
  width: 100%;
  height: 40px;
  background-color: rgba(59, 19, 19, 0.411);
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 100;
}
.nav_left{
  width: 20%;
  height: inherit;
}
.nav_right{
  width: 35%;
  height: inherit;
  display: flex;
  justify-content: space-around;
  align-items: center;
  min-width:220px ;
  max-width: 350px;
  margin-right: 5%;
}
#nav a {
  /* font-size: 0.95rem; */
  font-weight: bold;
  color: #fff;
  text-decoration: none ;
}
#nav a:hover {
  color: #42b983;
  /* text-decoration-line: underline; */
}
#nav a.router-link-exact-active {
  color: #42b983;
  text-decoration-line: underline;
}
/* 取消滚动条 */
::-webkit-scrollbar {
  width: 0 !important;
}
::-webkit-scrollbar {
  width: 0 !important;height: 0;
}
.site-bottom{
  width: 100%;
  height: 40px;
  background-color: #666;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #fff;
}





table {
  border-top: 1px solid #ccc;
  border-left: 1px solid #ccc;
}
table td,
table th {
  border-bottom: 1px solid #ccc;
  border-right: 1px solid #ccc;
  padding: 3px 5px;
}
table th {
  border-bottom: 2px solid #ccc;
  text-align: center;
}

/* blockquote 样式 */
blockquote {
  display: block;
  border-left: 8px solid #d0e5f2;
  padding: 5px 10px;
  margin: 10px 0;
  line-height: 1.4;
  font-size: 100%;
  background-color: #f1f1f1;
}

/* code 样式 */
code {
  display: inline-block;
  *display: inline;
  *zoom: 1;
  background-color: #7a7777;
  border-radius: 3px;
  padding: 3px 5px;
  margin: 0 3px;
  color: rgba(194,197,101);
}
pre code {
  display: block;
}

/* ul ol 样式 */
ul, ol {
  margin: 10px 0 10px 20px;
}
</style>
