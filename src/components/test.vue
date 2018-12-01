<template>
  <div id="app">


    <SvgGraph
      :width="750"
      :height="450"
      :circlePos=circles_pos
    />

  </div>
</template>

<script>
import SvgGraph from './SvgGraph'
export default {
  name: 'App',
  data(){
    return{
      circles_pos:[
      {
        "x":0,
        "y":75,
        "label":"Bolt 1"
      },
      {
        "x":100,
        "y":95,
        "label":"Bolt 2"
      },
      {
        "x":200,
        "y":115,
        "label":"Bolt 3"
      }
      ]
    }

  },
  components: {
    SvgGraph
  }
}
</script>
