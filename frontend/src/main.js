import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import VueResource from 'vue-resource'
import 'element-ui/lib/theme-chalk/index.css'
import qs from "qs"
Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(VueResource)
import axios from 'axios'
Vue.prototype.$axios = axios
Vue.prototype.$qs = qs
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
