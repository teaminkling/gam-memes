import { Module, VuexModule, Mutation } from 'vuex-module-decorators';

import { GameState } from "~/data/GameState";

/**
 * Define the states and mutations on that states that are possible for the application.
 */

@Module({
  name: 'appStore', stateFactory: true, namespaced: true,
})
export default class AppModule extends VuexModule {
  /* The player's authentication name. */

  playerName: string = "";

  /* Room code used to authenticate along with user name. */

  roomCode: string = "";

  /* Players currently in the client's game and the players' meta-information. */

  players: any[] = [];

  /* Game client state. */

  gameState: GameState = GameState.CREATING_STATE;

  /* Memes and their associated votes. Not sent to the server; allows pre-fetching of results. */

  memes: any[] = [];

  @Mutation
  setName(name: string) {
    this.playerName = name;
  }

  @Mutation
  setState(state: GameState) {
    this.gameState = state;
  }

  get getGameState() {
    return this.gameState
  }
}
