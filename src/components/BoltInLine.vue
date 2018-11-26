<template>
  <div>

    <div class="row">

      <div class="col-2 col-s-0"></div>

      <div class="col-4 col-s-5">
        <div class="card">

          <h4>BOLTS</h4>
          <button type="button" v-on:click="addNewBolt">
              Add Bolt
          </button>


          <div v-for="(bolt, index) in bolts">
            {{index}}
            <input v-model.number.lazy="bolt.x" style="max-width: 100px" type="number">
            <input v-model.number.lazy="bolt.y" style="max-width: 100px" type="number">
            <button type="button" v-on:click="removeBolt(index)"> Remove </button>

            <select v-model="bolt.type">
              <option v-for="bolt in bolt_sizes" v-bind:value="bolt">
                {{ bolt }}
              </option>
            </select>

            <select v-model="bolt.grade">
              <option v-for="bolt in bolt_grades" v-bind:value="bolt">
                {{ bolt }}
              </option>
            </select>

          </div>

          <h4>LOADS</h4>

          <button type="button" v-on:click="addNewForce">
              Add Force
          </button>

          <button type="button" v-on:click="addNewMoment">
              Add Moment
          </button>

          <div v-for="(load, index) in loads">

            {{index}}
            {{load.type}}
            <input v-model.number.lazy="load.magnitude" style="max-width: 100px" type="number">
            <input v-if="load.type == 'force'" v-model.number.lazy="load.x" style="max-width: 100px" type="number">
            <input v-if="load.type == 'force'" v-model.number.lazy="load.y" style="max-width: 100px" type="number">
            <input v-if="load.type == 'force'" v-model.number.lazy="load.angle" style="max-width: 100px" type="number">
            <button type="button" v-on:click="removeLoad(index)"> Remove </button>

          </div>


        </div>

        <div v-for="(bolt, index) in bolts">
          {{bolt}}
        </div>
        <br><br>
        <div v-for="(load, index) in loads">
          {{load}}
        </div>
        <button v-on:click="submitToApi">Submit</button>


        <div v-for="item in result">
          <div class="input-label-50px">{{item.label}}<sub>{{item.label_sub}}</sub>:</div>
          <div class="input-label-100px">{{item.value}}</div>
          <div class="input-label-50px">{{item.unit}}<sup>{{item.unit_pow}}</sup></div>
          <div class="input-label">{{item.description}}</div>
        </div>



        <br><br>
        {{viewboxSize}}
      </div>

      <div class="col-4 col-s-5">
        <div class="card">
          <svg  width="100%" height="600" v-bind:viewBox="viewboxSize" style="background: grey">
            <circle v-for="(item, index) in bolts" :cx="item.x" :cy="item.y" :r="16"/>
            <line v-for="(item, index) in loads" :x1="item.x" :y1="item.y" :x2="parseFloat(item.x)+parseFloat(item.magnitude)*Math.cos(parseFloat(item.angle)*(Math.PI/180))" :y2="parseFloat(item.y)+parseFloat(item.magnitude)*Math.sin(parseFloat(item.angle)*(Math.PI/180))" style="stroke:rgb(255,0,0);stroke-width:2"/>
          </svg>
           iuewg lsiuvg alsuv alsdv asdhf slduvh vluhas vluash vasuh dviaushd vlashd vlas vhdals dhas dhvalsu hvasliu hvsildu hvasliduvh asldiuvh asliduh alisuvh sdliuvh aslidu hlivuha sdlviusa dhvliuh liuh liuh l
       </div>
      </div>

      <div class="col-2 col-s-0"></div>

    </div>




  </div>
</template>

<script>
import axios from 'axios'
import { API_path } from '../variables.js'

export default{
  name: 'BoltInLine',
  components:{

  },
  data(){
    return{
      bolt_sizes:["M16", "M20"],
      bolt_grades:["8.8", "10.9"],
      selected:"",
      result:"",
      bolts:[
        {
        id:0,
        x:75,
        y:90,
        type:"M16",
        grade:"8.8"
      },
      {
        id:1,
        x:150,
        y:90,
        type:"M16",
        grade:"8.8"
      },
      {
        id:2,
        x:75,
        y:160,
        type:"M16",
        grade:"8.8"
      },
      {
        id:3,
        x:150,
        y:160,
        type:"M16",
        grade:"8.8"
      }
    ],

    loads:[
      {
        type:"force",
        magnitude:2000,
        x:250,
        y:90,
        angle:30
      },
    ]
    }
  },

  methods:{

    addNewBolt(){
      this.bolts.push({
        x:20,
        y:20,
        type:"M16",
        grade:"8.8"
      })
    },

    addNewForce(){
      this.loads.push({
        type:"force",
        magnitude:50,
        x:250,
        y:90,
        angle:45
      })
    },

    addNewMoment(){
      this.loads.push({
        type:"moment",
        magnitude:2000
      })
    },

    removeBolt: function (index) {
      this.$delete(this.bolts, index);
    },

    removeLoad: function (index) {
      this.$delete(this.loads, index);
    },

    getBoltInfo(){
      axios.get(API_path + 'get-bolt-options')
      .then(response => {
        this.bolt_sizes = response.data[0],
        this.bolt_grades = response.data[1]
      })
      .catch(error => {
        console.log(error)
      })
    },

    getJSON : function(){
       return {
           "type": "In-line",
           "bolts": this.bolts,
           "loads": this.loads
       }
    },

    submitToApi () {
          this.submited = true
           axios.post(API_path + 'get-bolt-inline-result', this.getJSON())
           .then(response => {this.result = response.data})
           .catch(error => {
             console.log(error)
           })
       }



  },

  computed:{
    viewboxSize: function () {
      let max_x = -100;
      let max_y = -100;
      let min_x = 100;
      let min_y = 100;

      for(let i = 0; i < this.loads.length; i++){

        if (this.loads[i].x > max_x) {
          max_x = this.loads[i].x
        }

        if (this.loads[i].y > max_y) {
          max_y = this.loads[i].y
        }

        if (this.loads[i].x < min_x) {
          min_x = this.loads[i].x
        }

        if (this.loads[i].y < min_y) {
          min_y = this.loads[i].y
        }

      };

      for(let i = 0; i < this.bolts.length; i++){

        if (this.bolts[i].x > max_x) {
          max_x = this.bolts[i].x
        }

        if (this.bolts[i].y > max_y) {
          max_y = this.bolts[i].y
        }

        if (this.bolts[i].x < min_x) {
          min_x = this.bolts[i].x
        }

        if (this.bolts[i].y < min_y) {
          min_y = this.bolts[i].y
        }

      };

      return [min_x-50,min_y-50,max_x+50,max_y+50]
    }
  },
    created: function() {
      this.getBoltInfo();
  }
}

</script>
<style>

.card {
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: 0.3s;
    width: 100%;
    background-color: white;
    padding: 10px;
}

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
