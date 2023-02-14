<template>
  <v-card>
    <v-img height="200" :src="pokemon.image_url" />
    {{ pokemon.name }}
  </v-card>
  <!-- <div class="action-buttons">
          <nuxt-link :to="`/recipes/${pokemon.id}/`" class="btn btn-sm btn-success">View</nuxt-link>
          <nuxt-link :to="`/recipes/${pokemon.id}/edit/`" class="btn btn-sm btn-primary">Edit</nuxt-link>
          <button @click="onDelete(pokemon.id)" class="btn btn-sm btn-danger">Delete</button>
        </div> -->
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

<style>
.pokemon-card {
  box-shadow: 0 1rem 1.5rem rgba(0 0 0 60%);
}
</style>
