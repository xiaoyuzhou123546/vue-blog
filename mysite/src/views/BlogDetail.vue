<template>
    <div class="blogdetail">
        <h3>{{blogDetail.title}}</h3>
        <p>auth:{{blogDetail.auth}}</p>
        <div ref="editorElem" v-html="blogDetail.content">
            {{blogDetail.content}}
        </div>
    </div>
</template>

<script>
export default {
    name:'BlogDetail',
    data(){
        return {
           blogDetail:{} 
        }
    },
    created(){
        const id = Number(this.$route.query.id)
        console.log(id)
        this.$axios.get('http://127.0.0.1:5000/blogdetail',{       // 还可以直接把参数拼接在url后边
        params:{
            id:id
        }
    }).then(res=>{
      console.log('博客内容',res.data.result)
        this.blogDetail = res.data.result;
    })
    },
    mounted(){
        
       
    }

}
</script>

<style scoped>
.blogdetail{
    padding: 80px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}


</style>