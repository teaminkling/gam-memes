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
            input.input.is-large.is-rounded.has-text-centered(type="input" value="10")

        div.field.settings-field
          label.label.is-medium
            | Seconds per Template
          div.settings-input
            input.input.is-large.is-rounded.has-text-centered(type="input" value="60")

        div.field.settings-field
          label.label.is-medium
            | Player Limit
          div.settings-input
            input.input.is-large.is-rounded.has-text-centered(type="input" value="8")
</template>

<script lang="ts">
export default {
  name: "settingsPanel"
}
</script>

<style scoped>

</style>
