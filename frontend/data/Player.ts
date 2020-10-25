// TODO: I should use Django Typomatic for this.

export default interface Player {
  /**
   * A user's name.
   */
  name: string,
  /**
   * Whether this user has readied up or has completed drawing in a round, depending on context.
   */
  ready: boolean,
  /**
   * Whether this user has VIP access to elements of the page.
   *
   * Note: there is no client-side security. While the interface may be different for VIP users
   * compared to normal users, the backend will still verify if the provided information
   * pertains to the correct user.
   */
  vip: boolean,
  /**
   * The score this player has in this game.
   */
  score: number,
}
