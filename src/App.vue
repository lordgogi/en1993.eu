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
    overflow-y: overlay;
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

* {
    box-sizing: border-box;
}

.row::after {
    content: "";
    clear: both;
    display: table;
}

[class*="col-"] {
    float: left;
    padding:4px
}

/* For mobile phones: */
[class*="col-"] {
    width: 98%;
    border-style: dashed;
    border-width: 0px;
}
@media only screen and (min-width: 650px) {
    /* For tablets: */
    .col-s-0 {width: 0%;}
    .col-s-1 {width: 8.33%;}
    .col-s-2 {width: 16.66%;}
    .col-s-3 {width: 25%;}
    .col-s-4 {width: 33.33%;}
    .col-s-5 {width: 49%;}
    .col-s-6 {width: 50%;}
    .col-s-7 {width: 58.33%;}
    .col-s-8 {width: 66.66%;}
    .col-s-9 {width: 75%;}
    .col-s-10 {width: 83.33%;}
    .col-s-11 {width: 91.66%;}
    .col-s-12 {width: 100%;}
}
@media only screen and (min-width: 1200px) {
    /* For desktop: */
    .col-1 {width: 8.33%;}
    .col-2 {width: 16.66%;}
    .col-3 {width: 25%;}
    .col-4 {width: 33.33%;}
    .col-5 {width: 41.66%;}
    .col-6 {width: 50%;}
    .col-7 {width: 58.33%;}
    .col-8 {width: 66.66%;}
    .col-9 {width: 75%;}
    .col-10 {width: 83.33%;}
    .col-11 {width: 91.66%;}
    .col-12 {width: 100%;}
}

.button_submit {
    background-color: #62A420;
    border: none;
    color: white;
    font-family: Metropolis Regular;
    padding: 6px 12px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 13px;
    border-radius: 6px;
}

</style>
