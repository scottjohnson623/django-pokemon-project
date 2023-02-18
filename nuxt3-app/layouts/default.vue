<template>
  <v-app-bar color="fee8b7">
    <v-app-bar-title class="title" @click="$router.push({ name: 'pokemon' })">
      Pokemon
    </v-app-bar-title>
    <v-btn v-if="!user" href="http://localhost:8000/google/login" class="mr-5">
      Login
    </v-btn>
    <v-btn v-else href="http://localhost:8000/logout" class="mr-5">
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
      <v-list-item prepend-icon="mdi-account-box" title="Account"></v-list-item>
      <v-list-item prepend-icon="mdi-gavel" title="Admin"></v-list-item>
    </v-list>
  </v-navigation-drawer>
  <v-main>
    <slot />
  </v-main>
</template>

<script>
import { useAuthStore } from '~~/stores/auth';

export default {
  computed: {
    user() {
      return useAuthStore().user;
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
