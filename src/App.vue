<template>
  <div id="app">
    <NavBar></NavBar>
    <router-view/>
  </div>
</template>

<script>
import NavBar from './components/NavBar'
export default {
  name: 'App',
  components: {
    'NavBar': NavBar
  }
}
</script>

<style>

html {
    height: 100%;
    background: #FAFAFA;
    display: block;
}

body{
    margin:0;
    font-family:"Metropolis",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";
    font-weight: 400;
}

</style>
