
import { NuxtPage } from './.nuxt/components';

<template>
    <v-app>
    <v-app-bar color="fee8b7">
      <template v-slot:prepend>
          <v-app-bar-nav-icon></v-app-bar-nav-icon>
        </template>

        <v-app-bar-title>Po</v-app-bar-title>
    </v-app-bar>
  <v-main>
    <NuxtPage />
  </v-main>
  </v-app>

</template>

<style scoped> 
  .v-application {
    background-color: #fee8b7
  }
</style>