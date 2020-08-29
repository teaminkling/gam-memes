<template lang="pug">
  div#base
    div#wrapper
      div.container
        shoulders
        br
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

<script>
  import feet from "@/components/web/feet";
  import shoulders from "@/components/web/shoulders";

  export default {
    components: {
      feet,
      shoulders,
    }
  }
</script>
