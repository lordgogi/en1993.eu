import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import About from '@/components/About'
import CrossSections from '@/components/CrossSections'
import I_Shape from '@/components/sections/I_shape.vue'
import rhsShape from '@/components/sections/rhsShape.vue'
import LStiffShape from '@/components/sections/LStiffShape.vue'

Vue.use(Router)

export default new Router({
  routes: [
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
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/I_Shape',
      name: 'I_Shape',
      component: I_Shape
    },
    {
      path: '/rhsShape',
      name: 'rhsShape',
      component: rhsShape
    },
    {
      path: '/LStiffShape',
      name: 'LStiffShape',
      component: LStiffShape
    }
  ],
  mode: 'history'
})
