<template>
  <div>
    <div class="col-2 col-s-1"></div>
    <div class="col-8 col-s-10">
      <component v-bind:is="active_component"></component>
    </div>

    <div class="col-2 col-s-1"></div>


  </div>
</template>

<script>
import CrossSections_I_shape from './sections/CrossSections_I_shape';


export default {
  name: 'CrossSections',
  components: {
    'CrossSections_I_shape': CrossSections_I_shape,

  },
  data () {
    return {
      active_component: 'CrossSections_I_shape',

    }
  }
}
</script>

<style scoped>

</style>
