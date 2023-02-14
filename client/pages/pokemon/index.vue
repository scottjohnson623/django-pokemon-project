<template>
  <v-container>
    <h3>Pokemon</h3>
    <v-row>
      <v-col
        v-for="pokemon in pokemons"
        :key="pokemon.id"
        cols="12"
        sm="3"
        md="4"
      >
        <pokemon-card :pokemon="pokemon"></pokemon-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import PokemonCard from '~/components/PokemonCard.vue'

export default {
  components: {
    PokemonCard,
  },
  async asyncData({ $axios, params }) {
    try {
      const pokemons = await $axios.$get(`/pokemon/`)
      return { pokemons: pokemons.results }
    } catch (e) {
      return { pokemons: [] }
    }
  },
  data() {
    return {
      pokemons: [],
    }
  },
  head() {
    return {
      title: 'Pokemon list',
    }
  },
}
</script>
