<template>
  <div>
    <footer class="bg-gray-600 px-12 py-8 mt-12 flex gap-12 justify-end">
      <div>
        <h2 class="font-semibold">LINKS</h2>
        <div class="flex flex-col gap-2 mt-2">
          <a href="#" class="text-gray-400 hover:text-gray-300">Instagram</a>
          <a href="#" class="text-gray-400 hover:text-gray-300">Twitter</a>
          <a href="#" class="text-gray-400 hover:text-gray-300">Facebook</a>
        </div>
      </div>
      <div>
        <h2 class="font-semibold">PRODUCTS</h2>
        <div class="flex flex-col gap-2 mt-2">
          <a href="#" class="text-gray-400 hover:text-gray-300"
            >Winter Jackets</a
          >
          <a href="#" class="text-gray-400 hover:text-gray-300"
            >Summer Jackets</a
          >
          <a href="#" class="text-gray-400 hover:text-gray-300"
            >Men's Jackets</a
          >
        </div>
      </div>
      <div>
        <h2 class="font-semibold">CONTACTS</h2>
        <div class="flex flex-col gap-2 mt-2">
          <a href="#" class="text-gray-400 hover:text-gray-300"
            ><span>Tel: </span> +2547324657</a
          >
          <a href="#" class="text-gray-400 hover:text-gray-300"
            ><span>Address: </span>Bogani Rd, Karen.</a
          >
          <a href="#" class="text-gray-400 hover:text-gray-300"
            ><span>Email: </span>djackets@info.com</a
          >
        </div>
      </div>
    </footer>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "FooterMain",
};
</script>
