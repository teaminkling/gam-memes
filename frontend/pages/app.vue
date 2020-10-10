<template lang="pug">
  div#app
    // This part of the app determines which panel components to show.
    // Contributors should use the Vue debugger to mutate the VueX state here.

    div.columns
      // Left panel.

      name-assign-panel(v-if="GameState.CREATING_STATE === currentGameState")
      lobby-panel(v-if="GameState.WAITING_FOR_PLAYERS_STATE === currentGameState")
      in-game-players-panel(
        v-if=`[
          GameState.FORGING_MEMES_STATE,
          GameState.JUDGING_MEMES_STATE,
          GameState.PRESENTING_WINNERS_STATE,
        ].includes(currentGameState)`
      )

      // Middle panel.

      join-room-panel(v-if="GameState.CREATING_STATE === currentGameState")
      settings-panel(v-if="GameState.WAITING_FOR_PLAYERS_STATE === currentGameState")

      // Right panel.

      game-creation-panel(v-if="GameState.CREATING_STATE === currentGameState")
      room-code-panel(v-if="GameState.WAITING_FOR_PLAYERS_STATE === currentGameState")

      // Large right panel.

      editor-panel(v-if="GameState.FORGING_MEMES_STATE === currentGameState")
      judging-panel(v-if="GameState.JUDGING_MEMES_STATE === currentGameState")
      winner-panel(v-if="GameState.PRESENTING_WINNERS_STATE === currentGameState")
</template>

<script lang="ts">
import NameAssignPanel from "~/components/game/left/nameAssignPanel.vue";
import EditorPanel from "~/components/game/right/editorPanel.vue";
import GameCreationPanel from "~/components/game/right/gameCreationPanel.vue";
import InGamePlayersPanel from "~/components/game/left/inGamePlayersPanel.vue";
import JoinRoomPanel from "~/components/game/middle/joinRoomPanel.vue";
import JudgingPanel from "~/components/game/right/judgingPanel.vue";
import LobbyPanel from "~/components/game/left/lobbyPanel.vue";
import RoomCodePanel from "~/components/game/right/roomCodePanel.vue";
import SettingsPanel from "~/components/game/middle/settingsPanel.vue";
import WinnerPanel from "~/components/game/right/winnerPanel.vue";

import GameState from "@/data/GameState";

import { appModuleStore } from '@/store';

export default {
  name: 'app',
  layout: 'base',
  components: {
    WinnerPanel,
    SettingsPanel,
    RoomCodePanel,
    LobbyPanel,
    JudgingPanel,
    JoinRoomPanel,
    InGamePlayersPanel,
    GameCreationPanel,
    EditorPanel,
    NameAssignPanel
  },
  computed: {
    currentGameState(): GameState {
      return appModuleStore.gameState;
    },
  },
  data() {
    return {
      /* Allow template to use GameState enum. */

      GameState,
    }
  },
};
</script>
