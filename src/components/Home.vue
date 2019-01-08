<template>
<div>

  <div class="row">

    <div class="col-2 col-s-1"></div>
    <div class="col-3 col-s-4">
      <ul>
        <li>
          Cross Section Properties<br>
          <router-link to="/I_shape"> <img alt="Cross Section Properties Preview" src="../assets/preview_cross_section.png"> </router-link>
        </li>
        <li>
          Bolts In-plane Loading<br>
          <router-link to="/BoltInLine"> <img alt="Cross Section Properties Preview" src="../assets/preview_in_plane.png"> </router-link>
        </li>

      </ul>
    </div>
    <div class="col-5 col-s-6">
      <h1>EN 1993 EU</h1>
      <h3>Mechanical Engineering Calculators</h3>

      <p>EN-1993 is a set of tools, scrips and API's built to help Mechanical Engineers and Designers with their daily task of sizing and design
        of machine elements. Ultimate goal is to build interactive set of components accessible via web browser as well as remote API's that Engineers
        can use to expand capability of their own programs and tools.<br><br>
        Website is build in Vue and API is build with Flask</p>

        <p>Main focus of site is:
          <ul>
            <li>Calculation of Cross section properties</li>
            <li>Bolted Connection sizing and checking</li>
            <li>Welded Connection sizing and checking</li>
            <li>Structural checks of plated elements and stiffened panels</li>
            <li>Various structural checks of elements to EN1993 and AISC</li>
          </ul>
        </p>

        <p>
          If you have questions, comments or want to contribute please contact me at: info@en1993.eu

        </p>

    </div>
    <div class="col-2 col-s-1"></div>

  </div>
</div>
</template>

<style scoped>

</style>
