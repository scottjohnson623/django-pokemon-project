<template>
  <v-card :to="link" nuxt>
    <v-img aspect-ratio="1" :src="pokemon.image_url" />
    <div class="text-h5 text-center pb-5 text-capitalize">
      {{ pokemon.name }}
    </div>
    <v-icon icon="mdi-heart-circle-outline" class="float-right" color="grey" size="x-large"/>
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
  computed: {
    link() {
      return 'pokemon/' + this.pokemon.id
    },
  },
}
</script>

<style>
.pokemon-card {
  box-shadow: 0 1rem 1.5rem rgba(0 0 0 60%);
}
</style>
