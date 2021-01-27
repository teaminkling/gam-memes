<template lang="pug">

  div#base
    div#wrapper
      div.container
        page_navbar

        nuxt
    page_footer

</template>

<style scoped>

/*
 * Min-height page content for sticky footer.
 */

#base {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}

#wrapper {
  flex: 1;
}

</style>

<script lang="ts">

import page_footer from "~/components/web/page_footer.vue";
import page_navbar from "~/components/web/page_navbar.vue";

export default {
  components: {
    page_footer,
    page_navbar,
  }
}

</script>
