<template lang="pug">
  div#index
    div(class="container")
      h1 this is the index

      nuxt-link(to="app") go to app

      feet
</template>

<script>
import feet from '../components/web/feet';

export default {
  name: 'index',
  components: {
    feet,
  }
}
</script>
