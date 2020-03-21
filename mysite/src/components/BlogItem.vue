<template>
  <div class="blog-view" @click="linkurl" >
    <!-- <h1 @click="getdata" >点击</h1> -->
    <h4>{{blogstr.title}}</h4>
    <img id="blog-img" src="" alt="">
    <i id="blog-content" >{{blogstr.content | dataFormat }}</i>
  </div>
</template>

<script>
export default {
  name: 'BlogItem',
  props: {
    blogstr: Object
  },
  create(){
    console.log('博客页面')
  },
  methods:{
    linkurl(){
      this.$router.push({ path: "blogdetail", query: { id: this.blogstr.blog_id } });
    }
  },
  filters:{
     dataFormat(val){//val就是以获取的msg的值
      return val.replace(/<[^>]*>/g,'');//去除文字的<...></...>标签
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.blog-view{
  width: 260px;
  height: 300px;
background-color: #999;
margin: 20px;
}
#blog-content{
  font-size: 0.7rem;
  width: inherit;
  display: -webkit-box; /*作为弹性伸缩盒子模型显示*/
  -webkit-line-clamp: 5; /*显示的行数；如果要设置2行加...则设置为2*/
  overflow: hidden;
  text-overflow: ellipsis; /* 溢出用省略号*/
  /*! autoprefixer: off */
  -webkit-box-orient: vertical;/*伸缩盒子的子元素排列：从上到下*/
  text-align: start;
}
#blog-img{
  width: inherit;
  height: 50%;
}
</style>
