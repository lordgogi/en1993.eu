<template>
  <div>

    <div class="row">

      <div class="col-1 col-s-0"></div>

      <div class="col-4 col-s-5">

        <div id="config_supporting_beam" class="card">

          <h4 style="margin:10px 10px 10px 0px;">Configuration of Supported beams:</h4>

          <div style="text-align: center;">
            <span @click="beam_config_picked = 'Right'"><img v-bind:class="{ image_picked: beam_config_picked == 'Right' }" alt="Cross Section L-shape" src="../assets/beam_config_right_only.png"></span>
            <span @click="beam_config_picked = 'Both'"><img v-bind:class="{ image_picked: beam_config_picked == 'Both' }" alt="Cross Section L-shape" src="../assets/beam_config_both.png"></span>
          </div>

          <br>


          <div>
            <div class="input-label-200px">Supporting Beam:</div>
            <select v-model="selected_supporting_beam">
              <option v-for="option in beams_keys" v-bind:value="option">
                {{ option }}
              </option>
            </select>
            <select v-model="selected_supporting_material">
              <option v-for="option in materials_keys" v-bind:value="option">
                {{ option }}
              </option>
            </select>
          </div>

          <div v-if="beam_config_picked == 'Both' ">
            <div class="input-label-200px">Left Supported Beam Size:</div>
            <select v-model="selected_supported_beam_left">
              <option v-for="option in beams_keys" v-bind:value="option">
                {{ option }}
              </option>
            </select>
            <select v-model="selected_supported_material_left">
              <option v-for="option in materials_keys" v-bind:value="option">
                {{ option }}
              </option>
            </select>
          </div>

          <div>
            <div class="input-label-200px">Right Supported Beam Size:</div>
            <select v-model="selected_supported_beam_right">
              <option v-for="option in beams_keys" v-bind:value="option">
                {{ option }}
              </option>
            </select>
            <select v-model="selected_supported_material_right">
              <option v-for="option in materials_keys" v-bind:value="option">
                {{ option }}
              </option>
            </select>
          </div>

        </div>

        <div class="card" id="left_specification" v-if="beam_config_picked == 'Left' || beam_config_picked == 'Both' ">

          <h6 style="margin:10px 10px 10px 0px;">Left Supported Beam:</h6>

          Shear Load Applied:
          <input :min="1" v-model.number="shear_load_left" placeholder="edit me" type="number">
          <br>

          End plate thickness:
          <input :min="1" :max="100" v-model.number="end_plate_thck_left" placeholder="edit me" type="number">
          <br>

          End plate height:
          <input :min="1" :max="1000" v-model.number="end_plate_height_left" placeholder="edit me" type="number">
          <span v-if=" this.supported_beam_left && this.end_plate_height_left && this.end_plate_height_left < 0.6*this.supported_beam_left.h" style="color:orange">Min <b>0.6 x Supported beam depth</b> recommended</span>
          <br>

          End plate width:
          <input :min="1" :max="1000" v-model.number="end_plate_width_left" placeholder="edit me" type="number">
          <br>

          Notch height:
          <input :min="1" :max="100" v-model.number="notch_left_top" placeholder="edit me" type="number">
          <span v-if="this.selected_supporting_beam && this.supported_beam_left &&
          this.notch_left_top<this.supporting_beam.t_f+this.supporting_beam.r && this.notch_left_top" style="color:red">Value is too low</span>
          <br>

          Horizontal notch width:
          <input :min="1" :max="100" v-model.number="notch_hor_left" placeholder="edit me" type="number">
          <br>

          Weld Throat thickness Left:
          <input :min="1" :max="100" v-model.number="weld_leg_size_left" placeholder="edit me" type="number">
          <br>



        </div>

        <div class="card" id="right_specification" v-if="beam_config_picked == 'Right' || beam_config_picked == 'Both' ">

          <h4 style="margin:10px 10px 10px 0px;">Right Supported Beam</h4>

          <br>

          <div class="input-label-50px">V<sub>Ed:</sub></div>
          <div class="input-label-100px"><input :min="1" v-model.number="shear_load_right" placeholder="edit me" type="number"></div>
          <div class="input-label-50px">N</div>
          <div class="input-label">Shear Load Applied</div>

          <br>

          <div class="input-label-50px">o<sub>b:</sub></div>
          <div class="input-label-100px"><input :min="0" :max="1000" v-model.number="offset_right" placeholder="edit me" type="number"></div>
          <div class="input-label-50px">mm</div>
          <div class="input-label">Beam Vertical offset</div>

          <template v-if="this.notch_right_top_present == false && this.notch_right_bottom_present == false">
            <span v-if="this.offset_right < this.supporting_beam.t_f" style="color:red"><b>Value too low</b></span>
            <span v-if="this.offset_right + this.supported_beam_right.h > this.supporting_beam.h - this.supporting_beam.t_f" style="color:red"><b>Value too high</b></span>
          </template>


          <h6 style="margin:20px 10px 10px 0px;">Configuration of notches</h6>

          <div style="text-align: center;">
            <span v-on:click="notch_right_top_present=false; notch_right_bottom_present=false"><img v-bind:class="{ image_picked: (notch_right_top_present==false && notch_right_bottom_present==false) }" alt="Cross Section L-shape" src="../assets/beam_notch_no.png"></span>
            <span v-on:click="notch_right_top_present=true; notch_right_bottom_present=false"><img v-bind:class="{ image_picked: (notch_right_top_present==true && notch_right_bottom_present==false) }" alt="Cross Section L-shape" src="../assets/beam_notch_top.png"></span>
            <span v-on:click="notch_right_top_present=false; notch_right_bottom_present=true"><img v-bind:class="{ image_picked: (notch_right_top_present==false && notch_right_bottom_present==true)}" alt="Cross Section L-shape" src="../assets/beam_notch_bottom.png"></span>
            <span v-on:click="notch_right_top_present=true; notch_right_bottom_present=true"><img v-bind:class="{ image_picked: (notch_right_top_present==true && notch_right_bottom_present==true)}" alt="Cross Section L-shape" src="../assets/beam_notch_both.png"></span>
            <br><br>
          </div>

          <template v-if="notch_right_top_present || notch_right_bottom_present">

            <div class="input-label-50px">l<sub>n:</sub></div>
            <div class="input-label-100px"><input :min="1" :max="500" v-model.number="notch_hor_right" placeholder="edit me" type="number"></div>
            <div class="input-label-50px">mm</div>
            <div class="input-label">Notch Width</div>

            <template v-if="this.supporting_beam && this.notch_right_top_present && this.end_plate_thck_right">
              <span v-if=" this.offset_right < this.supporting_beam.t_f && this.supporting_beam.t_w/2 + this.end_plate_thck_right + this.notch_hor_right < this.supporting_beam.b/2" style="color:red"><b>Value too low</b></span>
            </template>

            <br>

            <template v-if="notch_right_top_present">
              <div class="input-label-50px">d<sub>nt:</sub></div>
              <div class="input-label-100px"><input :min="1" :max="100" v-model.number="notch_right_top" placeholder="edit me" type="number"></div>
              <div class="input-label-50px">mm</div>
              <div class="input-label">Notch Height top</div>

              <template v-if="this.supporting_beam && this.notch_right_top_present && this.end_plate_thck_right">
                <span v-if="(this.notch_right_top < this.supported_beam_right.t_f + this.supported_beam_right.r) ||
                (this.offset_right + this.notch_right_top < this.supporting_beam.t_f + this.supporting_beam.r)" style="color:red"><b>Value too low</b></span>
              </template>

              <br>

            </template>

            <template v-if="notch_right_bottom_present">
              <div class="input-label-50px">d<sub>nb:</sub></div>
              <div class="input-label-100px"><input :min="1" :max="100" v-model.number="notch_right_bottom" placeholder="edit me" type="number"></div>
              <div class="input-label-50px">mm</div>
              <div class="input-label">Notch Height bottom</div>
            </template>

            <br>



          </template>





          <h6 style="margin:20px 10px 10px 0px;">End plate</h6>

          <div class="input-label-50px">t<sub>p:</sub></div>
          <div class="input-label-100px"><input :min="1" :max="100" v-model.number="end_plate_thck_right" placeholder="edit me" type="number"></div>
          <div class="input-label-50px">mm</div>
          <div class="input-label">End-plate thickness</div>

          <br>

          <div class="input-label-50px">h<sub>p:</sub></div>
          <div class="input-label-100px"><input :min="1" :max="1000" v-model.number="end_plate_height_right" placeholder="edit me" type="number"></div>
          <div class="input-label-50px">mm</div>
          <div class="input-label">End-plate height</div>
          <span v-if=" this.supported_beam_right && this.end_plate_height_right && this.end_plate_height_right < 0.6*this.supported_beam_right.h" style="color:orange">Min <b>0.6 x Supported beam depth</b> recommended</span>

          <span v-if="this.end_plate_height_right+this.notch_right_top_computed > this.supported_beam_right.h - this.supported_beam_right.t_f - this.supported_beam_right.r" style="color:red"><b>Value too high</b></span>



          <br>

          <div class="input-label-50px">w<sub>ep:</sub></div>
          <div class="input-label-100px"><input :min="1" :max="1000" v-model.number="end_plate_width_right" placeholder="edit me" type="number"></div>
          <div class="input-label-50px">mm</div>
          <div class="input-label">End-plate width</div>

          <br>





          <h6 style="margin:20px 10px 10px 0px;">Welding</h6>

          <div class="input-label-50px">s</div>
          <div class="input-label-100px"><input :min="1" :max="100" v-model.number="weld_leg_size_right" placeholder="edit me" type="number"></div>
          <div class="input-label-50px">mm</div>
          <div class="input-label">Weld leg size</div>

          <br>


        </div>

        <div class="card" id="bolts_specification">

          <h4 style="margin:10px 10px 10px 0px;">Bolts:</h4>

          Bolt Gauge:
          <input :min="1" :max="100" v-model.number="bolt_gauge" placeholder="edit me" type="number">
          <br>

          First bolt row position from top:
          <input :min="1" :max="100" v-model.number="first_bolt_row_distance" placeholder="edit me" type="number">
          <br>

        </div>

        <button v-on:click="calculate" class="button_submit">CALCULATE</button>


      </div>

      <div class="col-6 col-s-5">

        <svg viewBox="-600 -30 1200 1000" xmlns="http://www.w3.org/2000/svg">

          <g id="supporting_beam" fill="black" stroke="green" stroke-width="0" v-if="this.supporting_beam">

            <rect
            :x="-this.supporting_beam.b/2"
            :y="0"
            :width="this.supporting_beam.b"
            :height="this.supporting_beam.t_f"/>

            <rect
            :x="-this.supporting_beam.t_w/2"
            :y="this.supporting_beam.t_f"
            :width="this.supporting_beam.t_w"
            :height="this.supporting_beam.h-2*this.supporting_beam.t_f"/>

            <rect
            :x="-this.supporting_beam.b/2"
            :y="this.supporting_beam.h-this.supporting_beam.t_f"
            :width="this.supporting_beam.b"
            :height="this.supporting_beam.t_f"/></g>

          <g fill="black" v-if="this.supporting_beam && this.supported_beam_right && this.notch_hor_right && this.end_plate_thck_right">

            <rect fill="#948981"
            :x="this.supporting_beam.t_w/2 + this.end_plate_thck_right + this.notch_hor_right_computed_top"
            :y="this.offset_right"
            :width="(total_drawn_width/2)-(this.supporting_beam.t_w/2 + this.end_plate_thck_right + this.notch_hor_right_computed_top)"
            :height="this.supported_beam_right.t_f"/>

            <rect fill="#E3DDD1"
            :x="this.supporting_beam.t_w/2 + this.end_plate_thck_right + this.notch_hor_right_computed_top"
            :y="this.supported_beam_right.t_f + this.offset_right"
            :width="(total_drawn_width/2)-(this.supporting_beam.t_w/2 + this.end_plate_thck_right + this.notch_hor_right_computed_top)"
            :height="this.supported_beam_right.r"/>

            <rect fill="#F4F1E6" v-if="this.notch_right_top_computed-this.supported_beam_right.t_f - this.supported_beam_right.r > 0"
            :x="this.supporting_beam.t_w/2 + this.end_plate_thck_right + this.notch_hor_right_computed_top"
            :y="this.offset_right + this.supported_beam_right.t_f + this.supported_beam_right.r"
            :width="(total_drawn_width/2)-(this.supporting_beam.t_w/2 + this.end_plate_thck_right + this.notch_hor_right_computed_top)"
            :height="this.notch_right_top_computed-this.supported_beam_right.t_f - this.supported_beam_right.r"/>




            <rect fill="#F4F1E6"
            :x="this.supporting_beam.t_w/2 + this.end_plate_thck_right"
            :y="this.offset_right + this.notch_right_top_computed"
            :width="(total_drawn_width/2) - (this.supporting_beam.t_w/2 + this.end_plate_thck_right) "
            :height="this.supported_beam_right.h - this.notch_right_top_computed - this.notch_right_bottom_computed "/>

            <rect fill="#948981"
            :x="this.supporting_beam.t_w/2"
            :y="this.offset_right + this.notch_right_top_computed"
            :width="this.end_plate_thck_right"
            :height="this.end_plate_height_right "/>




            <rect fill="#F4F1E6" v-if="this.notch_right_bottom_computed > this.supported_beam_right.t_f + this.supported_beam_right.r"
            :x="this.supporting_beam.t_w/2 + this.end_plate_thck_right + this.notch_hor_right_computed_bottom"
            :y="this.offset_right + this.supported_beam_right.h - this.notch_right_bottom_computed"
            :width="(total_drawn_width/2)-(this.supporting_beam.t_w/2+this.end_plate_thck_right+this.notch_hor_right_computed_bottom)"
            :height="this.notch_right_bottom_computed - this.supported_beam_right.t_f - this.supported_beam_right.r "/>

            <rect fill="#E3DDD1"
            :x="this.supporting_beam.t_w/2 + this.end_plate_thck_right + this.notch_hor_right_computed_bottom"
            :y="this.offset_right + this.supported_beam_right.h - this.supported_beam_right.t_f - this.supported_beam_right.r"
            :width="(total_drawn_width/2)-(this.supporting_beam.t_w/2+this.end_plate_thck_right+this.notch_hor_right_computed_bottom)"
            :height="this.supported_beam_right.t_f"/>

            <rect fill="#948981"
            :x="this.supporting_beam.t_w/2 + this.end_plate_thck_right + this.notch_hor_right_computed_bottom"
            :y="this.offset_right + this.supported_beam_right.h - this.supported_beam_right.t_f"
            :width="(total_drawn_width/2)-(this.supporting_beam.t_w/2+this.end_plate_thck_right+this.notch_hor_right_computed_bottom)"
            :height="this.supported_beam_right.t_f"/>






          </g>


        </svg>

        {{notch_right_top_computed}}
        {{notch_right_bottom_computed}}

        <h6 style="margin:10px 10px 10px 0px;">Results:</h6>

        <div class="card" v-for="item in results">
            <h4>{{item.card_name}}</h4>

            <template v-for="line in item.display">
              <div class="input-label-50px">{{line.property}}<sub>{{line.property_sub}}</sub>:</div>
              <div class="input-label-100px">{{line.value}}</div>
              <div class="input-label-50px">{{line.unit}}<sup>{{line.unit_pow}}</sup></div>
              <div class="input-label">{{line.description}}</div>
              <br>
            </template>

          </div>

      </div>

      <div class="col-1 col-s-0"></div>

    </div>

  </div>
