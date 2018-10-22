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

h1 {
  font-family: Metropolis Light;
  color: #000000;
  font-size: 32px;
  font-weight: lighter;
  letter-spacing: normal
}

h2 {
  font-family: Metropolis Light;
  color: #000000;
  font-size: 28px;
  font-weight: lighter;
  letter-spacing: normal
}

h3 {
  font-family: Metropolis Light;
  color: #000000;
  font-size: 22px;
  font-weight: lighter;
  letter-spacing: normal
}

h4 {
  font-family: Metropolis Light;
  color: #000000;
  font-size: 18px;
  font-weight: lighter;
  letter-spacing: normal
}

h5 {
  font-family: Metropolis Regular;
  color: #565656;
  font-size: 16px;
  font-weight: normal;
  letter-spacing: 0.01em
}

h6 {
  font-family: Metropolis Medium;
  color: #313131;
  font-size: 14px;
  font-weight: normal;
  letter-spacing: normal;
}

.p1 {
  font-family: Metropolis Regular;
  color: #565656;
  font-size: 14px;
  letter-spacing: normal;
}

.p2 {
  font-family: Metropolis Medium;
  color: #565656;
  font-size: 13px;
  letter-spacing: normal;
}

.p3 {
  font-family: Metropolis Regular;
  color: #565656;
  font-size: 14px;
  letter-spacing: normal;
}

.p4 {
  font-family: Metropolis Semibold;
  color: #565656;
  font-size: 12px;
  letter-spacing: normal;
}

.p5 {
  font-family: Metropolis Regular;
  color: #565656;
  font-size: 12px;
  letter-spacing: normal;
}

.card {
    border: 1px solid #d7d7d7;
    border-radius: 0.125rem;
    box-shadow: 0 0.125rem 0 0 #d7d7d7;
    background-color: #fff;
    margin-top: 1rem;
    width: 100%;
    display: inline-block;
    vertical-align: text-top;
}

.card-header {
  padding: 18px 12px;
  border-bottom: 1px solid #eee;
}

.card-footer {
  padding: 12px 18px;
  border-bottom: 1px solid #eee;
}

.card-block {
  padding: 12px 18px;
  border-bottom: 1px solid #eee;
}

.card-text {

}

.btn {
  cursor: pointer;
  border: 1px solid #0079b8;
  font-weight: 500;
  border-color: #0079b8;
  background-color: #0079b8;
  color: #FFFFFF;
}

.row {

}

.cont {
  padding: 50px;
}

.form-row {
  display: block;

}

ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
}

.output {
  display: inline-block;
  font-family: Metropolis Regular;
  color: #565656;
  font-size: 12px;
  letter-spacing: normal;
  padding: 3px;
}




</style>
