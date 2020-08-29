<template lang="pug">
  div#index
    h1 this is the index

    nuxt-link(to="app") go to app
</template>

<script>
import feet from '../components/web/feet';

export default {
  name: 'index',
  layout: 'base',
  components: {
    feet,
  }
}
</script>
