<template>
  <div class="font-raleway bg-[#212529]">
    <NavBar />
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";
export default {
  components: {
    NavBar,
  },
};
</script>

<style>
#app {
  background-color: #212529;
  color: white;
  width: 100%;
  min-height: 100vh;
}
</style>
