<template>
  <div>
    <header>
      <div class="text-box">
        <h1>Pokemon</h1>
        <p class="mt-3">Gotta catch em all</p>
        <div class="mt-5">
          <v-btn to="/pokemon" nuxt>
            Explore <span class="ml-2">&rarr;</span>
          </v-btn>
        </div>
      </div>
    </header>
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: 'Home page',
    }
  },
  mounted() {
    definePageMeta({
      layout: 'simple',
    })
  },
}
</script>

<style>
header {
  min-height: 100vh;
  background-image: url('https://images.alphacoders.com/235/235203.png');
  background-position: center;
  background-size: cover;
  position: relative;
  display: flex;
}

.text-box {
  position: absolute;
  top: 15%;
  left: 10%;
  transform: translateY(-50%);
  color: #fff;
}

.text-box h1 {
  font-family: cursive;
  font-size: 5rem;
}

.text-box p {
  font-size: 2rem;
  font-weight: lighter;
}
</style>
