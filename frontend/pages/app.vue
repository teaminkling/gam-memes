<template lang="pug">
  div#app
    h1 game state is <{{ gameState }}>

    lobby
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
 */

import lobby from '@/components/game/lobby.vue';
import { CREATING_STATE } from '@/constants/state'

export default {
  name: 'app',
  components: {
    lobby,
  },
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
