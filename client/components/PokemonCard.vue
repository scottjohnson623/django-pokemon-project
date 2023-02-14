<template>
  <v-card>
    <v-img height="200" :src="pokemon.image_url" />
    <nuxt-link :to="{ name: 'pokemon', params: { id: pokemon.id } }">
      {{ pokemon.name }}
    </nuxt-link>
  </v-card>
</template>

<script>
export default {
  props: {
    pokemon: {
      type: Object,
      default: () => {},
    },
  },
}
</script>
