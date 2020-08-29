<template lang="pug">
  div.column(style="padding-top: 15vh").has-text-centered
    div
      p.subtitle.has-text-weight-bold SETTINGS
      br
      br
      div.container
        div.field.is-horizontal
          div.field-label.is-normal
            label.label ROUNDS
          div.field-body
            div.field
              p.control
                input.input(type="input" value="10")
        div.field.is-horizontal
          div.field-label.is-normal
            label.label TIME
          div.field-body
            div.field
              p.control
                input.input(type="input" value="80")
        div.field.is-horizontal
          div.field-label.is-normal
            label.label OTHER
          div.field-body
            div.field
              p.control
                input.input(type="input")
        div.field.is-horizontal
          div.field-label.is-normal
            label.label MAX PLAYERS
          div.field-body
            div.field
              p.control
                input.input(type="input" value="16")
</template>

<script>
export default {
  name: "settingsPanel"
}
</script>

<style scoped>

</style>
