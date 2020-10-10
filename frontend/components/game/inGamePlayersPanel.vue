<template lang="pug">
  div.panel-parent.column.has-text-centered.is-one-quarter
    div
      h1.title.panel-header
        | Artists Playing

      div.has-text-left
        div.container
          table.table.is-striped.is-hoverable.is-fullwidth
            tbody
              tr
                td.name TEST
                td.ready DONE
                td.score 11
              tr
                td.name TEST
                td.ready
                td.score 6
              tr
                td.name TEST
                td.ready
                td.score 2
              tr
                td.name TEST
                td.ready
                td.score 2
              tr
                td.name TEST
                td.ready DONE
                td.score 1
              tr
                td.name TEST
                td.ready DONE
                td.score 0

      p.count Waiting on #[b 3] players!
</template>

<script>
export default {
  name: "inGamePlayersPanel"
}
</script>

<style scoped>
.name {
  width: 90%;
}

.ready {
  width: 5%;

  font-weight: bold;
  color: forestgreen;
}

.score {
  width: 5%;
}

.count {
  padding: 1.5em;
}
</style>
