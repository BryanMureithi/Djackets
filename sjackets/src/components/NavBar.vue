<template>
  <div>
    <nav class="px-24 py-6 flex justify-between items-center">
      <h2 class="text-3xl font-light">Djackets</h2>
      <div class="flex gap-8">
        <router-link to="/" class="text-sm p-2 border-b-2 hover:text-gray-400"
          >Home</router-link
        >
        <router-link to="/products" class="text-sm p-2 hover:text-gray-400"
          >Products</router-link
        >
        <router-link to="/about" class="text-sm p-2 hover:text-gray-400"
          >Features</router-link
        >
        <router-link to="/about" class="text-sm p-2 hover:text-gray-400"
          >Flash Sale</router-link
        >
        <router-link to="/about" class="text-sm p-2 hover:text-gray-400"
          >Contact</router-link
        >
      </div>
      <div class="flex items-center gap-8">
        <router-link to="/login" class="text-sm hover:text-gray-400"
          >Sign in</router-link
        >
        <router-link
          to="/signup"
          class="px-8 py-2 text-sm border rounded-3xl border-gray-200 hover:bg-gray-400 hover:text-gray-700"
          >Sign Up</router-link
        >
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "NavBar",
};
</script>
