<template lang="pug">

  // Joining a lobby requires a non-empty name and join code.

  div.panel-parent.column.has-text-centered
    div.create-pad
      div.field.settings-field
        label.label.is-large Join Lobby
        div.settings-input
          input.input.is-large.is-rounded.has-text-centered(
            type="input", placeholder="Room Code.", @blur="update_room_code"
          )
        div.join-pad
          button.button.is-success.is-large.is-rounded.is-outlined(@click="join_lobby") Join

</template>

<script lang="ts">

import { appModuleStore } from '@/store';

export default {
  name: "join_room_panel",
  methods: {
    update_room_code(event: { target: HTMLInputElement }) {
      /* Update the room code in the state when the code field is unfocused. */

      appModuleStore.set_room_code(event.target.value);
    },
    join_lobby() {
      /* Try to join the lobby if the state is valid. */

      if (!appModuleStore.room_code || !appModuleStore.current_player.name) {
        alert("Please supply both a name and room code.");
      } else {
        // TODO: Send POST request now. On promise completion, mutate the state.
      }
    }
  }
}

</script>

<style scoped>

.join-pad {
  margin-top: 3em;
}

</style>
