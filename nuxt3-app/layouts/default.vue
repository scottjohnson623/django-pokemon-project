<template>
  <div>
    <v-app-bar color="fee8b7">
      <v-app-bar-title class="title" @click="$router.push('/')">
        Pokemon
      </v-app-bar-title>
      <v-btn
        v-if="!user"
        prepend-icon="mdi-google"
        :href="`${apiUrls.BASE_URL}/google/login`"
        class="mr-5"
      >
        Login
      </v-btn>
      <v-btn v-else :href="`${apiUrls.BASE_URL}/logout`" class="mr-5">
        Logout
      </v-btn>
    </v-app-bar>
    <v-navigation-drawer width="175" permanent>
      <v-list color="transparent">
        <v-list-item
          v-if="user"
          :title="user.username"
          class="pb-3 font-weight-bold"
        ></v-list-item>
        <v-list-item
          v-for="link in links"
          :key="link.to"
          :prepend-icon="link.icon"
          :title="link.title"
          :to="link.to"
          active-color="black"
          nuxt
        ></v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <slot />
    </v-main>
  </div>
</template>

<script>
import { useAuthStore } from '~~/stores/auth';
import apiUrls from '~~/constants/apiUrls';

export default {
  data() {
    return {
      apiUrls,
    };
  },
  computed: {
    user() {
      return useAuthStore().user;
    },
    links() {
      const links = [
        { icon: 'mdi-home', title: 'Home', to: { name: 'pokemon' } },
      ];
      if (this.user) {
        links.push({
          icon: 'mdi-heart',
          title: 'Favorites',
          to: { name: 'favorites' },
        });
      }
      return links;
    },
  },
};
</script>
<style scoped>
.v-application {
  background-color: #fee8b7;
}
.title {
  font-family: cursive;
  cursor: pointer;
  font-size: 30px;
}
</style>
