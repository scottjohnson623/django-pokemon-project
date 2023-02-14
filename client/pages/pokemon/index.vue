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
        AAAAA
        <pokemon-card :pokemon="pokemon" />
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
  data() {
    return {
      pokemons: [],
    }
  },
  async fetch() {
    try {
      const pokemons = await this.$axios.$get(`/pokemon/`)
      this.pokemons = pokemons.results
    } catch (e) {
      this.pokemons = []
    }
  },
  head() {
    return {
      title: 'Pokemon list',
    }
  },
}
</script>