</template>

<script>

import axios from 'axios'
import { API_path } from '../variables.js'

export default {

  name: 'App',

  data(){
    return{

      beam_config_picked:"Right",

      selected_supporting_beam:"UB_610x229x140",
      selected_supporting_material:"S275",
      selected_supported_beam_left:"UB_406x178x74",
      selected_supported_material_left:"S275",
      selected_supported_beam_right:"UB_533x210x92",
      selected_supported_material_right:"S275",

      shear_load_left:340000,
      shear_load_right:550000,

      offset_right:0,
      offset_left:0,

      end_plate_thck_left:10,
      end_plate_thck_right:12,
      end_plate_height_left:290,
      end_plate_height_right:430,
      end_plate_width_left:200,
      end_plate_width_right:200,

      weld_leg_size_left:6,
      weld_leg_size_right:6,

      first_bolt_row_distance:100,

      notch_right_top_present:true,
      notch_left_top_present:false,
      notch_right_bottom_present:false,
      notch_left_bottom_present:false,

      notch_left_top:50,
      notch_right_top:50,
      notch_left_bottom:50,
      notch_right_bottom:50,
      notch_hor_right:110,

      bolt_gauge:140,

      beams:"",
      beams_keys:"",
      materials:"",
      materials_keys:"",

      results:[7],

    }

  },

  created: function() {
    this.getBeamsSizes();
    this.getMaterialsOptions();

  },

  methods:{

    getBeamsSizes(){
      axios.get(API_path + 'get-beams-options')
      .then(response => {
        this.beams = response.data,
        this.beams_keys = Object.keys(response.data)

      })
      .catch(error => {
        console.log(error)
      })
    },
    getMaterialsOptions(){
      axios.get(API_path + 'get-materials-options')
      .then(response => {
        this.materials = response.data,
        this.materials_keys = Object.keys(response.data)
      })
      .catch(error => {
        console.log(error)
      })
    },
    calculate(){

      // Empty the results variables
      this.results = []

      // Right beam is there always so no conditin needed - always performed

      this.check_web_shear(this.supported_material_right.Re,1,this.supported_beam_right.t_w,this.end_plate_height_right);
      this.check_weld_size(this.weld_leg_size_right, this.supported_beam_right.t_w, this.selected_supported_material_right);
      this.check_notch_resistance_single(this.supported_beam_right.h, this.supported_beam_right.b, this.supported_beam_right.t_f, this.supported_beam_right.t_w, this.supported_beam_right.r, this.notch_right_top_computed, this.supported_material_right.Re, this.shear_load_right, this.end_plate_thck_right, this.notch_hor_right_computed_top);
      this.check_local_stability(this.notch_right_top_present, this.notch_right_bottom_present, this.supported_material_right.Re, this.notch_right_top_computed, this.notch_right_bottom_computed, this.notch_hor_right_computed_top, this.supported_beam_right.h, this.selected_supported_material_right, this.supported_beam_right.t_w);



    },
    check_weld_size(weld_leg, beam_web, material){ // Implement error handeling and S235 not implemented

      var weld_throat = weld_leg/Math.sqrt(2)
      var min_throat = 0;
      var Fos = 0;

      if(material == 'S275'){
        min_throat = 0.4* beam_web;
        Fos = weld_throat/min_throat;
      } else if(material == 'S355'){
        min_throat = 0.48* beam_web;
        Fos = weld_throat/min_throat;
      } else {
        min_throat = 0;
        Fos = 0;
      };

      this.results.push(
        {'card_name':'2. Weld Check',
          'display':
          [
            {
              'property':'a',
              'property_sub':'w',
              'value':weld_throat.toFixed(2),
              'unit':'mm',
              'unit_pow':'',
              'description':'Weld throat size',
            },
            {
              'property':'a',
              'property_sub':'min',
              'value':min_throat.toFixed(2),
              'unit':'mm',
              'description':'Minimum allowable weld throat size',
            },
            {
              'property':'FoS',
              'property_sub':'',
              'value':Fos.toFixed(2),
              'unit':'-',
              'description':'Factor of safety',
            },
          ]
        }

      );


    },
    check_web_shear(tensile_strength, gamma, web_thickness, end_plate_height){ // Deal with different Re based on thickness!

      var shear_area = web_thickness*end_plate_height*0.9 // Access steel document SN014
      var resistance = shear_area*(tensile_strength/Math.sqrt(3))/gamma

      this.results.push(
        {'card_name':'1. Web shear check',
          'display':
          [
            {
              'property':'A',
              'property_sub':'v',
              'value':shear_area.toFixed(2),
              'unit':'mm',
              'unit_pow':'2',
              'description':'Shear Area',
            },
            {
              'property':'f',
              'property_sub':'y',
              'value':tensile_strength,
              'unit':'MPa',
              'unit_pow':'',
              'description':'Web Tensile Strength',
            },
            {
              'property':'\u03B3',
              'property_sub':'M0',
              'value':gamma,
              'unit':'-',
              'unit_pow':'',
              'description':'Safety Coefficient',
            },
            {
              'property':'V',
              'property_sub':'c,Rd',
              'value':(resistance/1000).toFixed(1),
              'unit':'kN',
              'unit_pow':'',
              'description':'Design shear resistance of beam',
            },
            {
              'property':'V',
              'property_sub':'Ed',
              'value':this.shear_load_right/1000,
              'unit':'kN',
              'unit_pow':'',
              'description':'Applied load',
            },
            {
              'property':'FoS',
              'property_sub':'',
              'value':(resistance/this.shear_load_right).toFixed(2),
              'unit':'-',
              'unit_pow':'',
              'description':'Factor of Safety',
            },
          ]
        }

      );

    },
    check_notch_resistance_single(beam_h, beam_b, beam_t_f, beam_t_w, beam_r, notch, beam_tens_str, V_eD, end_pl_th, notch_width){ // Deal with different Re based on thickness!

      // Area of the Tee section
      var A_tee = (((beam_h-notch)-beam_t_f)*beam_t_w)+beam_t_f*beam_b;

      // Shear area of T section
      var A_vN = A_tee - beam_b*beam_t_f + (beam_t_w+2*beam_r)*(beam_t_f/2);

      // Shear resistance at the notch
      var V_pl_N_rd = (A_vN*beam_tens_str)/(Math.sqrt(3)*1);

      // Check if we have high or low shear condition

      var shear_condition;

      if(V_eD <= V_pl_N_rd*0.5){
        shear_condition = "low"
      } else {
        shear_condition = "high"
      }

      // Calculate position of Neutral axis from bottom of T-section

      var z = ((beam_b*beam_t_f*(beam_t_f/2))+(beam_h-notch-beam_t_f)*beam_t_w*(((beam_h-notch)/2)+beam_t_f))/((beam_b*beam_t_f)+((beam_h-notch)*beam_t_w));

      // Calculate Second moment of Inertia of T-section

      var I_yy = (((beam_b*Math.pow(beam_t_f,3))/12)+beam_b*beam_t_f*(Math.pow((z-(beam_t_f/2)),2)))+((beam_t_w*Math.pow((beam_h-notch-beam_t_f),3))/12)+(beam_h-notch-beam_t_f)*beam_t_w*Math.pow((((beam_h-notch-beam_t_f)/2)+beam_t_f-z),2);

      // Calulate maximum distance from

      var min_z = Math.max(z, beam_h-notch-z);


      // Calculate Section Modulus of T-section

      var W_el = I_yy/min_z;

      // Calculate Moment resistance of notched portion of the beam

      var M_vNRd = (beam_tens_str*W_el/1)*(1-Math.pow(((2*V_eD)/V_pl_N_rd)-1,2));

      // Calculate Eccentric Moment

      var M_ecc = V_eD*(notch_width + end_pl_th);

      // Calculate FoS

      var FoS = M_ecc/M_vNRd;


      this.results.push(
        {'card_name':'3. Notch Resistance Check',
          'display':
          [
            {
              'property':'A',
              'property_sub':'tee',
              'value':A_tee,
              'unit':'mm',
              'unit_pow':'2',
              'description':'Area of the tee section',
            },
            {
              'property':'A',
              'property_sub':'v,N',
              'value':A_vN,
              'unit':'mm',
              'unit_pow':'2',
              'description':'Shear Area of the tee section',
            },
            {
              'property':'V',
              'property_sub':'pl,N,Rd',
              'value':(V_pl_N_rd/1000).toFixed(2),
              'unit':'kN',
              'unit_pow':'',
              'description':'Shear Resistance at the notch',
            },
            {
              'property':'V',
              'property_sub':'cond',
              'value':shear_condition,
              'unit':'',
              'unit_pow':'',
              'description':'Shear relative magnitude',
            },
            {
              'property':'z',
              'property_sub':'cent',
              'value':z.toFixed(2),
              'unit':'mm',
              'unit_pow':'',
              'description':'Position of neutral line',
            },
            {
              'property':'I',
              'property_sub':'yy',
              'value':I_yy.toFixed(2),
              'unit':'mm',
              'unit_pow':'4',
              'description':'Second Moment of Inertia',
            },
            {
              'property':'z',
              'property_sub':'min',
              'value':min_z.toFixed(2),
              'unit':'mm',
              'unit_pow':'',
              'description':'Maximum distance from centroid',
            },
            {
              'property':'W',
              'property_sub':'el,N,y',
              'value':W_el.toFixed(2),
              'unit':'mm',
              'unit_pow':'3',
              'description':'Section Modulus',
            },
            {
              'property':'M',
              'property_sub':'v,N,Rd',
              'value':M_vNRd.toFixed(2),
              'unit':'Nm',
              'unit_pow':'',
              'description':'Moment resistance of notch portion',
            },
            {
              'property':'M',
              'property_sub':'ecc',
              'value':M_ecc.toFixed(2),
              'unit':'Nm',
              'unit_pow':'',
              'description':'Applied eccentric moment',
            },
            {
              'property':'FoS',
              'property_sub':'',
              'value':FoS.toFixed(2),
              'unit':'-',
              'unit_pow':'',
              'description':'Factor of safety',
            },

          ]
        }

      );

    },
    check_local_stability(top_present, bottom_present, beam_tens_str, d_nt, d_nb, l_n, h_b1, material, t_w){

      if(top_present==true && bottom_present==false){

        // Check number 1

        if(d_nt <= h_b1/2){
          var check_1 = true;
        } else {
          var check_1 = false;
        }

        // Check number 2



      } else if(top_present==false && bottom_present==true){

        var check_1 = false;

      } else if(top_present==true && bottom_present==true){

        var check_1 = false;

      }

      this.results.push(
        {'card_name':'4. Local stability Check',
          'display':
          [
            {
              'property':'Check 1',
              'property_sub':'',
              'value':check_1,
              'unit':'-',
              'unit_pow':'',
              'description':'Area of the tee section',
            },
          ]
        }

      );



    }
  },

  computed: {

    supporting_beam: function () {
      return this.beams[this.selected_supporting_beam]
    },
    supporting_material: function () {
      return this.materials[this.selected_supporting_material]
    },
    supported_beam_left: function () {
      return this.beams[this.selected_supported_beam_left]
    },
    supported_material_left: function () {
      return this.materials[this.selected_supported_material_left]
    },
    supported_beam_right: function () {
      return this.beams[this.selected_supported_beam_right]
    },
    supported_material_right: function () {
      return this.materials[this.selected_supported_material_right]
    },
    notch_right_top_computed: function () {
      if(this.notch_right_top_present == true){
        return this.notch_right_top
      } else {
        return this.supported_beam_right.t_f + this.supported_beam_right.r
      }
    },
    notch_right_bottom_computed: function () {
      if(this.notch_right_bottom_present == true){
        return this.notch_right_bottom
      } else {
        return this.supported_beam_right.t_f + this.supported_beam_right.r
      }
    },
    notch_hor_right_computed_top: function () {
      if(this.notch_right_top_present == true){
        return this.notch_hor_right
      } else {
        return 0
      }
    },
    notch_hor_right_computed_bottom: function () {
      if(this.notch_right_bottom_present == true){
        return this.notch_hor_right
      } else {
        return 0
      }
    },
    left_end_plate_drawn: function() {

      if ((this.beam_config_picked == 'Left' || this.beam_config_picked == 'Both') && this.end_plate_thck_left && this.end_plate_height_left && this.notch_left_top && this.selected_supported_beam_left && this.notch_hor_left)  {
        return true;
        } else {
        return false;
      }
    },
    right_end_plate_drawn: function() {

      if ((this.beam_config_picked == 'Right' || this.beam_config_picked == 'Both') && this.end_plate_thck_right && this.end_plate_height_right && this.notch_right_top && this.selected_supported_beam_right && this.notch_hor_right)  {
        return true;
        } else {
        return false;
      }
    },
    total_drawn_width: function () {
      return this.supporting_beam.b*2;
    },

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
    margin: 10px;
    font-size: 12px;
}
.input-label-50px{
  width: 50px;
  display: inline-block;
  font-family: Metropolis Regular;
  color: #565656;
  font-size: 12px;
  letter-spacing: normal;

}
.input-label-100px{
  width: 100px;
  display: inline-block;
  font-family: Metropolis Regular;
  color: #565656;
  font-size: 12px;
  letter-spacing: normal;

}
.input-label-150px{
  width: 150px;
  display: inline-block;
  font-family: Metropolis Regular;
  color: #565656;
  font-size: 12px;
  letter-spacing: normal;

}
.input-label-200px{
  width: 200px;
  display: inline-block;
  font-family: Metropolis Regular;
  color: #565656;
  font-size: 12px;
  letter-spacing: normal;

}
.input-label{
  display: inline-block;
  font-family: Metropolis Regular;
  color: #565656;
  font-size: 12px;
  letter-spacing: normal;

}
input {
    width: 100%;
    font-family: Metropolis Regular;
    font-size: 12px;
    margin:1px;
}
select {
  font-family: Metropolis Regular;
}
.image_picked{
  background-color: #CFC8BD
  }

</style>
