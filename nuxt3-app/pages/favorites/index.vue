<template>
  <div>
    <pokemon-card-list :pokemons="pokemons" />
  </div>
</template>

<script>
import apiUrls from '~~/constants/apiUrls';
import { makeApiCall } from '~~/utils/apiUtil';

export default {
  data() {
    return {
      pokemons: [],
    };
  },
  head() {
    return {
      title: 'Pokemon list',
    };
  },
  async mounted() {
    try {
      const pokemons = await makeApiCall(apiUrls.FAVORITE_POKEMONS);
      this.pokemons = pokemons;
    } catch (e) {
      this.pokemons = [];
    }
  },
};
</script>
