import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    // redirect 路由重定向  component 注册
    { 
      path: '/', 
      redirect: '/login',
      beforeEnter: (to, from, next) => {
        document.getElementById('titleId').innerHTML = "登入界面"
        next()
      }
    },
    { 
      path: '/login', 
      component: Login, 
      beforeEnter: (to, from, next) => {
        document.getElementById('titleId').innerHTML = "登入界面"
        // document.querySelector('body').style.overflow="visible"
        next()
      }
    },
  ]
})
