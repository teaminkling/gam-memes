<template lang="pug">

  div.navbar-end
    a.navbar-item(@click="toggle")
      ColorScheme(tag="span")
        span(v-if="$colorMode.value === 'dark'")
          p #[fa(icon="moon")] Theme
        span(v-else)
          p #[fa(icon="lightbulb")] Theme


</template>

<script>

export default {
  name: "page_toggle",
  methods: {
    toggle() {
      if (this.$colorMode.preference !== "dark") {
        this.$colorMode.preference = 'dark';
      } else {
        this.$colorMode.preference = 'light';
      }
    },
  }
}

</script>
