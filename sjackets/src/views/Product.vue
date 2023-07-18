<template>
  <div class="min-h-screen px-12 py-8">
    <div class="flex ml-12">
      <div class="w-4/12">
        <figure class="">
          <img
            :src="product.get_image"
            alt="Product Image"
            class="img rounded-lg h-full"
          />
        </figure>

        <h1>{{ product.name }}</h1>

        <p>{{ product.description }}</p>
      </div>
      <div class="px-6 py-6">
        <h2 class="w-8/12">
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ducimus
          magnam eaque, vitae animi error odit laborum sequi illum veritatis
          explicabo!
        </h2>

        <p class="mt-4 font-bold">${{ product.price }}</p>

        <div class="flex items-center mt-5">
          <div>
            <input
              type="number"
              name="quantity"
              id="quantity"
              min="1"
              v-model="quantity"
              class="text-black"
            />
          </div>
          <div>
            <router-link
              to="/"
              class="bg-gray-400 text-black px-4 py-1 rounded-md"
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
  max-width: 100%;
}
</style>
