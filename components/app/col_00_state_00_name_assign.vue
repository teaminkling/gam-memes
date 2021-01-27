<template lang="pug">

  // A name must be present for joining and for creating games.

  div.panel-parent.column.has-text-centered
    div.create-pad
      div.field.ui-field
        label.label.is-large
          | Name
        div.ui-field
          input#name-input.input.is-large.is-rounded.has-text-centered(
            type="input", placeholder="Your name.", @blur="update_name"
          )

</template>

<script lang="ts">

import { appModuleStore } from '~/store';

export default {
  name: "col_00_state_00_name_assign",
  methods: {
    update_name(event: { target: HTMLInputElement }) {
      /* Update the player's name in the state when the name field is unfocused. */

      appModuleStore.set_name(event.target.value);
    }
  },
}

</script>
