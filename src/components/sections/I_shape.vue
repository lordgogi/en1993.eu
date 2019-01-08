<template>
  <div>
    <CrossSectionsHelper>

      <div slot="title">Cross Section Properties - I-Section</div>
      <div slot="subtitle">Calculator calculates Cross-Sectional properties - both elastic and plastic of I-Beam Cross-section</div>

      <div slot="inputs">
          <div>
            <div class="input-label-50px">b:</div>
            <input class="output" type="number" min="0" v-model="b" style="width: 100px; display: inline-block"/>
            <div class="input-label">{{units}}</div>
          </div>
          <div>
            <div class="input-label-50px">h:</div>
            <input class="output" type="number" min="0" v-model="h" style="width: 100px; display: inline-block"></input>
            <div class="input-label">{{units}}</div>
          </div>
          <div>
            <div class="input-label-50px">t<sub>w</sub>:</div>
            <input class="output" type="number" min="0" v-model="t_w" style="width: 100px; display: inline-block"></input>
            <div class="input-label">{{units}}</div>
          </div>
          <div>
            <div class="input-label-50px">t<sub>f</sub>:</div>
            <input class="output" type="number" min="0" v-model="t_f" style="width: 100px; display: inline-block"></input>
            <div class="input-label">{{units}}</div>
          </div>
          <br>
          <button v-on:click="submitBasic" class="button_submit">CALCULATE</button>
      </div>

      <div slot="picture">
        <img alt="Cross Section I-beam" src="../../assets/legend-i-section.png">
      </div>


      <div slot="outputs">
        <div v-for="item in result">
          <div class="input-label-50px">{{item.label}}<sub>{{item.label_sub}}</sub>:</div>
          <div class="input-label-100px">{{item.value}}</div>
          <div class="input-label-50px">{{item.unit}}<sup>{{item.unit_pow}}</sup></div>
          <div class="input-label">{{item.description}}</div>
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
  name: 'I_shape',
  components:{
    'CrossSectionsHelper': CrossSectionsHelper,
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

<style>

.input-label-50px{
  width: 50px;
  display: inline-block;
  font-family: Metropolis Regular;
  color: #565656;
  font-size: 14px;
  letter-spacing: normal;

}

.input-label-100px{
  width: 100px;
  display: inline-block;
  font-family: Metropolis Regular;
  color: #565656;
  font-size: 14px;
  letter-spacing: normal;

}

.input-label{
  display: inline-block;
  font-family: Metropolis Regular;
  color: #565656;
  font-size: 14px;
  letter-spacing: normal;

}

</style>
