import Player from "~/data/Player";
import Game from "~/data/Game";

/**
 * A data representation for a user's meme.
 */
export default interface Meme {
  /** The URL for the meme created. */
  url: string,

  /** The integer ID of the player who created this meme. */
  player: Player,

  /** The game the meme was created in. */
  game: Game,
}
