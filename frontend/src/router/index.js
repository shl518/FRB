import Vue from 'vue'
import Router from 'vue-router'
import SignImage from '../components/SignImage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'SignImage',
      component:SignImage
    }
  ]
})
