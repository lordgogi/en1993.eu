<template>
  <div class="hello">

    <div class="title" >
      EN1993.eu
    </div>

    <div class="sub-title" >
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vel augue urna. Suspendisse et justo porta, tincidunt ligula id, bibendum tortor.
      Quisque pretium dignissim orci id fermentum. Morbi gravida varius dolor sed feugiat. Aenean eget dictum ante. Nullam est nisi, dapibus sed massa quis, maxim
    </div>

    <img v-on:click="active_component='section_i'" alt="Vue logo" src="../assets/main-art.png">

    <div class="accented" >
      Engineering Scrips, Calculators and API's for Mechanical and Civil Engineers
    </div>
  </div>
</template>

<style scoped>

.title {
  padding: 50px 0 0 0;
  font-size: 50px;
  font-weight: lighter;
  color: #676767;
  letter-spacing: 4px;
}

.sub-title {
  padding: 50px 0 0 0;
  font-size: 12px;
  font-weight: lighter;
  color: #676767;
  letter-spacing: 2px;
}

.accented {
  padding: 50px 0 0 0;
  font-size: 26px;
  font-weight: lighter;
  color: #676767;
  letter-spacing: 2px;
}

</style>
