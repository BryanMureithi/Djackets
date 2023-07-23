<template>
  <div>
    <div class="hero grid grid-cols-2 gap-8 px-12">
      <div>
        <img
          src="../assets/jacket-hero.jpg"
          alt="Multiple jackets"
          class="image"
        />
      </div>
      <div class="p-0 col-span-1">
        <h1
          class="w-10/12 mt-16 ml-12 text-gray-100 text-4xl font-bold md:text-2xl lg:text-2xl xl:text-3xl 2xl:text-4xl 2xl:w-7/12"
        >
          Unleash your style. Discover the perfect jackets for every occassion.
        </h1>
        <p
          class="w-7/12 mt-6 ml-12 leading-relaxed text-sm text-textSecondary font-inter"
        >
          Elevate your wardrobe with our exceptional collection of jackets,
          meticulously crafted to keep you stylish, comfortable, and ready for
          any adventure.
        </p>
        <div class="ml-12 mt-8 flex items-center gap-8">
          <router-link
            to="/products"
            class="px-8 py-2 flex items-center gap-2 text-sm border rounded-3xl border-gray-200 hover:bg-gray-500 hover:text-gray-700"
            >Shop Now <i class="bx bx-right-arrow-alt"></i
          ></router-link>
          <router-link
            to=""
            class="px-8 py-2 text-sm rounded-3xl bg-gray-600 hover:bg-gray-500 hover:text-gray-300"
            >Categories</router-link
          >
        </div>
      </div>
    </div>
    <div
      class="w-100 h-48 mt-5 font-inter bg-container px-12 flex flex-wrap items-center justify-between"
    >
      <!--Stats-->
      <div class="flex gap-4">
        <div>
          <i class="bx bx-package bx-md mt-3 text-textSecondary"></i>
        </div>
        <div class="flex flex-col gap-3">
          <h3 class="font-semibold text-sm">FREE SHIPPING</h3>
          <p class="text-textSecondary text-sm">On all orders above $140 USD</p>
        </div>
      </div>
      <!--Vertical Line-->
      <div class="w-0.5 h-24 bg-textSecondary"></div>
      <!--Stats-->
      <div class="flex gap-4">
        <div>
          <i class="bx bx-package bx-md mt-3 text-textSecondary"></i>
        </div>
        <div class="flex flex-col gap-3">
          <h3 class="font-semibold text-sm">24 / 7 SERVICE</h3>
          <p class="text-textSecondary text-sm">
            Get help whenever you need it
          </p>
        </div>
      </div>
      <!--Vertical Line-->
      <div class="w-0.5 h-24 bg-textSecondary"></div>
      <!--Stats-->
      <div class="flex gap-4">
        <div>
          <i class="bx bx-package bx-md mt-3 text-textSecondary"></i>
        </div>
        <div class="flex flex-col gap-3">
          <h3 class="font-semibold text-sm">100% MONEY BACK</h3>
          <p class="text-textSecondary text-sm">21 days money back guarantee</p>
        </div>
      </div>
      <!--Vertical Line-->
      <div class="w-0.5 h-24 bg-textSecondary"></div>
      <!--Stats-->
      <div class="flex gap-4">
        <div>
          <i class="bx bx-package bx-md mt-3 text-textSecondary"></i>
        </div>
        <div class="flex flex-col gap-3">
          <h3 class="font-semibold text-sm">FREE SHIPPING</h3>
          <p class="text-textSecondary text-sm">On all orders above $140 USD</p>
        </div>
      </div>
    </div>
    <div class="mt-6 px-12">
      <h2 class="font-semibold font-inter">NEW ARRIVALS</h2>
      <JacketCard />
    </div>
    <div class="mt-6">
      <PromoSection />
    </div>
    <FooterMain />
    <router-view />
  </div>
</template>

<script>
import JacketCard from "../components/Card.vue";
import FooterMain from "../components/Footer.vue";
import PromoSection from "../components/Promo.vue";
export default {
  name: "HomePage",
  components: { JacketCard, FooterMain, PromoSection },
};
</script>

<style>
.image {
  border-radius: 7px;
  margin: 12px;
  max-width: 100%;
}
</style>
