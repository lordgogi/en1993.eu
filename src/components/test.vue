<template>
  <div>
    <button v-on:click="funcion1">Fit All</button>
    <svg  width="1000" height="600" id="uhlo" style="background: #808080">
      <text class="label" id="country-name" x="10" y="390"> </text>
    </svg>
  </div>
</template>

<script>

export default{
  name: 'test',
  components:{

  },
  data(){
    return{
      bolt_sizes:"M16",
    }
  },

  methods:{

    funcion1(){
      document.getElementById('uhlo').getElementById('country-name').firstChild.data = "sdcsdc";
    }

  },

  computed:{

  },



}

</script>
