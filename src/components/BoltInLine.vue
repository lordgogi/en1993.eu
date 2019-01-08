<template>
  <div>

    <div class="row">

      <div class="col-1 col-s-0"></div>

      <!-- INPUTS -->

      <div class="col-4 col-s-5">

        <div class="card">

          <!-- 1. BOLTS TYPE -->

          <h4>1. SPECIFY TYPE OF BOLTS</h4>

          <p class="p3">
            <span style="padding-left:70px;padding-right:20px">Bolt size:</span>
            <select v-model="selected_bolt_type">
              <option v-for="bolt in bolt_sizes" v-bind:value="bolt">
                {{ bolt }}
              </option>
            </select>
            <span style="padding-left:70px;padding-right:20px">Bolt grade:</span>
            <select v-model="selected_bolt_grade">
              <option v-for="bolt in bolt_grades" v-bind:value="bolt">
                {{ bolt }}
              </option>
            </select>
          </p>

          <!-- 2. BOLTS THEMSELVES -->

          <h4 style="display: inline-block; padding-right:20px">2. ADD BOLTS</h4>

          <button class="button" type="button" v-on:click="addNewBolt"> + Add Bolt</button><br>

          <div class="input-label-50px" style="text-align:center">ID:</div>
          <div class="input-label-100px" style="text-align:center">X [mm]</div>
          <div class="input-label-100px" style="text-align:center">y [mm]</div>
          <div class="input-label-50px" style="text-align:center"></div><br><br>


          <div v-for="(bolt, index) in bolts">
            <div class="input-label-50px" style="text-align:center">{{bolt.id}}</div>
            <div class="input-label-100px" ><input v-model.number="bolt.x" style="max-width: 100px" type="number"></div>
            <div class="input-label-100px"><input v-model.number="bolt.y" style="max-width: 100px" type="number"></div>
            <button class="button_del" type="button" v-on:click="removeBolt(index)"> delete </button>
          </div>

          <!-- 3. LOADING -->

          <h4 style="display: inline-block; padding-right:20px">3. ADD LOADS</h4>
          <button class="button" type="button" v-on:click="addNewForce">+ Add Force</button>
          <button class="button" type="button" v-on:click="addNewMoment">+ Add Moment</button><br>

          <div class="input-label-50px" style="text-align:center">ID:</div>
          <div class="input-label-100px" style="text-align:center">type:</div>
          <div class="input-label-100px" style="text-align:center">Magnitude [N]</div>
          <div class="input-label-50px" style="text-align:center">X [mm]</div>
          <div class="input-label-50px" style="text-align:center">Y: [mm]</div>
          <div class="input-label-50px" style="text-align:center">Angle: [deg]</div>

          <div v-for="(load, index) in loads">
            <div class="input-label-50px" style="text-align:center">{{index}}</div>
            <div class="input-label-100px" style="text-align:center">{{load.type}}</div>
            <div class="input-label-100px" style="text-align:center"><input v-model.number.lazy="load.magnitude" style="max-width: 100px" type="number"></div>
            <div class="input-label-50px" style="text-align:center"><input v-if="load.type == 'force'" v-model.number="load.x" style="max-width: 100px" type="number"></div>
            <div class="input-label-50px" style="text-align:center"><input v-if="load.type == 'force'" v-model.number="load.y" style="max-width: 100px" type="number"></div>
            <div class="input-label-50px" style="text-align:center"><input v-if="load.type == 'force'" v-model.number.lazy="load.angle" style="max-width: 100px" type="number"></div>
            <button class="button_del" type="button" v-on:click="removeLoad(index)"> Remove </button>
          </div>
          <br>
          <button v-on:click="submitToApi" class="button_submit">CALCULATE</button>
        </div>
        <br>

        <div class="card">

          <h4>RESULTS</h4>
          {{bolt_radius}}

          <div class="input-label-100px">C<sub>x</sub>:</div> <div class="input-label-100px">{{result.centroid_x}}</div>  <div class="input-label-50px">mm</div> <div class="input-label"> Centroid position in X</div><br>
          <div class="input-label-100px">C<sub>y</sub>:</div> <div class="input-label-100px">{{result.centroid_y}}</div>  <div class="input-label-50px">mm</div> <div class="input-label"> Centroid position in Y</div><br>
          <div class="input-label-100px">F<sub>x,total</sub>:</div> <div class="input-label-100px">{{result.total_Fx_prim}}</div>  <div class="input-label-50px">N</div> <div class="input-label"> Primary shear  in X</div><br>
          <div class="input-label-100px">F<sub>y,total</sub>:</div>  <div class="input-label-100px">{{result.total_Fy_prim}}</div> <div class="input-label-50px">N</div> <div class="input-label"> Primary shear  in Y</div><br>

          <div v-for="bolt in result['bolts']">
            <p class="p5">
              <div class="input-label-50px">F<sub>x</sub><sup>'</sup>:</div> <div class="input-label-100px">{{bolt.bolt_Fx_prim}}</div>  <div class="input-label-50px">N</div> <div class="input-label"> Primary shear  in X</div><br>
              <div class="input-label-50px">F<sub>y</sub><sup>'</sup>:</div>  <div class="input-label-100px">{{bolt.bolt_Fy_prim}}</div> <div class="input-label-50px">N</div> <div class="input-label"> Primary shear  in Y</div><br>
              <div class="input-label-50px">F<sub>x</sub><sup>''</sup>:</div> <div class="input-label-100px"> {{bolt.bolt_Fx_sec}}</div> <div class="input-label-50px">N</div> <div class="input-label"> Secondary shear  in X</div><br>
              <div class="input-label-50px">F<sub>y</sub><sup>''</sup>:</div> <div class="input-label-100px"> {{bolt.bolt_Fy_sec}}</div> <div class="input-label-50px">N</div> <div class="input-label"> Secondary shear  in Y</div><br>
              <div class="input-label-50px">F<sub>x</sub>:</div> <div class="input-label-100px">{{bolt.bolt_Fx_total}}</div><div class="input-label-50px">N</div> <div class="input-label"> Total shear  in X</div><br>
              <div class="input-label-50px">F<sub>y</sub>:</div> <div class="input-label-100px">{{bolt.bolt_Fy_total}}</div><div class="input-label-50px">N</div> <div class="input-label"> Total shear  in Y</div><br>
            </p>
            <br>
          </div>

        </div>

      </div>

      <!-- SVG  -->

      <div class="col-6 col-s-5">
        <div class="card">
          Show Primary shear:<input type="checkbox" id="checkbox_primary" v-model="shown_primary_shear">
          Show Secondary shear:<input type="checkbox" id="checkbox_secondary" v-model="shown_secondary_shear">
          Show Total shear:<input type="checkbox" id="checkbox_total" v-model="shown_total_shear">

            <SvgGraph

              :height="450"

              :elements="[
                {
                  items:this.bolts,
                  type:'circles',
                  color:'black',
                  radius:this.bolt_radius,
                  shown:true
                },
                {
                  items:this.bolts,
                  type:'labels',
                  shown:true
                },
                {
                  items:this.result.bolts,
                  type:'arrows_inline_prim',
                  shown:this.shown_primary_shear,
                  scale:this.forces_scale
                },
                {
                  items:this.result.bolts,
                  type:'arrows_inline_sec',
                  shown:this.shown_secondary_shear,
                  scale:this.forces_scale
                },
                {
                  items:this.result.bolts,
                  type:'arrows_inline_tot',
                  shown:this.shown_total_shear,
                  scale:this.forces_scale
                },
                {
                  items:this.loads,
                  type:'arrows',
                  shown:true,
                  scale:this.forces_scale
                },
                {
                  items:this.centroid_pos,
                  type:'circles',
                  color:'blue',
                  radius:2,
                  shown:true
                  }
                ]"

              :coordinate_sys="true"
            />

        </p>
       </div>
      </div>

      <div class="col-1 col-s-0"></div>

    </div>

  </div>
