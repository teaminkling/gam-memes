<template lang="pug">

  div#base
    div#wrapper
      div.container
        navbar
        nuxt
    feet

</template>

<style scoped>

  #base {
    display: flex;
    min-height: 120vh;
    flex-direction: column;
  }

  #wrapper {
    flex: 1;
  }

</style>

<script lang="ts">

  import feet from "~/components/web/feet.vue";
  import navbar from "~/components/web/navbar.vue";

  export default {
    components: {
      feet,
      navbar,
    }
  }

</script>
