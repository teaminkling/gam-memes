<template lang="pug">
  div.column
    br
    br
    div#tui(style="width: 800px; height: 600px; margin: 0;")
      tui(ref="editor" :include-ui="true" :options="options")
</template>

<script>
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
      options: { // for tui-image-editor component's "options" prop
        includeUI: {
          initMenu: 'filter',
          menuBarPosition: 'bottom'
        },
        cssMaxWidth: 600,
        cssMaxHeight: 400,
      }
    };
  },
}
</script>
