<template>
  <v-app-bar color="fee8b7">
    <v-app-bar-title 
      style="font-family: cursive"
      @click="$router.push({ name: 'pokemon' })"
    >
      Pokemon
    </v-app-bar-title>
  </v-app-bar>
  <v-navigation-drawer permanent>
  </v-navigation-drawer>
  <v-main>
    <slot />
  </v-main>
</template>

<style scoped> 
  .v-application {
    background-color: #fee8b7
  }
</style>