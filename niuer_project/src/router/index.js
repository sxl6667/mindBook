import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Mystudyplan from '../views/Mystudyplan.vue'
Vue.use(VueRouter)

export default new VueRouter({
  mode: "history",
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
    { 
      path: '/blog', 
      name: 'Mystudyplan',
      component: Mystudyplan, 
      beforeEnter: (to, from, next) => {
        body("学习计划")
        next()
      }
    },
  ]
})
function body(content) {
  document.getElementById('titleId').innerHTML = content
  document.querySelector('body').style.overflow="visible"
}
