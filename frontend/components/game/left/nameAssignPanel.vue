<template lang="pug">
  div.panel-parent.column.has-text-centered
    div.create-pad
      div.field.settings-field
        label.label.is-large
          | Name
        div.settings-input
          input.input.is-large.is-rounded.has-text-centered(type="input" placeholder="Your name.")
</template>

<script lang="ts">
export default {
  name: "nameAssignPanel"
}
</script>

<style scoped>

</style>
