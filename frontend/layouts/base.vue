<template lang="pug">
  div#base
    div#wrapper
      div.container
        shoulders
        nuxt
    feet
</template>

<style scoped>
  #base {
    display: flex;
    min-height: 122vh;
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
