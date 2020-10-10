<template lang="pug">
  div#app
    button.button(@click="mutateState(GameState.CREATING_STATE)") CREATING
    button.button(@click="mutateState(GameState.WAITING_FOR_PLAYERS_STATE)") WAITING_FOR_PLAYERS
    button.button(@click="mutateState(GameState.FORGING_MEMES_STATE)") FORGING_MEMES
    button.button(@click="mutateState(GameState.JUDGING_MEMES_STATE)") JUDGING_MEMES
    button.button(@click="mutateState(GameState.PRESENTING_WINNERS_STATE)") PRESENTING_WINNERS

    // This part of the app determines which panel components to show.

    div.columns
      name-assign-panel(v-if="GameState.CREATING_STATE === currentGameState")

      lobby-panel(v-if="GameState.WAITING_FOR_PLAYERS_STATE === currentGameState")

      in-game-players-panel(
        v-if=`[
          GameState.FORGING_MEMES_STATE,
          GameState.JUDGING_MEMES_STATE,
          GameState.PRESENTING_WINNERS_STATE,
        ].includes(currentGameState)`
      )

      join-room-panel(v-if="GameState.CREATING_STATE === currentGameState")

      settings-panel(v-if="GameState.WAITING_FOR_PLAYERS_STATE === currentGameState")

      game-creation-panel(v-if="GameState.CREATING_STATE === currentGameState")

      room-code-panel(v-if="GameState.WAITING_FOR_PLAYERS_STATE === currentGameState")

      editor-panel(v-if="GameState.FORGING_MEMES_STATE === currentGameState")

      judging-panel(v-if="GameState.JUDGING_MEMES_STATE === currentGameState")

      winner-panel(v-if="GameState.PRESENTING_WINNERS_STATE === currentGameState")
</template>

<script lang="ts">
import NameAssignPanel from "@/components/game/nameAssignPanel.vue";
import EditorPanel from "@/components/game/editorPanel.vue";
import GameCreationPanel from "@/components/game/gameCreationPanel.vue";
import InGamePlayersPanel from "@/components/game/inGamePlayersPanel.vue";
import JoinRoomPanel from "@/components/game/joinRoomPanel.vue";
import JudgingPanel from "@/components/game/judgingPanel.vue";
import LobbyPanel from "@/components/game/lobbyPanel.vue";
import RoomCodePanel from "@/components/game/roomCodePanel.vue";
import SettingsPanel from "@/components/game/settingsPanel.vue";
import WinnerPanel from "@/components/game/winnerPanel.vue";

import { GameState } from "@/data/GameState";
import { appModule } from '@/store';

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
      return appModule.gameState;
    },
  },
  data() {
    return {
      /* Allow template to use GameState enum. */

      GameState,
    }
  },
  methods: {
    // TODO: Remove this when debugging without the console is no longer required.

    mutateState(newState: GameState) {
      appModule.setState(newState);
    }
  }
};
</script>
