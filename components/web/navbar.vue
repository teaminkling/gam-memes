<template lang="pug">

  div#navbar
    nav.navbar(role="navigation")
      div.navbar-brand
        NuxtLink.navbar-item(to="/")
          p Memeforming
      div.navbar-menu#navbar
        div.navbar-start
          NuxtLink.navbar-item(to="/")
            p #[fa(icon='home')] Home
          NuxtLink.navbar-item(to="/app")
            p #[fa(icon='gamepad')] Game
          a.navbar-item(:href="discord_link", target="__blank")
            p #[fa(:icon=['fab', 'discord'])] Discord

</template>

<script lang="ts">

import { DISCORD_LINK } from "@/constants/social";

export default {
  name: "navbar",
  data() {
    return {
      /* Social. */

      "discord_link": DISCORD_LINK,
    }
  }
}

</script>
