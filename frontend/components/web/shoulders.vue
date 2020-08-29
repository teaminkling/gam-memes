<template lang="pug">
  div#shoulders
    nav.navbar(role="navigation")
      div.navbar-brand
        NuxtLink.navbar-item(to="/")
          p Logo Here
      div.navbar-menu#navbar
        div.navbar-start
          NuxtLink.navbar-item(to="/")
            p #[fa(icon='home')] Home
          NuxtLink.navbar-item(to="/app")
            p #[fa(icon='gamepad')] Game
        div.navbar-end
          NuxtLink.navbar-item(to="/about")
            p #[fa(icon='address-card')] About
          a.navbar-item(:href="discordLink", target="__blank")
            p #[fa(:icon=['fab', 'discord'])] Discord
</template>

<script>
import { DISCORD_LINK } from "@/constants/social";

export default {
  name: "shoulders",
  data() {
    return {
      /* Social. */
      "discordLink": DISCORD_LINK,
    }
  }
}
</script>
