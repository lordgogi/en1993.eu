<template>
  <div id="app">
    <NavBar></NavBar>
    <div class="app_content">
      <router-view/>
    </div>
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
    background: #F9F9F9;
    display: block;
}

body{
    margin:0;
    font-family:"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";
    text-align:left;
}

.app_content {
  width: 1000px;
  margin: 0 auto;
  text-align: center;

}
</style>
