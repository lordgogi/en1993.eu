<template>
  <div>

    <div class="row">
      <div class="col-12 col-s-12"><SectionsNavBar></SectionsNavBar></div>
    </div>

    <div class="row">
      <div class="col-12 col-s-12" style="text-align: center"><h1><slot name="title"></slot></h1></div>
    </div>

    <div class="row">
      <div class="col-12 col-s-12" style="text-align: center"><p class="p1>"<slot name="subtitle"></slot></p></div>
    </div>

    <div class="row">

      <div class="col-2 col-s-1"></div>

      <div class="col-4 col-s-5">
        <div class="card">
          <h3>Inputs:</h3>
          <div style="display:inline-block;width:48%; text-align: center; vertical-align:middle;"><slot name="inputs"></slot></div>
          <div style="display:inline-block;width:48%; text-align: center; vertical-align:middle;"><slot name="picture"></slot></div>
        </div>
      </div>

      <div class="col-4 col-s-5">
        <div class="card">
          <h3>Outputs:</h3>
          <slot name="outputs"></slot>
        </div>
      </div>

      <div class="col-2 col-s-1"></div>

    </div>

  </div>
</template>

<script>
import SectionsNavBar from './SectionsNavBar.vue';

export default{
  components:{
    'SectionsNavBar': SectionsNavBar,
  },
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


</style>
