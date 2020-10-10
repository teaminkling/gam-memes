export enum GameState {
  /**
   * User can see three panels: name assignment table, join room code, and new game creation panel.
   * At the bottom of the page, a "how to play" button is present.
   */
  CREATING_STATE,

  /**
   * User can see three panels: lobby panel, settings panel, and room code/start game panel. The
   * same "how to play" button remains on the screen.
   */
  WAITING_FOR_PLAYERS_STATE,

  /**
   * User can see two panels: in-game panel, and the editor panel. The editor panel is far larger
   * than the lobby panel. The in-game panel is nearly identical to the lobby panel, but each
   * player has current points shown as well as ready status (i.e., they are done with the editing).
   */
  FORGING_MEMES_STATE,

  /**
   * User can see two panels: in-game panel, and the judging panel. The in-game panel is identical
   * to the one in FORGING_MEMES, except all players will be marked "ready". It is meant to be
   * zero-distraction. The judging panel is similar to the editor except it displays all the
   * memes with a carousel to move left and right. A button appears on the bottom of the meme
   * with the text "ASSIGN YOUR VOTE" if you still have a vote, "REASSIGN YOUR VOTE" if you have
   * already voted, and "REMOVE YOUR VOTE" if you're on the meme you voted on.
   */
  JUDGING_MEMES_STATE,

  /**
   * Users can see two panels: in-game panel, and the winner panel. The winner panel only displays
   * the winner with the name of the winner with their vote tally. In this phase, the number of
   * points other players have won in the delta will be displayed in the in-game panel.
   */
  PRESENTING_WINNERS_STATE,
}
