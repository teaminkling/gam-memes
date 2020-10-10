<template lang="pug">
  div.panel-parent.column.has-text-centered
    div.create-pad
      div.field.settings-field
        label.label.is-large
          | Join Lobby
        div.settings-input
          input.input.is-large.is-rounded.has-text-centered(type="input" placeholder="Room Code.")
        div.join-pad
          button.button.is-success.is-large.is-rounded.is-outlined Join
</template>

<script lang="ts">
export default {
  name: "joinRoomPanel"
}
</script>

<style scoped>
.join-pad {
  margin-top: 3em;
}
</style>
