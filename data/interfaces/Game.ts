import Player from "~/data/interfaces/Player";
import MemeTemplate from "~/data/interfaces/MemeTemplate";
import GameState from "~/data/structs/GameState";

export default interface Game {
  /** The room key for the app. Read-only. */
  room_key: string,

  /** The meme templates for the app. Read-only. */
  meme_templates: MemeTemplate[],

  /** The privileged VIP player of the app. Read-only. */
  vip: Player,

  /** The VIP player of the app to send to the server when creating lobbies. Write-only. */
  vip_name: string,

  /*
   * Options.
   */

  /** The max allowed players in this app. Read/write. */
  max_players_allowed: number,

  /** The time per turn. Read/write. */
  time_per_turn: number,

  /** The max number of rounds for this app. Read/write. */
  max_rounds: number,

  /*
   * State.
   */

  /** Time until the next state. Read-only. */
  time_until_next_state: number,

  /** The current round. */
  round: number,

  /** Game state. */
  state: GameState,

  /** Players in the server. */
  players: Player[],
}
