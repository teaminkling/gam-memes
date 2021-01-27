<template lang="pug">

  div.panel-parent.column.has-text-centered
    div
      h1.title.panel-header
        | Game Settings

      div.container.has-text-left
        div.field.ui-field
          label.label.is-medium
            | Rounds per Game
          div.ui-field
            input.input.is-large.is-rounded.has-text-centered(
              type="input", value="10", @blur="update_rounds_per_game"
            )

        div.field.ui-field
          label.label.is-medium
            | Seconds per Template
          div.ui-field
            input.input.is-large.is-rounded.has-text-centered(
              type="input" value="60", @blur="update_seconds_per_template"
            )

        div.field.ui-field
          label.label.is-medium
            | Player Limit
          div.ui-field
            input.input.is-large.is-rounded.has-text-centered(
              type="input" value="8", @blur="update_player_limit"
            )

</template>

<script lang="ts">

// import { appModuleStore } from '~/store';

export default {
  name: "col_01_state_01_settings",
  methods: {
    update_rounds_per_game(_event: { target: HTMLInputElement }) {
      /* Update the room code in the state when the code field is unfocused. */

      // appModuleStore.set_rounds_per_game(event.target.value);
    },
    update_seconds_per_template(_event: { target: HTMLInputElement }) {
      /* Update the room code in the state when the code field is unfocused. */

      // appModuleStore.set_seconds_per_template(event.target.value);
    },
    update_player_limit(_event: { target: HTMLInputElement }) {
      /* Update the room code in the state when the code field is unfocused. */

      // appModuleStore.set_player_limit(event.target.value);
    },
  }
}

</script>

<style scoped>

</style>
