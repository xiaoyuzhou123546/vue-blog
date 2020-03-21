import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Blog from '../views/Blog.vue'
import DownLoad from '../views/DownLoad.vue'
import Workers from '../views/Workers.vue'
import BlogDetail from "../views/BlogDetail.vue"

Vue.use(VueRouter)

const routes = [
  {path: '/',name: 'Home',component: Home},
  {path: '/about',name: 'About',component: About},
  {path: '/workers',name: 'Workers',component: Workers},
  {path: '/download',name: 'DownLoad',component: DownLoad},
  {path:'/blog',name:'Blog',component:Blog},
  {path:'/blogdetail',name:'BlogDetail',component:BlogDetail}
]

const router = new VueRouter({
  routes
})

export default router
