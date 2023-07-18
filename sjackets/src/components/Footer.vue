<template>
  <footer class="bg-transparent px-12 py-6 mt-6">
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-3xl font-raleway">DJACKETS</h1>
      </div>
      <div class="flex items-center gap-4">
        <router-link to="/">Summer</router-link>
        <router-link to="/">Winter</router-link>
        <router-link to="/">Spring</router-link>
        <router-link to="/">Discounts</router-link>
        <router-link to="/">Products</router-link>
      </div>
      <div class="flex items-center gap-3">
        <i class="bx bxl-instagram bx-md"></i>
        <i class="bx bxl-facebook bx-md"></i>
        <i class="bx bxl-twitter bx-md"></i>
      </div>
    </div>
    <hr class="w-full mt-6" />
    <div class="flex items-center justify-between mt-6">
      <div>
        <h2 class="text-sm text-gray-300">
          © 2023 Djackets. All rights reserved. Created by Bryan Mureithi
        </h2>
      </div>
      <div>
        <a href="#" class="text-sm text-gray-300"
          >Privacy Policy | Terms of Service</a
        >
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "FooterMain",
};
</script>
