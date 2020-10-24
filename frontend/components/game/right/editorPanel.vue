<template lang="pug">
  div.panel-parent.column.has-text-centered
    div#tui(style="width: 100%; height: 64vh; margin: 0;")
      tui(ref="editor" :include-ui="true" :options="options")
</template>

<style scoped>
#tui {
  padding-top: 2em;
}
</style>

<script lang="ts">
import ImageEditor from '@toast-ui/vue-image-editor/src/ImageEditor.vue';

/* To use the included UI, just import the CSS. */

import 'tui-image-editor/dist/tui-image-editor.css';

export default {
  name: "editorPanel",
  components: {
    'tui': ImageEditor,
  },
  data() {
    return {
      options: {
        includeUI: {
          initMenu: 'text',
          menu: ["crop", "draw", "text", "icon"],
          menuBarPosition: 'bottom'
        },
      }
    };
  },
}
</script>
