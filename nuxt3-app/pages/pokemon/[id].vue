<template>
  <v-container class="d-flex flex-column w-80 back-button">
    <div class="d-absolute mt-3 ml-3 d-inline-flex justify-space-between">
      <div @click="$router.push({ name: 'pokemon' })">
        <v-icon icon="mdi-keyboard-backspace" />
      </div>
      <like-button
        :is-favorited="isFavorited"
        :do-disable="!user"
        size="x-large"
        class="float-right"
        @clicked="handleClick"
      />
    </div>
    <div class="text-h3 text-center text-capitalize">
      {{ pokemon.name }} #{{ pokemonExtendedDetails.id }}
      <type-chip
        v-for="(type, index) in pokemon.types"
        :key="index"
        class="align-self-center"
        :type="type"
      >
        {{ type.name }}
      </type-chip>
    </div>

    <v-row>
      <v-col cols="6">
        <v-img :src="pokemon.image_url" aspect-ratio="1" max-height="500px" />
      </v-col>
      <v-col cols="6">
        <div class="mt-9 mb-4">{{ flavorText }}</div>
        <v-row class="mt-1 mb-1"
          ><v-col cols="6"
            ><span class="ml-3"
              ><span class="font-weight-bold"> Height</span>:
              {{ formatHeight(pokemonExtendedDetails.height) }}</span
            ></v-col
          ><v-col cols="6"
            ><span class="font-weight-bold">Weight</span>:
            {{ formatWeight(pokemonExtendedDetails.weight) }}</v-col
          ></v-row
        >
        <v-card>
          <div class="text-h5 ml-4 mt-4 font-weight-bold">Stats</div>
          <v-row
            v-for="(stat, index) in pokemonExtendedDetails.stats"
            :key="index"
            class="mt-2 mb-2 d-flex justify-center align-center"
          >
            <v-col cols="10">
              <span class="text-capitalize m-0 font-weight-bold">
                {{ stat.stat.name.replace('-', ' ') }}
                <v-progress-linear
                  :model-value="stat.base_stat"
                  max="255"
                  striped
                  :color="barColor(stat.base_stat)"
              /></span>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { useAuthStore } from '~~/stores/auth';
import apiUrls from '~~/constants/apiUrls';
export default {
  components: {},
  data() {
    return {
      pokemon: {},
      pokemonExtendedDetails: {},
      pokemonFlavorText: null,
      drawer: false,
    };
  },
  head() {
    return {
      title: 'View Pokemon',
    };
  },
  computed: {
    flavorText() {
      return this.pokemonFlavorText
        ? this.pokemonFlavorText.flavor_text_entries.filter(
            (elem) => elem.language.name === 'en'
          )[0].flavor_text
        : null;
    },
    user() {
      return useAuthStore().user;
    },
    isFavorited() {
      return this.user?.favorites?.includes(this.pokemon.id);
    },
  },
  async mounted() {
    try {
      const pokemon = await $fetch(
        `http://localhost:8000/api/pokemon/${this.$route.params.id}`
      );
      this.pokemon = pokemon;
    } catch (e) {
      this.pokemon = {};
    }
    try {
      const pokemon = await $fetch(
        `https://pokeapi.co/api/v2/pokemon/${this.$route.params.id}`
      );
      this.pokemonExtendedDetails = pokemon;
    } catch (e) {
      this.pokemonExtendedDetails = {};
    }
    try {
      const pokemon = await $fetch(
        `https://pokeapi.co/api/v2/pokemon-species/${this.$route.params.id}`
      );
      this.pokemonFlavorText = pokemon;
    } catch (e) {
      this.pokemonFlavorText = null;
    }
  },
  methods: {
    formatHeight(height) {
      return `${height * 10} cm`;
    },
    formatWeight(weight) {
      return `${weight / 10} kg`;
    },
    barColor(statValue) {
      if (statValue <= 65) {
        return 'red';
      }
      if (statValue <= 100) {
        return 'yellow';
      }
      return 'green';
    },
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
