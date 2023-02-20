<template>
  <div>
    <pokemon-card-list :pokemons="pokemons" />
    <v-card v-intersect="infiniteScrolling"></v-card>
  </div>
</template>

<script>
import apiUrls from '~~/constants/apiUrls';
import { makeApiCall } from '~~/utils/apiUtil';

export default {
  data() {
    return {
      pokemons: [],
      url: apiUrls.POKEMON_ROOT_VIEW,
    };
  },
  head() {
    return {
      title: 'Pokemon list',
    };
  },
  async mounted() {
    try {
      const pokemons = await makeApiCall(this.url);
      this.url = pokemons.next;
      this.pokemons = pokemons.results;
    } catch (e) {
      this.pokemons = [];
    }
  },
  methods: {
    infiniteScrolling(entries, observer, isIntersecting) {
      if (!this.url) {
        return;
      }
      setTimeout(() => {        
          makeApiCall(this.url)
          .then((response) => {
            this.url = response.next;
            if (response.results.length > 1) {
              response.results.forEach((item) => this.pokemons.push(item));
            }
          })
          .catch((err) => {
            console.log(err);
          });
      }, 500);
    },
  },
};
</script>
