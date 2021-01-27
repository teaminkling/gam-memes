<template lang="pug">

  div#page_navbar
    nav.navbar(role="navigation")
      div.navbar-brand
        NuxtLink.navbar-item(to="/")
          p Memeforming
        a.navbar-burger(role="button")
          span
          span
          span
      div.navbar-menu#navbar
        div.navbar-start
          NuxtLink.navbar-item(to="/")
            p About
          NuxtLink.navbar-item(to="/app")
            p #[fa(:icon=['fab', 'chrome'])] Web
          a.navbar-item
            p #[fa(:icon=['fab', 'apple'])] iOS
          a.navbar-item
            p #[fa(:icon=['fab', 'google'])] Android
          a.navbar-item
            p #[fa(:icon=['fab', 'steam'])] Steam
      page_toggle

</template>

<script lang="ts">

import page_toggle from '~/components/web/page_toggle.vue';

export default {
  name: "navbar",
  components: {
    page_toggle
  }
}

</script>
