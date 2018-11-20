<template>
  <div>
    <CrossSectionsHelper>

      <div slot="title">Cross Section Properties - L-profile stiffened plate-Section</div>
      <div slot="subtitle">Calculator calculates Cross-Sectional properties - both elastic and plastic of Plate stiffenned with L-profile</div>

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
            <div class="input-label-50px">t<sub>b</sub>:</div>
            <input class="output" type="number" min="0" v-model="t_b" style="width: 100px; display: inline-block"></input>
            <div class="input-label">{{units}}</div>
          </div>
          <div>
            <div class="input-label-50px">t<sub>h</sub>:</div>
            <input class="output" type="number" min="0" v-model="t_h" style="width: 100px; display: inline-block"></input>
            <div class="input-label">{{units}}</div>
          </div>
          <button v-on:click="submitBasic">Submit</button>
      </div>

      <div slot="picture">
        <img alt="Cross Section I-beam" src="../../assets/legend-plate-stiff.png">
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
  name: 'PlateStiffShape',
  components:{
    'CrossSectionsHelper': CrossSectionsHelper,
  },
  data(){
    return{
      b:400,
      h:150,
      t_b:5,
      t_h:10,
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
              "type": "plate-stiff-shape",
              "b": this.b,
              "h": this.h,
              "t_b": this.t_b,
              "t_h": this.t_h
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
