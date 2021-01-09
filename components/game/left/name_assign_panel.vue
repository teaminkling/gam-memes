<template lang="pug">

  // A name must be present for joining and for creating games.

  div.panel-parent.column.has-text-centered
    div.create-pad
      div.field.settings-field
        label.label.is-large
          | Name
        div.settings-input
          input#name-input.input.is-large.is-rounded.has-text-centered(
            type="input", placeholder="Your name."
          )

</template>

<script lang="ts">

export default {
  name: "name_assign_panel"
}

</script>

<style scoped>

</style>
