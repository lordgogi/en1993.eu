<template>
  <div>
    <CrossSectionsHelper>
      <div slot="inputs">

        <div style="display: inline-block; vertical-align: text-top;">

          <input type="radio" id="one" value="mm" v-model="units">
          <label for="one" class="output" >metric</label>
          <input type="radio" id="two" value="inch" v-model="units">
          <label for="two" class="output" >US</label>
          <br>
          <br>

          <div style="padding:5px">
            <div class="output" style="width: 30px; display: inline-block">b:</div>
            <input class="output" type="number" min="0" v-model="b" style="width: 100px; display: inline-block"/>
            <div class="output">{{units}}</div>
          </div>

          <div style="padding:5px">
            <div class="output" style="width: 30px; display: inline-block">h:</div>
            <input class="output" type="number" min="0" v-model="h" style="width: 100px; display: inline-block"></input>
            <div class="output">{{units}}</div>
          </div>

          <div style="padding:5px">
            <div class="output" style="width: 30px; display: inline-block">t<sub>w</sub>:</div>
            <input class="output" type="number" min="0" v-model="t_w" style="width: 100px; display: inline-block"></input>
            <div class="output">{{units}}</div>
          </div>

          <div style="padding:5px">
            <div class="output" style="width: 30px; display: inline-block">t<sub>f</sub>:</div>
            <input class="output" type="number" min="0" v-model="t_f" style="width: 100px; display: inline-block"></input>
            <div class="output">{{units}}</div>
          </div>

          <button v-on:click="submitBasic">Submit</button>

        </div>

      </div>


      <div slot="outputs">
        <p class="p4">Basic Output:</p>
        <ul>

          <li v-for="item in result">
            <div class="output" style="width: 50px;">{{item.label}}<sub>{{item.label_sub}}</sub>:</div>
            <div class="output" style="width: 150px;">{{item.value}}</div>
            <div class="output" style="width: 50px;">{{item.unit}}<sup>{{item.unit_pow}}</sup></div>
            <div class="output">{{item.description}}</div>
          </li>
        </ul>

        <div>
          <p class="p4" v-on:click="en1993 = !en1993">Advanced EN-1993 <img alt="RHS-section" src="../../assets/Expand-Icon.png"></p>
          <div v-show="en1993">
            <input class="input_standard"></input>
            blablablablbalbalbalbalbalba
          </div>
        </div>


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
      t_w:8,
      t_f:12,
      result:'',
      units:'mm',
      submited:false,
      en1993:false
    }
  },
  methods:{
    submitBasic () {
          this.submited = true
           axios.post(API_path + 'json-example', this.getJSON())
           .then(response => {this.result = response.data})
           .catch(error => {
             console.log(error)
           })
       },
       getJSON : function(){
          return {
              "type": "I-shape",
              "h": this.h,
              "b": this.b,
              "t_f": this.t_f,
              "t_w": this.t_w
          }
       }
  },

}

</script>
