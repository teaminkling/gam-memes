<template lang="pug">
  div#feet
    footer(class="footer")
      div(class="content is-size-7 has-text-weight-light has-text-centered")
        p
          | Crafted with #[fa(icon="heart", class="has-text-danger")] by #[b Inkling Interactive], {{ copyrightDate }}.
      div(class="columns")
        div(class="column is-one-quarter")
        div(class="column")
          ul(class="mt-4")
            li
              fa(icon='home', class="fixed-icon-pad")
              NuxtLink(to="/") Home
            li
              fa(icon='gamepad', class="fixed-icon-pad")
              NuxtLink(to="/app") Game
            br
            br
            li
              fa(icon='address-card', class="fixed-icon-pad")
              NuxtLink(to="/about") About
        div(class="column")
          ul(class="mt-4")
            li
              fa(:icon=['fab', 'discord'], class="fixed-icon-pad")
              a(:href="discordLink", target='blank') Discord
            br
            li
              fa(:icon=['fab', 'github'], class='fixed-icon-pad')
              a(:href="repoLink", target='blank') GitHub Source
            li
              fa(icon='bug', class='fixed-icon-pad')
              a(:href="bugLink", target='blank') Report Bugs
            li
              fa(icon='paint-brush', class='fixed-icon-pad')
              a(:href="featureLink", target='blank') Request Features
        div(class="column")
          ul(class="mt-4")
            li
              fa(icon='balance-scale', class="fixed-icon-pad")
              a(:href="licenseLink", target="__blank") {{ licenseName }}
            br
            br
            li
              fa(icon='user-shield', class="fixed-icon-pad")
              NuxtLink(to="/privacy") Privacy Policy
            li
              fa(icon='file-alt', class="fixed-icon-pad")
              NuxtLink(to="/terms") Terms and Conditions
        div(class="column is-one-quarter")
</template>

<!--suppress CssUnusedSymbol -->
<style scoped>
  .fixed-icon-pad {
    width: 3em;
  }
</style>

<script>
import urljoin from 'url-join';

import {
  DISCORD_LINK,
  GITHUB_BUG_REPO_PATH,
  GITHUB_FEATURE_REQUEST_PATH,
  GITHUB_REPO_LINK,
  LICENSE_LINK,
  LICENSE_NAME,
} from '@/constants/social';

export default {
  name: "feet",
  data() {
    return {
      /* Social. */
      "discordLink"   : DISCORD_LINK,
      /* GitHub. */
      "repoLink"      : GITHUB_REPO_LINK,
      "bugLink"       : urljoin(GITHUB_REPO_LINK, GITHUB_BUG_REPO_PATH),
      "featureLink"   : urljoin(GITHUB_REPO_LINK, GITHUB_FEATURE_REQUEST_PATH),
      /* Legal. */
      "licenseName"   : LICENSE_NAME,
      "licenseLink"   : LICENSE_LINK,
      "copyrightDate" : `2020 - present`,
    }
  }
}
</script>
