<button type="button" v-on:click="addNewApartment">
    Add +
</button>



<div v-for="(apartment, index) in apartments">

            <input v-model="apartment.price" name="apartments[][price]">

            <input v-model="apartment.rooms" name="apartments[][rooms]">

            <button type="button" v-on:click="removeApartment(index)"> Remove </button>

</div>




  data: {
    apartment: {
      price: '',
      rooms: ''
    },
    apartments: [],
  },




  methods:
  {


    addNewApartment: function () {
      this.apartments.push(Vue.util.extend({}, this.apartment))
    },



    removeApartment: function (index) {
      Vue.delete(this.apartments, index);
    },


  }
})
