<template>
  <div style="background-color:yellow; width:100%">
    <svg
      id="svg1"
      @mousemove="someMethod"
      @mouseup="mouseUp"
      @mousedown="mouseDown"
      @mouseenter="mouseEnter"
      @mouseleave="mouseLeave"
      @wheel="onwheel($event)"
      style="background: #ffffff"

      :viewBox="view"
      width=100%
      :height="height"

    >

    <defs>
      <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" />
      </marker>
    </defs>

    <polyline v-if="coordinate_sys" points="90,0 0,0 0,90" fill="none" stroke="black" marker-start="url(#arrow)" marker-end="url(#arrow)"  />

    <template v-for="elem in elements">

      // This is CIRCLES rendering
      <template v-if="elem.type=='circles' ">
        <circle v-for="item in elem.items"
          :cx="item.x"
          :cy="item.y"
          :fill="elem.color"
          :r="elem.radius"
        />
      </template>

      // This is ARROWS rendering
      <template v-if="elem.type=='arrows' ">
        <line v-for="item in elem.items"
          :x1="item.x"
          :y1="item.y"
          :x2="item.x + item.magnitude*Math.cos(item.angle*(Math.PI/180))*elem.scale"
          :y2="item.y - item.magnitude*Math.sin(item.angle*(Math.PI/180))*elem.scale"
          marker-end="url(#arrow)"
          style="stroke:rgb(255,0,0);stroke-width:2" />
      </template>

      // This is just to accomodate different naming convention for boltInline component. To be rewritten to be reusable
      <template v-if="(elem.type=='arrows_inline_prim' && elem.shown==true )">
        <line v-for="item in elem.items"
          :x1="item.bolt_x"
          :y1="item.bolt_y"
          :x2="item.bolt_x + item.bolt_Fx_prim*elem.scale"
          :y2="item.bolt_y + item.bolt_Fy_prim*elem.scale"
          :stroke-dasharray="4"
          marker-end="url(#arrow)"
          style="stroke:gray;stroke-width:1" />
      </template>

      // This is just to accomodate different naming convention for boltInline component. To be rewritten to be reusable
      <template v-if="elem.type=='arrows_inline_sec' && elem.shown==true ">
        <line v-for="item in elem.items"
          :x1="item.bolt_x"
          :y1="item.bolt_y"
          :x2="item.bolt_x + item.bolt_Fx_sec*elem.scale"
          :y2="item.bolt_y + item.bolt_Fy_sec*elem.scale"
          :stroke-dasharray="4"
          marker-end="url(#arrow)"
          style="stroke:gray;stroke-width:1" />
      </template>

      // This is just to accomodate different naming convention for boltInline component. To be rewritten to be reusable
      <template v-if="elem.type=='arrows_inline_tot' && elem.shown==true ">
        <line v-for="item in elem.items"
          :x1="item.bolt_x"
          :y1="item.bolt_y"
          :x2="item.bolt_x + item.bolt_Fx_total*elem.scale"
          :y2="item.bolt_y + item.bolt_Fy_total*elem.scale"
          marker-end="url(#arrow)"
          style="stroke:gray;stroke-width:2" />
      </template>

      // This is LABELS rendering
      <template v-if="elem.type=='labels' ">
        <text v-for="item in elem.items"
          :x="item.x+10" :y="item.y+10" fill="gray">{{item.id}}</text>
      </template>

    </template>







    </svg>

    <br>
    SCG size : {{width}}, {{height}}<br>
    View Box : {{view}}<br>
    Is pressed: {{isPressed}}<br>
    X: {{xPos}}
    Y: {{yPos}}<br>
    pos0: {{pos0}}<br>
    pos1: {{pos1}}<br>
    vector_x:  {{vector_x}}<br>
    Viewport Scale: {{scale}}<br>
    Wheel Counter: {{wheel}}<br>
    Width: {{width_real}}
    Height: {{height_real}}


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
      width_real:100,
      height_real:100,

    }
  },
  methods:{

    onwheel(e){
      document.documentElement.style.overflow = 'hidden'
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
    },
    mouseLeave(){
      document.documentElement.style.overflow = 'overlay'
    },
    mouseEnter(){
      document.documentElement.style.overflow = 'hidden'
    }

  },

  computed: {

    scale: function(){
      return [this.view[2]/Math.min(this.height_real,this.width_real),this.view[3]/Math.min(this.height_real,this.width_real)];
    }

  },

  props: {

    width: {
      type: Number,
      default: 200,
      required: false
    },
    height: {
      type: Number,
      default: 200,
      required: false
    },
    elements:{
      type: Array,
      default:[],
      required: false
    },
    coordinate_sys:{
      default:false,
      required: false
    }

  },

  mounted: function () {
    var svg1 = document.getElementById('svg1');
    this.width_real = svg1.clientWidth;
    this.height_real = svg1.clientHeight;
  }

}
</script>

<style>
svg {
  cursor: move;
}
svg text{
   -webkit-user-select: none;
   -moz-user-select: none;
   -ms-user-select: none;
   user-select: none;
}

</style>
