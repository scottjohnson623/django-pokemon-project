<template>
  <v-container class="d-flex flex-column w-80 back-button">
    <div
      class="d-absolute mt-3 ml-3"
      @click="$router.push({ name: 'pokemon' })"
    >
      <v-icon icon="mdi-keyboard-backspace" />
    </div>
    <v-img :src="pokemon.image_url" aspect-ratio="1" max-height="500px" />
    <span class="text-h3 text-center text-capitalize"
      >{{ pokemon.name }} #{{ pokemonExtendedDetails.id }}
      <type-chip
        v-for="(type, index) in pokemon.types"
        :key="index"
        class="align-self-center"
        :type="type"
      >
        {{ type.name }}
      </type-chip>
    </span>
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
    }
  },
  head() {
    return {
      title: 'View Pokemon',
    }
  },
  async mounted() {
    try {
      const pokemon = await $fetch(
        `http://localhost:8000/api/pokemon/${this.$route.params.id}`
      )
      this.pokemon = pokemon
    } catch (e) {
      this.pokemon = {}
    }
    try {
      const pokemon = await $fetch(
        `https://pokeapi.co/api/v2/pokemon/${this.$route.params.id}`
      )
      this.pokemonExtendedDetails = pokemon
    } catch (e) {
      this.pokemonExtendedDetails = {}
    }
  },
}
</script>
