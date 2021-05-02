import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Mystudyplan from '../views/Mystudyplan.vue'
import StudyPlan from '../components/StudyPlan'
import Idea from '../components/Idea'
import Navigation from '../components/Navigation'
import Case  from '../components/Case'
import Photo from '../components/Photo'
import StudyMaterials from '../components/StudyMaterials'
import Api from '../components/Api'
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
      },
      children:[
        {
          path: '/', 
          name: 'StudyPlan',
          component: StudyPlan, 
          beforeEnter: (to, from, next) => {
            body("学习计划")
            next()
          }
        },
        {
          path: '/blog/StudyPlan', 
          name: 'StudyPlan',
          component: StudyPlan, 
          beforeEnter: (to, from, next) => {
            body("学习计划")
            next()
          }
        },
        {
          path: '/blog/Idea', 
          name: 'Idea',
          component: Idea, 
          beforeEnter: (to, from, next) => {
            body("想法")
            next()
          }
        },
        {
          path: '/blog/Navigation', 
          name: 'Navigation',
          component: Navigation, 
          beforeEnter: (to, from, next) => {
            body("导航")
            next()
          }
        },
        {
          path: '/blog/Case', 
          name: 'Case',
          component: Case, 
          beforeEnter: (to, from, next) => {
            body("案例")
            next()
          }
        },
        {
          path: '/blog/Photo', 
          name: 'Photo',
          component: Photo, 
          beforeEnter: (to, from, next) => {
            body("相册")
            next()
          }
        },
        {
          path: '/blog/StudyMaterials', 
          name: 'StudyMaterials',
          component: StudyMaterials, 
          beforeEnter: (to, from, next) => {
            body("学习资源")
            next()
          }
        },
        {
          path: '/blog/Api', 
          name: 'Api',
          component: Api, 
          beforeEnter: (to, from, next) => {
            body("API")
            next()
          }
        }
      ]
    },
  ]
})
function body(content) {
  document.getElementById('titleId').innerHTML = content
  document.querySelector('body').style.overflow="visible"
}
