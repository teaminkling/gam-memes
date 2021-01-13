/**
 * A read-only interface for a meme template.
 */
export default interface MemeTemplate {
  /** A direct URL to an image. */
  url: string,

  /** The number of likes for this template. */
  likes: number,

  /** The number of dislikes for this template. */
  dislikes: number,
}
