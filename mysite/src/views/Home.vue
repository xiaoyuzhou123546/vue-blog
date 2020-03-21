<template>
  <div class="home">
    <HelloWorld msg="获取数据"/>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  },
  mounted(){
    // console.log(123)
  }
}
</script>
