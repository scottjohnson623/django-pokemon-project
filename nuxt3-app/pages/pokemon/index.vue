<template>
  <v-container>
    <v-row>
      <v-col
        v-for="pokemon in pokemons"
        :key="pokemon.id"
        cols="12"
        sm="4"
        md="2"
      >
        <pokemon-card :pokemon="pokemon" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import PokemonCard from '~/components/PokemonCard.vue';
export default {
  components: {
    PokemonCard,
  },
  data() {
    return {
      pokemons: [],
    };
  },
  async mounted() {
    try {
      const pokemons = await $fetch('http://localhost:8000/api/pokemon');
      this.pokemons = pokemons.results;
    } catch (e) {
      console.log(e);
      this.pokemons = [];
    }
  },
  head() {
    return {
      title: 'Pokemon list',
    };
  },
};
</script>
