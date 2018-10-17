<template>
  <div>
    <CrossSectionsHelper>
      <div slot="inputs">


        <div style="display: inline-block; vertical-align: text-top;">

          <div style="padding:5px">
            <div style="width: 30px; display: inline-block">b:</div>
            <input type="number" style="width: 100px; display: inline-block"></input>
            mm
          </div>

          <div style="padding:5px">
            <div style="width: 30px; display: inline-block">h:</div>
            <input type="number" style="width: 100px; display: inline-block"></input>
            mm
          </div>

          <div style="padding:5px">
            <div style="width: 30px; display: inline-block">t<sub>w</sub>:</div>
            <input type="number" style="width: 100px; display: inline-block"></input>
            mm
          </div>

          <div style="padding:5px">
            <div style="width: 30px; display: inline-block">t<sub>f</sub>:</div>
            <input type="number" style="width: 100px; display: inline-block"></input>
            mm
          </div>

        </div>

        <div style="display: inline-block; vertical-align: text-top;">
          <img alt="RHS-section" src="../../assets/legend-i-section.png">
        </div>


      </div>


      <h3 slot="outputs">Here is the Output slot</h3>
    </CrossSectionsHelper>
  </div>
</template>

<script>
import CrossSectionsHelper from './CrossSectionsHelper.vue';

export default{
  components:{
    'CrossSectionsHelper': CrossSectionsHelper
  },
  data(){
    return{

    }
  },
  methods:{

  }
}

</script>
