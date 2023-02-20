<template>
  <div style="cursor: pointer" @click.prevent="handleClick">
    <v-icon icon="mdi-heart-circle-outline" :color="iconColor" :size="size" />
  </div>
</template>

<script>
export default {
  props: {
    isFavorited: {
      type: Boolean,
      default: false,
    },
    doDisable: {
      type: Boolean,
      default: false,
    },
    size: {
      type: String,
      default: 'med',
    },
  },
  emits: ['clicked'],
  computed: {
    iconColor() {
      return this.isFavorited ? 'red' : 'grey';
    },
  },
  methods: {
    handleClick() {
      if (this.doDisable) {
        return;
      }
      this.$emit('clicked');
    },
  },
};
</script>
