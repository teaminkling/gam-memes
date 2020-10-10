<template lang="pug">
  div#feet
    footer.footer
      div.content.is-size-7.has-text-weight-light.has-text-centered
        p Crafted with #[fa(icon="heart", class="has-text-danger")] by #[b Inkling Interactive], {{ copyrightDate }}.
      div.container
        div.columns
          div.column
          div.column
            ul.mt-4
              li
                fa.fixed-icon-pad(:icon=['fab', 'github'])
                a(:href="repoLink", target='blank') GitHub Source
              li
                fa.fixed-icon-pad(icon='bug')
                a(:href="bugLink", target='blank') Report Bugs
              li
                fa.fixed-icon-pad(icon='paint-brush')
                a(:href="featureLink", target='blank') Request Features
          div.column
            ul.mt-4
              li
                fa.fixed-icon-pad(icon='balance-scale')
                a(:href="licenseLink", target="__blank") {{ licenseName }}
              li
                fa.fixed-icon-pad(icon='user-shield')
                NuxtLink(to="/privacy") Privacy Policy
              li
                fa.fixed-icon-pad(icon='file-alt')
                NuxtLink(to="/terms") Terms and Conditions
          div.column
</template>

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
