<template>
  <div>
    <div class="cont">
      <div class="row">

        <div class="card" style="width: 400px;">
          <div class="card-header" style="padding: 5px;">
            <h6 style="margin:0px;">Select a predefined shape:</h6>
          </div>
          <img v-on:click="active_component='CrossSections_I_shape'" alt="I-section" src="../assets/icon-i-section-32.png">
          <img v-on:click="active_component='CrossSections_rhs'" alt="RHS-section" src="../assets/icon-rhs-32.png">
          <img alt="RHS-section" src="../assets/icon-u-shape-32.png">
          <img alt="RHS-section" src="../assets/icon-l-shape-32.png">
          <img alt="RHS-section" src="../assets/icon-plate-stiff-32.png">
          <img alt="RHS-section" src="../assets/icon-t-stiff-32.png">
          <img alt="RHS-section" src="../assets/icon-l-stiff-32.png">
        </div>

        <div class="card" style="width: 150px;">
          <div class="card-header" style="padding: 5px;">
            <h6 style="margin:0px;">Or standard profile:</h6>
          </div>
          <img alt="I-section" src="../assets/icon-en-32.png">
          <img alt="RHS-section" src="../assets/icon-aisc-32.png">
        </div>

        <div class="card" style="width: 200px;">
          <div class="card-header" style="padding: 5px;">
            <h6 style="margin:0px;">Or build custom profile:</h6>
          </div>
          <img alt="I-section" src="../assets/icon-custom-32.png">

        </div>

      </div>
      <component v-bind:is="active_component"></component>

    </div>
  </div>
</template>

<script>
import CrossSections_I_shape from './sections/CrossSections_I_shape';
import CrossSections_rhs from './sections/CrossSections_rhs';

export default {
  name: 'CrossSections',
  components: {
    'CrossSections_I_shape': CrossSections_I_shape,
    'CrossSections_rhs': CrossSections_rhs,
  },
  data () {
    return {
      active_component: 'CrossSections_I_shape',

    }
  }
}
</script>
