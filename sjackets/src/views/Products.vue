<template>
  <div class="px-24">
    <div class="mt-6 flex flex-wrap gap-12 ml-6">
      <div v-for="product in Products" :key="product.id">
        <div class="w-72">
          <figure>
            <img
              :src="product.get_image"
              class="img rounded-lg h-96"
              alt="jacket"
            />
          </figure>

          <h3 class="mt-2 font-semibold">{{ product.name }}</h3>
          <p class="mt-1 font-semibold text-gray-400">${{ product.price }}</p>

          <router-link :to="product.get_absolute_url">View details</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ProductView",
  data() {
    return {
      Products: {},
    };
  },
  components: {},
  mounted() {
    this.getProducts();
  },
  methods: {
    getProducts() {
      axios
        .get("/api/v1/all-products/")
        .then((response) => {
          this.Products = response.data;
        })
        .catch((error) => {
          console.log("Error getting products:", error);
        });
    },
  },
};
</script>

<style>
.img {
  max-width: 100%;
}
</style>
