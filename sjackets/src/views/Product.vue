<template>
  <div class="min-h-screen px-12">
    <div class="flex ml-12">
      <div class="w-8/12 px-4 py-10">
        <img
          :src="product.get_image"
          alt="Product Image"
          class="img rounded-lg"
        />
      </div>
      <div class="py-12">
        <h1 class="text-3xl font-semibold">{{ product.name }}</h1>

        <p class="mt-6 w-8/12">{{ product.description }}</p>
        <p class="mt-6 text-4xl font-bold">${{ product.price }}</p>

        <div class="flex items-center mt-5">
          <div>
            <input
              type="number"
              name="quantity"
              id="quantity"
              min="1"
              v-model="quantity"
              class="text-black py-1"
            />
          </div>
          <div>
            <router-link
              to="/"
              class="bg-gray-400 text-black text-sm px-4 py-2 rounded-md"
              >Add to cart</router-link
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProductDetail",
  data() {
    return {
      product: {},
      quantity: 1,
    };
  },
  mounted() {
    this.getProduct();
  },
  methods: {
    getProduct() {
      const category_slug = this.$route.params.category_slug;
      const product_slug = this.$route.params.product_slug;

      axios
        .get(`/api/v1/products/${category_slug}/${product_slug}`)
        .then((response) => {
          this.product = response.data;
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
  width: 80%;
  height: 70%;
  object-fit: cover;
}
</style>
