import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import BoltInLine from '@/components/BoltInLine'
import I_Shape from '@/components/sections/I_shape.vue'
import rhsShape from '@/components/sections/rhsShape.vue'
import LStiffShape from '@/components/sections/LStiffShape.vue'
import PlateStiffShape from '@/components/sections/PlateStiffShape.vue'
import TStiffShape from '@/components/sections/TStiffShape.vue'
import LShape from '@/components/sections/LShape.vue'
import UShape from '@/components/sections/UShape.vue'
import CHSShape from '@/components/sections/CHSShape.vue'
import SC_simple_partial_endplate from '@/components/SC_simple_partial_endplate.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/SC_simple_partial_endplate',
      name: 'SC_simple_partial_endplate',
      component: SC_simple_partial_endplate
    },
    {
      path: '/BoltInLine',
      name: 'BoltInLine',
      component: BoltInLine
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
    },
    {
      path: '/PlateStiffShape',
      name: 'PlateStiffShape',
      component: PlateStiffShape
    },
    {
      path: '/TStiffShape',
      name: 'TStiffShape',
      component: TStiffShape
    },
    {
      path: '/LShape',
      name: 'LShape',
      component: LShape
    },
    {
      path: '/UShape',
      name: 'UShape',
      component: UShape
    },
    {
      path: '/CHSShape',
      name: 'CHSShape',
      component: CHSShape
    }
  ],
  mode: 'history'
})
