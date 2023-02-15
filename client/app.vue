<template>
  <v-app>
    <v-app-bar color="fee8b7">
      <template v-slot:prepend>
          <v-app-bar-nav-icon></v-app-bar-nav-icon>
        </template>

        <v-app-bar-title>Photos</v-app-bar-title>

        <template v-slot:append>
          <v-btn icon="mdi-dots-vertical"></v-btn>
        </template>
    </v-app-bar>
  <v-main>
    <nuxt />
  </v-main>
  </v-app>
</template>

<style scoped> 
  .v-application {
    background-color: #fee8b7
  }
</style>