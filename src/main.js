// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueRouter from 'vue-router'  // Add this
import VueAnalytics from 'vue-analytics'

Vue.config.productionTip = false

const isProd = process.env.NODE_ENV === 'production'

Vue.use(VueAnalytics, {
  id: 'UA-124823484-1',
  router,
  debug:{
    enabled: !isProd,
    sendHitTask:isProd
  }
})

Vue.use(VueRouter)                  // Add this

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
