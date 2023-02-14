<template>
  <v-container>
    <pokemon-card :pokemon="pokemon"></pokemon-card>
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
      const pokemon = await $axios.$get(`/pokemon/${params.id}`)
      return { pokemon }
    } catch (e) {
      return { pokemons: {} }
    }
  },
  data() {
    return {
      pokemon: {},
    }
  },
  head() {
    return {
      title: 'View Pokemon',
    }
  },
}
</script>
