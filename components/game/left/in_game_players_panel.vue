<template lang="pug">

  div.panel-parent.column.has-text-centered.is-one-quarter
    div
      h1.title.panel-header
        | Artists Playing

      div.has-text-left
        div.container
          table.table.is-striped.is-hoverable.is-fullwidth
            tbody(v-for="player in players")
              tr
                td.name {{ player.name }}
                td.ready
                  p(v-if="player.ready === true") Done
                td.score {{ player.score }}
      div(v-if="remaining")
        p.count Waiting on {{ remaining }} players!

</template>

<script lang="ts">

import { appModuleStore } from '@/store';

import Player from "~/data/Player";

export default {
  name: "in_game_players_panel",
  computed: {
    players() {
      return appModuleStore.players;
    },
    remaining() {
      /* We only check for falseyness of the ready value, not explicitly "Ready". */

      return appModuleStore.players.filter((player: Player) => !player.ready).length;
    },
  }
}

</script>

<style scoped>

.name {
  width: 90%;
}

.ready {
  width: 5%;

  font-weight: bold;
  color: forestgreen;
}

.score {
  width: 5%;
}

.count {
  padding: 1.5em;
}

</style>
