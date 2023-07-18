<template>
  <div>
    <div class="mt-6 flex flex-wrap gap-12 ml-6">
      <div v-for="product in latestProducts" :key="product.id">
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
  name: "ImageCard",
  data() {
    return {
      latestProducts: [],
    };
  },
  components: {},
  mounted() {
    this.getLatestProducts();
  },
  methods: {
    getLatestProducts() {
      axios
        .get("/api/v1/latest-products/")
        .then((response) => {
          this.latestProducts = response.data;
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
