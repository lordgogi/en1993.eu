<template>
  <div>
    <div class="row">

      <div class="card" style="width: 550px;">
        <div class="card-header">
          <h6 style="margin:0px;">Inputs:</h6>
        </div>
        <div class="card-block">
          <slot name="inputs"></slot>
          <button>Submit</button>
        </div>
      </div>

      <div class="card"  style="width: 500px;">
        <div class="card-header">
          <h6 style="margin:0px;">Outputs:</h6>
        </div>
        <div class="card-block">
          <slot name="outputs"></slot>
        </div>
      </div>

    </div>
  </div>
</template>
