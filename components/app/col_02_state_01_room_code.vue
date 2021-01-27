<template lang="pug">

  div.panel-parent.column.has-text-centered
    div
      p.title.panel-header
        | Room Code

      p.room-code.has-text-success
        | {{ roomCode }}
    div
      button.button.is-success.is-large.is-rounded.is-outlined.start(disabled)
        | Start
    div
      button.button.is-danger.is-large.is-rounded.is-outlined.disband
        | Disband
    div(v-if="remaining")
      p.ready-warning {{ remaining }} player(s) still need to ready up!

</template>

<style scoped>

.room-code {
  font-size: 96px;
  padding: 16px;
}

.start {
  margin-top: 10vh;
  padding: 0.5em;

  width: 8em;
}

.disband {
  margin-top: 2vh;
  padding: 0.5em;

  width: 8em;
}

.ready-warning {
  padding-top: 4em;
}

</style>

<script lang="ts">

import Player from "~/data/interfaces/Player";

import { appModuleStore } from '~/store';

export default {
  name: "col_02_state_01_room_code",
  computed: {
    remaining() {
      /* We only check for falseyness of the ready value, not explicitly "Ready". */

      return appModuleStore.players.filter((player: Player) => !player.ready).length;
    },
    roomCode() {
      return appModuleStore.room_code || "ERROR";
    }
  }
}

</script>
