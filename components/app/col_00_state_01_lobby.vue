<template lang="pug">

  div.panel-parent.column.has-text-centered
    div
      h1.title.panel-header
        | Connected Players

      div.has-text-left
        div.container
          table.table.is-striped.is-hoverable.is-fullwidth
            // TODO: The current player must be in this list without needing a backend call.
            tbody(v-for="player in players")
              tr
                td.name {{ player.name }}
                td.ready {{ player.ready }}

      p.count
        | Total Players: <b>{{ players.length }}</b>

</template>

<script lang="ts">

import { appModuleStore } from '~/store';

export default {
  name: "col_00_state_01_lobby",
  computed: {
    players() {
      return appModuleStore.players;
    },
  }
}

</script>

<style scoped>

.name {
  width: 80%;
}

.ready {
  width: 20%;

  font-weight: bold;
  color: forestgreen;
}

.count {
  padding: 1.5em;
}

</style>
