<template lang="pug">
  div#feet
    footer(class="footer")
      div(class="content has-text-centered")
        p Copyright #[b Inkling Interactive] &#169; 2020 - {{ new Date().getFullYear() }}.
        p Source on #[fa(:icon=['fab', 'github'])] #[a(:href="githubRepoLink", target="__blank") GitHub].
</template>

<script>
import { APACHE_2_0_LINK, GITHUB_REPO_LINK } from '@/constants/social';

export default {
  name: "feet",
  data() {
    return {
      "githubRepoLink": GITHUB_REPO_LINK,
      "apacheLicenseLink": APACHE_2_0_LINK,
    }
  }
}
</script>
