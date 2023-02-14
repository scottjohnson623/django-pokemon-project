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
  data() {
    return {
      pokemon: {},
    }
  },
  async fetch({ params }) {
    try {
      const pokemon = await this.$axios.$get(`/pokemon/${params.id}`)
      this.pokemon = pokemon
    } catch (e) {
      this.pokemon = {}
    }
  },
  head() {
    return {
      title: 'View Pokemon',
    }
  },
}
</script>
