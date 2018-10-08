import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import HelloWorld from '@/components/HelloWorld'
import About from '@/components/About'
import CrossSections from '@/components/CrossSections'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/About',
      name: 'About',
      component: About
    },
    {
      path: '/CrossSections',
      name: 'CrossSections',
      component: CrossSections
    },
    {
      path: '/Home',
      name: 'Home',
      component: Home
    }
  ]
})
