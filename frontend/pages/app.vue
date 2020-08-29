<template lang="pug">
  div#app
    p set state to:&nbsp
      button.button(@click="gameState = 'CREATING'") CREATING
      button.button(@click="gameState = 'WAITING_FOR_PLAYERS'") WAITING_FOR_PLAYERS
      button.button(@click="gameState = 'FORGING_MEMES'") FORGING_MEMES
      button.button(@click="gameState = 'JUDGING_MEMES'") JUDGING_MEMES
      button.button(@click="gameState = 'PRESENTING_WINNERS'") PRESENTING_WINNERS
    p "{{ gameState }}" is the current game state.
    div.columns
      name-assign-panel(
        v-if="['CREATING'].includes(gameState)"
      )

      lobby-panel(
        v-if="['WAITING_FOR_PLAYERS'].includes(gameState)"
      )

      in-game-players-panel(
        v-if="['FORGING_MEMES', 'JUDGING_MEMES', 'PRESENTING_WINNERS'].includes(gameState)"
      )

      join-room-panel(
        v-if="['CREATING'].includes(gameState)"
      )

      settings-panel(
        v-if="['WAITING_FOR_PLAYERS'].includes(gameState)"
      )

      game-creation-panel(
        v-if="['CREATING'].includes(gameState)"
      )

      room-code-panel(
        v-if="['WAITING_FOR_PLAYERS'].includes(gameState)"
      )

      editor-panel(
        v-if="['FORGING_MEMES'].includes(gameState)"
      )

      judging-panel(
        v-if="['JUDGING_MEMES'].includes(gameState)"
      )

      winner-panel(
        v-if="['PRESENTING_WINNERS'].includes(gameState)"
      )
</template>

<script>
/**
 * This is the main app logic page for the client application. There is a game state on the backend that is synced and
 * reflected by this Vue client.
 *
 * States influence the components seen on the page.
 *
 * - CREATING
 *
 * User can see three panels: name assignment table, join room code, and new game creation panel. At the bottom of the
 * page, a "how to play" button is present.
 *
 * - WAITING_FOR_PLAYERS
 *
 * User can see three panels: lobby panel, settings panel, and room code/start game panel. The same "how to play"
 * button remains on the screen.
 *
 * - FORGING_MEMES
 *
 * User can see two panels: in-game panel, and the editor panel. The editor panel is far larger than the lobby panel.
 * The in-game panel is nearly identical to the lobby panel, but each player has current points shown as well as ready
 * status (i.e., they are done with the editing).
 *
 * - JUDGING_MEMES
 *
 * User can see two panels: in-game panel, and the judging panel. The in-game panel is identical to the one in
 * FORGING_MEMES, except all players will be marked "ready". It is meant to be zero-distraction. The judging panel is
 * similar to the editor except it displays all the memes with a carousel to move left and right. A button appears on
 * the bottom of the meme with the text "ASSIGN YOUR VOTE" if you still have a vote, "REASSIGN YOUR VOTE" if you have
 * already voted, and "REMOVE YOUR VOTE" if you're on the meme you voted on.
 *
 * - PRESENTING_WINNERS
 *
 * Users can see two panels: in-game panel, and the winner panel. The winner panel only displays the winner with the
 * name of the winner with their vote tally. In this phase, the number of points other players have won in the delta
 * will be displayed in the in-game panel.
 *
 * That means there are the following panels:
 *
 * - `nameAssignPanel`
 * - `joinRoomPanel`
 * - `gameCreationPanel`
 * - `lobbyPanel`
 * - `settingsPanel`
 * - `roomCodePanel`
 * - `inGamePlayersPanel`
 * - `editorPanel` (67% of the play area)
 * - `judgingPanel` (67% of the play area)
 * - `winnerPanel` (67% of the play area)
 */

import { CREATING_STATE } from '@/constants/state'

import NameAssignPanel from "@/components/game/nameAssignPanel";
import EditorPanel from "@/components/game/editorPanel";
import GameCreationPanel from "@/components/game/gameCreationPanel";
import InGamePlayersPanel from "@/components/game/inGamePlayersPanel";
import JoinRoomPanel from "@/components/game/joinRoomPanel";
import JudgingPanel from "@/components/game/judgingPanel";
import LobbyPanel from "@/components/game/lobbyPanel";
import RoomCodePanel from "@/components/game/roomCodePanel";
import SettingsPanel from "@/components/game/settingsPanel";
import WinnerPanel from "@/components/game/winnerPanel";

export default {
  name: 'app',
  layout: 'base',
  components: {
    WinnerPanel,
    SettingsPanel,
    RoomCodePanel,
    LobbyPanel,
    JudgingPanel, JoinRoomPanel, InGamePlayersPanel, GameCreationPanel, EditorPanel, NameAssignPanel},
  data() {
    return {
      /* The player's authentication name. */

      playerName: null,

      /* Room code used to authenticate along with user name. */

      roomCode: null,

      /* Players currently in the client's game and the players' meta-information. */

      players: [],

      /* Game client state. */

      gameState: null,

      /* Memes and their associated votes. Not sent to the server, but allows pre-fetching of results page. */

      memes: [],
    }
  },
  methods: {

  },
  mounted() {
    /*
     * Start with the default game state.
     *
     * If you leave the page navigation, you always need to re-auth.
     *
     * States include:
     *
     * - CREATING
     * - WAITING_FOR_PLAYERS
     * - FORGING_MEMES
     * - JUDGING_MEMES
     * - PRESENTING_WINNERS
     *
     * Note these have parity with the backend server. Also, note that "CREATING" can also mean "about to join."
     */

    this.gameState = CREATING_STATE;
  }
};
</script>
