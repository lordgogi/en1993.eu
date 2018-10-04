<template>
  <div class="hello">
    <br>{{msg}}<br><br>
    <button @click="getResults">GET</button>
    <button @click="getResults2">POST</button>
    <br>{{test}}<br><br>
    <br>{{result}}<br><br>
  </div>
</template>

<script>

import axios from 'axios'
import { API_path } from '../variables.js'

export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      result:'',
      test:	{
        	    "language" : "Python",
        	    "framework" : "Flask",
        	    "website" : "Scotch",
        	    "version_info" : {
        	        "python" : 3.4,
        	        "flask" : 0.12
        	    },
        	    "examples" : ["query", "form", "json"],
        	    "boolean_test" : true
        	},
    }
  },
  methods:{

    getResults () {
            axios.get(API_path)
            .then(response => {this.result = response.data})
            .catch(error => {
              console.log(error)
            })
        },

    getResults2 () {
           axios.post(API_path + 'json-example', this.test)
           .then(response => {this.result = response.data})
           .catch(error => {
             console.log(error)
           })
       }

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

</style>
