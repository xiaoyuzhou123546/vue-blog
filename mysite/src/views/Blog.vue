<template>
<div class="blog" >
	<!-- <h1>现在是博客页面</h1> -->
	<BlogItem  v-for="(item,index) in blogList "  :key="index" :blogstr="item" />
</div>
</template>

<script>
import BlogItem from '@/components/BlogItem.vue'

export default {
  name: 'blog',
  components: {
    BlogItem
  },
  data(){
    return{
      blogList:[]
    }
  },
  created(){
    this.$axios.get('http://127.0.0.1:5000/blog',{       // 还可以直接把参数拼接在url后边
        params:{}
    }).then(res=>{
      console.log('博客列表',res.data.result)
        this.blogList = res.data.result;
    })
  }
}
</script>

<style scoped>
.blog{
	width: 100%;
	min-height: 500px;
  display: flex;
  flex-direction: row;
  padding: 80px;
  box-sizing: border-box;
  flex-wrap: wrap;
}
</style>
