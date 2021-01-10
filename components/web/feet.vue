<template lang="pug">

  div#feet
    footer.footer
      div.content.is-size-7.has-text-weight-light.has-text-centered
        p Crafted with #[fa(icon="heart", class="has-text-danger")] by #[b Inkling Interactive], {{ copyright_date }}.
      div.container
        div.columns
          div.column
          div.column
            ul.mt-4
              li
                fa.fixed-icon-pad(:icon=['fab', 'github'])
                a(:href="repo_link", target='blank') GitHub Source
              li
                p &nbsp;
              li
                fa.fixed-icon-pad(icon='bug')
                a(:href="bug_link", target='blank') Report Bugs
              li
                fa.fixed-icon-pad(icon='paint-brush')
                a(:href="feature_link", target='blank') Request Features
          div.column
            ul.mt-4
              li
                fa.fixed-icon-pad(icon='balance-scale')
                a(:href="license_link", target="__blank") License
              li
                p &nbsp;
              li
                fa.fixed-icon-pad(icon='user-shield')
                a(:href="privacy_link", target="__blank") Privacy Policy
              li
                fa.fixed-icon-pad(icon='file-alt')
                a(:href="terms_link", target="__blank") Terms of Use
          div.column

</template>

<style scoped>

  .fixed-icon-pad {
    width: 3em;
  }

</style>

<script lang="ts">

import urljoin from 'url-join';

import {
  DISCORD_LINK,
  GITHUB_BUG_REPO_PATH,
  GITHUB_FEATURE_REQUEST_PATH,
  GITHUB_REPO_LINK,
  LICENSE_LINK,
  PRIVACY_LINK,
  TERMS_LINK,
} from '@/constants/social';

export default {
  name: "feet",
  data() {
    return {
      /* Social. */

      "discord_link"   : DISCORD_LINK,

      /* GitHub. */

      "repo_link"      : GITHUB_REPO_LINK,
      "bug_link"       : urljoin(GITHUB_REPO_LINK, GITHUB_BUG_REPO_PATH),
      "feature_link"   : urljoin(GITHUB_REPO_LINK, GITHUB_FEATURE_REQUEST_PATH),

      /* Legal. */

      "license_link"   : LICENSE_LINK,
      "privacy_link"   : PRIVACY_LINK,
      "terms_link"     : TERMS_LINK,
      "copyright_date" : `2020 - present`,
    }
  }
}

</script>
