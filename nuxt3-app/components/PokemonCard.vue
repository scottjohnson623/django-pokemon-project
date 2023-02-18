<template>
  <v-card :to="link" nuxt>
    <v-img aspect-ratio="1" :src="pokemon.image_url" class="mt-2" />
    <div style="cursor: pointer" @click.prevent="handleClick">
      <v-icon
        icon="mdi-heart-circle-outline"
        class="float-right"
        :color="iconColor"
        size="x-large"
        style="position: absolute; top: 0; right: 0"
      />
    </div>
    <div class="text-h5 text-center pb-5 text-capitalize">
      {{ pokemon.name }}
    </div>
  </v-card>
</template>

<script>
import { useAuthStore } from '~~/stores/auth';
import apiUrls from '~~/constants/apiUrls';
import { makeApiCall } from '~~/utils/apiUtil';

export default {
  props: {
    pokemon: {
      type: Object,
      default: () => {},
    },
  },
  computed: {
    link() {
      return 'pokemon/' + this.pokemon.id;
    },
    user() {
      return useAuthStore().user;
    },
    isFavorited() {
      return this.user?.favorites?.includes(this.pokemon.id);
    },
    iconColor() {
      return this.isFavorited ? 'red' : 'grey';
    },
  },
  methods: {
    handleClick() {
      if (!this.user) {
        return;
      }
      if (this.isFavorited) {
        this.user.favorites = this.user.favorites?.filter(
          (id) => id !== this.pokemon.id
        );
        makeApiCall(apiUrls.UNFAVORITE, 'POST', {
          pokemon_id: this.pokemon.id,
        });
      } else {
        this.user.favorites?.push(this.pokemon.id);
        makeApiCall(apiUrls.FAVORITE, 'POST', { pokemon_id: this.pokemon.id });
      }
    },
  },
};
</script>

<style>
.pokemon-card {
  box-shadow: 0 1rem 1.5rem rgba(0 0 0 60%);
}
</style>
