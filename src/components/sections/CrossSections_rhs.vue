<template>
  <div>
    <CrossSectionsHelper>
      <div slot="inputs">


        <div style="display: inline-block; vertical-align: text-top;">

          <div style="padding:5px">
            <div style="width: 30px; display: inline-block">b:</div>
            <input type="number" v-model="b" style="width: 100px; display: inline-block"/>
            mm
          </div>

          <div style="padding:5px">
            <div style="width: 30px; display: inline-block">h:</div>
            <input type="number" v-model="h" style="width: 100px; display: inline-block"></input>
            mm
          </div>

          <div style="padding:5px">
            <div style="width: 30px; display: inline-block">t<sub>h</sub>:</div>
            <input type="number" v-model="t_h" style="width: 100px; display: inline-block"></input>
            mm
          </div>

          <div style="padding:5px">
            <div style="width: 30px; display: inline-block">t<sub>b</sub>:</div>
            <input type="number" v-model="t_b" style="width: 100px; display: inline-block"></input>
            mm
          </div>

          <button v-on:click="submitBasic">Submit</button>

        </div>

        <div style="display: inline-block; vertical-align: text-top;">
          <img alt="RHS-section" src="../../assets/legend-rhs.png">
        </div>


      </div>


      <div slot="outputs">
        <ul>
          <li v-for="item in result">
            <div class="output" style="width: 50px;">{{item.label}}:</div>
            <div class="output" style="width: 150px;">{{item.value}}</div>
            <div class="output" style="width: 50px;">{{item.unit}}</div>
            <div class="output">{{item.description}}</div>
          </li>
        </ul>
      </div>

    </CrossSectionsHelper>
  </div>
</template>

<script>
import CrossSectionsHelper from './CrossSectionsHelper.vue';
import axios from 'axios'
import { API_path } from '../../variables.js'

export default{
  name: 'CrossSections_I_shape',
  components:{
    'CrossSectionsHelper': CrossSectionsHelper
  },
  data(){
    return{
      b:200,
      h:400,
      t_h:8,
      t_b:12,
      result:''
    }
  },
  methods:{
    submitBasic () {
           axios.post(API_path + 'json-example', this.getJSON())
           .then(response => {this.result = response.data})
           .catch(error => {
             console.log(error)
           })
       },
       getJSON : function(){
          return [
                  {
                   "material": "S355",
                   "type": "rectangle",
                   "coordinates": {
                     "x_1": -this.b/2,
                     "y_1": this.h/2,
                     "x_2": this.b/2,
                     "y_2": this.h/2-this.t_h
                   }
                 },
                 {
                   "material": "S355",
                   "type": "rectangle",
                   "coordinates": {
                     "x_1": -this.b/2,
                     "y_1": this.h/2-this.t_h,
                     "x_2": -this.b/2+this.t_b,
                     "y_2": -this.h/2+this.t_h
                   }
                 },
                  {
                   "material": "S355",
                   "type": "rectangle",
                   "coordinates": {
                     "x_1": this.b/2-this.t_b,
                     "y_1": this.h/2-this.t_h,
                     "x_2": this.b/2,
                     "y_2": -this.h/2+this.t_h
                   }
                 },
                 {
                  "material": "S355",
                  "type": "rectangle",
                  "coordinates": {
                    "x_1": -this.b/2,
                    "y_1": -this.h/2+this.t_h,
                    "x_2": this.b/2,
                    "y_2": -this.h/2
                  }
                }

              ]
       }
  }

}

</script>
