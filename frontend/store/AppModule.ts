import { Module, Mutation, VuexModule } from 'vuex-module-decorators';

import Player from "~/data/Player";
import GameState from "~/data/GameState";

/**
 * Define the states and mutations on that states that are possible for the application.
 */

@Module({name: 'AppModule', stateFactory: true, namespaced: true})
export default class AppModule extends VuexModule {
  /* The player's authentication name. */

  currentPlayer: Player = {"name": "", ready: false, vip: false, score: 0.0};

  /* Room code used to authenticate along with user name. */

  roomCode: string = "";

  /* Players currently in the client's game and the players' meta-information. */

  players: Player[] = [];

  /* Game client state. */

  gameState: GameState = GameState.CREATING_STATE;

  /* Memes and their associated votes. Not sent to the server; allows pre-fetching of results. */

  memes: any[] = [];

  @Mutation
  setName(name: string) {
    this.currentPlayer.name = name;
  }

  @Mutation
  setState(state: GameState) {
    this.gameState = state;
  }
}
