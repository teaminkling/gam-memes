<template lang="pug">

  div.panel-parent.column.has-text-centered
    div
      h1.title.panel-header
        | Game Settings

      div.container.has-text-left
        div.field.settings-field
          label.label.is-medium
            | Rounds per Game
          div.settings-input
            input.input.is-large.is-rounded.has-text-centered(
              type="input", value="10", @blur="update_rounds_per_game"
            )

        div.field.settings-field
          label.label.is-medium
            | Seconds per Template
          div.settings-input
            input.input.is-large.is-rounded.has-text-centered(
              type="input" value="60", @blur="update_seconds_per_template"
            )

        div.field.settings-field
          label.label.is-medium
            | Player Limit
          div.settings-input
            input.input.is-large.is-rounded.has-text-centered(
              type="input" value="8", @blur="update_player_limit"
            )

</template>

<script lang="ts">

import { appModuleStore } from '@/store';

export default {
  name: "settings_panel",
  methods: {
    update_rounds_per_game(event: { target: HTMLInputElement }) {
      /* Update the room code in the state when the code field is unfocused. */

      appModuleStore.set_rounds_per_game(event.target.value);
    },
    update_seconds_per_template(event: { target: HTMLInputElement }) {
      /* Update the room code in the state when the code field is unfocused. */

      appModuleStore.set_seconds_per_template(event.target.value);
    },
    update_player_limit(event: { target: HTMLInputElement }) {
      /* Update the room code in the state when the code field is unfocused. */

      appModuleStore.set_player_limit(event.target.value);
    },
  }
}

</script>

<style scoped>

</style>
