<template>
  <div class="login flex items-center justify-center mt-12">
    <div class="bg-gray-300 rounded-md text-gray-700 px-12 py-16 flex gap-3">
      <div>
        <h2 class="text-2xl font-semibold text-gray-600 mt-8">
          Sign In to browse jackets
        </h2>
        <p class="text-gray-700 w-8/12 mt-4">
          Our registration process is quick and easy, taking no more than 10
          minutes to complete.
        </p>
        <div class="mt-8">
          <img src="../assets/jacket-hero.jpg" alt="image" class="h-64 w-100" />
        </div>
      </div>
      <div class="w-72 mr-12">
        <h2 class="font-semibold text-2xl">Get Started</h2>
        <p class="text-gray-700 text-sm mt-4">Log in to your account.</p>
        <form action="" class="mt-8">
          <div class="mt-6">
            <input
              type="email"
              name="email"
              id="email"
              class="border-b-2 border-gray-600 bg-transparent h-9 w-72 focus:outline-none"
              placeholder="Username"
            />
          </div>
          <div class="mt-6">
            <input
              type="password"
              name="pass"
              id="pass"
              class="border-b-2 border-gray-600 bg-transparent h-9 w-72 focus:outline-none"
              placeholder="Password"
            />
          </div>
          <button
            type="submit"
            class="w-72 px-12 py-2 rounded-lg bg-gray-600 text-white mt-10"
          >
            Sign In
          </button>
        </form>
        <div class="mt-2">
          <router-link to="/signup" class="text-sm text-blue-500 mt-5"
            ><span class="text-gray-700">Don't have an account?</span>Sign
            Up</router-link
          >
        </div>
      </div>
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "LogIn",
};
</script>
