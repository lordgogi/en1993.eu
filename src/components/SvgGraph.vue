<template>
  <div>
    <svg
      @mousemove="someMethod"
      @mouseup="mouseUp"
      @mousedown="mouseDown"
      @wheel="onwheel($event)"

      :viewBox="view"
      :width="width"
      :height="height"

    >
      <circle v-for="(item, index) in circlePos"
        :cx="item.x"
        :cy="item.y"
        :r="16"/>


    </svg>

    <br>
    View Box : {{view}}<br>
    Is pressed: {{isPressed}}<br>
    X: {{xPos}}
    Y: {{yPos}}<br>
    pos0: {{pos0}}<br>
    pos1: {{pos1}}<br>
    vector_x:  {{vector_x}}<br>
    Viewport Scale: {{scale}}<br>
    Wheel Counter: {{wheel}}


  </div>

</template>

<script>
export default {
  name: 'SvgGraph',
  data(){
    return{
      view:[0, 0, 150, 150],
      isPressed:false,
      xPos:0,
      yPos:0,
      vector_x:0,
      vector_y:0,
      pos0:[0,0],
      pos1:[0,0],
      wheel:0,

    }
  },
  methods:{

    onwheel(e){
      this.wheel = e.deltaY
      if ( e.deltaY>0){
        this.view = [this.view[0]+10, this.view[1]+10, this.view[2]-20, this.view[3]-20]
      }
      else {
        this.view = [this.view[0]-10, this.view[1]-10, this.view[2]+20, this.view[3]+20]
      }



    },

    someMethod(event) {
        this.xPos = event.clientX;
        this.yPos = event.clientY;

    },
    mouseDown(){
      this.isPressed = true
      this.pos0 = [event.clientX, event.clientY]
    },
    mouseUp(){
      this.isPressed = false
      this.pos1 = [event.clientX, event.clientY],
      this.vector_x = (this.pos1[0]-this.pos0[0])*this.scale[0],
      this.vector_y = (this.pos1[1]-this.pos0[1])*this.scale[0],
      this.view = [this.view[0]-this.vector_x,this.view[1]-this.vector_y,this.view[2],this.view[3]]

    }


  },

  computed: {
    scale: function(){
      return [this.view[2]/this.height,this.view[3]/this.height];
    },
  },

  props: {

    width: {
      type: Number,
      default: 50,
      required: false
    },
    height: {
      type: Number,
      default: 50,
      required: false
    },
    circlePos:{
      type: Array,
      default:[],
      required: false
    }

  }
}
</script>
