<template lang="pug">

  // A name must be present for joining and for creating games.

  div.panel-parent.column.has-text-centered
    div.create-pad
      div.field.settings-field
        label.label.is-large
          | Name
        div.settings-input
          input#name-input.input.is-large.is-rounded.has-text-centered(
            type="input", placeholder="Your name.", @blur="update_name"
          )

</template>

<script lang="ts">

import { appModuleStore } from '@/store';

export default {
  name: "name_assign_panel",
  methods: {
    update_name(event: { target: HTMLInputElement }) {
      /* Update the player's name in the state when the name field is unfocused. */

      appModuleStore.set_name(event.target.value);
    }
  },
}

</script>
