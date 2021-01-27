<template lang="pug">

  div#page_footer
    footer.footer
      div.content.is-size-7.has-text-weight-light.has-text-centered
        p
          | Created with #[fa(icon="heart", class="has-text-danger")] and published by
          | #[a(:href="site_link", target="__blank") Inkling Interactive].
          | Proudly free and open-source since 2020!
        p
          fa.fixed-icon-pad(:icon=['fab', 'github'])
          a(:href="repo_link", target='blank') GitHub Source
          fa.fixed-icon-pad.icon-margin(icon='user-shield')
          a(:href="privacy_link", target="__blank") Privacy Policy

          fa.fixed-icon-pad.icon-margin(icon='file-alt')
          a(:href="terms_link", target="__blank") Terms of Use

</template>

<style scoped>

.icon-margin {
  margin-left: 2.5em;
}

.footer {
  padding-bottom: 2.5rem !important;
}

</style>

<script lang="ts">

import { REPO_LINK, SITE_LINK, PRIVACY_LINK, TERMS_LINK } from '~/data/constants';

export default {
  name: "page_footer",
  data() {
    return {
      /* Links. */

      "repo_link"    : REPO_LINK,
      "site_link"    : SITE_LINK,
      "privacy_link" : PRIVACY_LINK,
      "terms_link"   : TERMS_LINK,
    }
  }
}

</script>
