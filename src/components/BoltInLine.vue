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
            <div class="input-label-50px" style="text-align:center">{{index}}</div>
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

      <!-- VIEWPORT  -->

      <div class="col-6 col-s-5">
        <div class="card">

          <p class="p5">

            <input type="checkbox" id="primary_total" v-model="primary_total" style="width:auto">
            <label for="primary_total">Show Primary Shear</label>
            <input type="checkbox" id="secondary_total" v-model="secondary_total" style="width:auto">
            <label for="secondary_total">Show Secondary Shear</label>
            <input type="checkbox" id="total" v-model="total" style="width:auto">
            <label for="total">Show Total Shear</label>
            <button v-on:click="zoomIn">+ Zoom In</button>
            <button v-on:click="zoomOut">- Zoom Out</button>
            <button v-on:click="viewboxFitAll">Fit All</button>


        </p>

          <!-- SVG VIEWPORT -->

          <svg  width="100%" height="600" v-bind:viewBox="viewPort" style="background: #ffffff"><!-- transform-origin: 50% 50%; transform: scale(1,-1); -->
            <defs>
              <!-- arrowhead marker definition -->
              <marker id="arrow_CS" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse" :fill="colors.coordinate_system">
                <path d="M 0 0 L 10 5 L 0 10 z" />
              </marker>
              <marker id="arrow_Force" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse" :fill="colors.force">
                <path d="M 0 0 L 10 5 L 0 10 z" />
              </marker>
              <marker id="arrow_Primary" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse" :fill="colors.primary">
                <path d="M 0 0 L 10 5 L 0 10 z" />
              </marker>
              <marker id="arrow_Secondary" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse" :fill="colors.secondary">
                <path d="M 0 0 L 10 5 L 0 10 z" />
              </marker>
            </defs>

            <circle v-for="(item, index) in bolts" :cx="item.x" :cy="item.y" :r="16"/>
            <path class="button" onclick="pan(0, 25)" d="M25 5 l6 10 a20 35 0 0 0 -12 0z" />
            <circle v-if="result['centroid_x']":cx="result['centroid_x']" :cy="result['centroid_y']" :r="5"/>
            <!-- Input Forces -->
            <line v-for="(item, index) in loads" :x1="item.x" :y1="item.y" :x2="item.x+item.magnitude*Math.cos(item.angle*(Math.PI/180))*0.1" :y2="item.y-item.magnitude*Math.sin(item.angle*(Math.PI/180))*0.1" marker-end="url(#arrow_Force)" :stroke="colors.force"/>
            <!-- Primary and secondary Forces -->
            <line v-if="primary_total" v-for="(item, index) in result['bolts']" :x1="item['bolt_x']" :y1="item['bolt_y']" :x2="item['bolt_x'] - item['bolt_Fx_prim']*0.1" :y2="item['bolt_y'] - item['bolt_Fy_prim']*0.1" marker-end="url(#arrow_Primary)" :stroke="colors.primary" stroke-dasharray="4" />
            <line v-if="secondary_total" v-for="(item, index) in result['bolts']" :x1="item['bolt_x']" :y1="item['bolt_y']" :x2="item['bolt_x'] - item['bolt_Fx_sec']*0.1" :y2="item['bolt_y'] - item['bolt_Fy_sec']*0.1" marker-end="url(#arrow_Secondary)" :stroke="colors.secondary" stroke-dasharray="4" />
            <!-- Total Shear Force Forces -->
            <line v-if="total" v-for="(item, index) in result['bolts']" :x1="item['bolt_x']" :y1="item['bolt_y']" :x2="item['bolt_x'] - item['bolt_Fx_total']*0.1" :y2="item['bolt_y'] - item['bolt_Fy_total']*0.1" marker-end="url(#arrow_Primary)" :stroke="colors.primary" />
            <!-- Coordinate system Render -->
            <polyline points="10,90 10,10 90,10" fill="none" :stroke="colors.coordinate_system" marker-start="url(#arrow_CS)" marker-end="url(#arrow_CS)"  />
            <text x="0" y="0" class="small">0</text>
            <text x="90" y="0" class="small">X</text>
            <text x="0" y="90" class="small">Y</text>
          </svg>

       </div>
      </div>

      <div class="col-1 col-s-0"></div>

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
      viewPort:[-200,-200,400,400],
      selected_bolt_type:"M12",
      selected_bolt_grade:"8.8",
      colors:{
        "coordinate_system":"black",
        "force":"red",
        "primary":"gray",
        "secondary":"gray"
      },
      zoom:1,
      result:"",
      primary_total:"false",
      secondary_total:"false",
      total:"false",
      bolts:[
        {
        x:-50,
        y:50,

      },
      {
        x:-50,
        y:-50,
      },
      {
        x:50,
        y:50,
      },
      {
        x:50,
        y:-50,
      },
      {
        x:50,
        y:150,
      },
      {
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

  methods:{

    addNewBolt(){
      this.bolts.push({
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

    removeBolt: function (index) {
      this.$delete(this.bolts, index);
    },

    removeLoad: function (index) {
      this.$delete(this.loads, index);
    },

    zoomOut(){
      this.zoom += 1
    },

    zoomIn(){

      if (this.zoom > 1){
        this.zoom -= 1;
      }
    },

    viewboxFitAll: function () {

      let max_x = 0;
      let max_y = 0;
      let min_x = 0;
      let min_y = 0;

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

      for(let i = 0; i < this.loads.length; i++){

        max_x = Math.max(this.loads[i].x,this.loads[i].x+this.loads[i].x)

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

      this.viewPort  = [min_x-50, min_y-50, max_x-min_x+100, max_y-min_y+100]
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

  computed:{

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

.button_submit {
    background-color: #62A420;
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