</template>

<script>
import axios from 'axios'
import { API_path } from '../variables.js'
import SvgGraph from './SvgGraph'

export default{
  name: 'BoltInLine',
  components:{

  },
  data(){
    return{
      bolt_sizes:["M16", "M20"],
      bolt_grades:["8.8", "10.9"],
      selected_bolt_type:"M12",
      selected_bolt_grade:"8.8",
      result:"",
      shown_primary_shear:true,
      shown_secondary_shear:true,
      shown_total_shear:true,
      primary_total:"false",
      secondary_total:"false",
      total:"false",
      bolts:[
        {
          id:1,
          x:-50,
          y:50,
        },
        {
          id:2,
          x:-50,
          y:-50,
        },
        {
          id:3,
          x:50,
          y:50,
        },
        {
          id:4,
          x:50,
          y:-50,
        },
        {
          id:5,
          x:50,
          y:150,
        },
        {
          id:6,
          x:-50,
          y:150,
        }
    ],

    loads:[
      {
        type:"force",
        magnitude:2000,
        x:200,
        y:90,
        angle:270
      },
    ]
    }
  },

  computed: {
    centroid_pos: function () {
      if (this.result != "")
      {
        return [
          {
            x:this.result.centroid_x,
            y:this.result.centroid_y
          }
        ]
      }
    },

    forces_scale: function () {
      return 0.1
    },

    bolt_radius: function () {
      var splitted = this.selected_bolt_type.split("").splice(-2)
      return parseInt(splitted.join(""))/2
    }
  },

  methods:{

    addNewBolt(){
      this.bolts.push({
        id:this.bolts.length+1,
        x:20,
        y:20,
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

    reorderBolts: function(){
      var x;
      for (x in this.bolts) {
        this.bolts[x].id = parseInt(x)+1;
      }
    },

    removeBolt: function (index) {
      this.$delete(this.bolts, index);
      this.reorderBolts()
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
           "loads": this.loads,
           "grade": this.selected_bolt_grade,
           "size": this.selected_bolt_type
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

  mounted: function() {
    this.getBoltInfo();
  },

  components: {
    SvgGraph
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
.button {
    background-color: #007CBB;
    border: none;
    color: white;
    font-family: Metropolis Regular;
    padding: 6px 12px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 13px;
    border-radius: 6px;
}
.button_del {
    background-color: #E62700;
    border: none;
    color: white;
    font-family: Metropolis Regular;
    padding: 5px 5px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 10px;
    border-radius: 6px;
}
input {
    width: 100%;
}


</style>
