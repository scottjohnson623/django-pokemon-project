<template>
  <v-container class="d-flex w-80">
    <v-img :src="pokemon.image_url" aspect-ratio="1" max-height="600px"/>
    <h1> {{ pokemon.name }} </h1> 
    <v-chip v-for="(type, index) in pokemon.types" :key="index"> {{ type.name }} </v-chip>
  </v-container>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      pokemon: {},
      pokemonExtendedDetails: {},
      drawer: false,
    };
  },
  async mounted() {
    try {
      const pokemon = await $fetch(
        `http://localhost:8000/api/pokemon/${this.$route.params.id}`
      );
      this.pokemon = pokemon;
    } catch (e) {
      this.pokemon = {};
    }
    try {
      const pokemon = await $fetch(
        `https://pokeapi.co/api/v2/pokemon/${this.$route.params.id}`
      );
      this.pokemonExtendedDetails = pokemon;
    } catch (e) {
      this.pokemonExtendedDetails = {};
    }
  },
  head() {
    return {
      title: 'View Pokemon',
    };
  },
};
</script>
