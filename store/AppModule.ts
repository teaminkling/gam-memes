import { Module, Mutation, VuexModule } from "vuex-module-decorators";

import Player from "~/data/Player";
import GameState from "~/data/GameState";

/**
 * Define the states and mutations on that states that are possible for the application.
 */
@Module({ name: "AppModule", stateFactory: true, namespaced: true })
export default class AppModule extends VuexModule {
  /* The player's authentication name. */

  current_player: Player = { name: "", ready: false, vip: false, score: 0.0 };

  /* Room code used to authenticate along with user name. */

  room_code: string = "";

  /* Players currently in the client's game (not including the current player). */

  players: Player[] = [];

  /* Game client state. */

  game_state: GameState = GameState.CREATING_STATE;

  /* Memes and their associated votes. Not sent to the server; allows pre-fetching of results. */

  memes: any[] = [];

  @Mutation
  set_name(name: string) {
    this.current_player.name = name;
  }

  @Mutation
  set_room_code(room_code: string) {
    this.room_code = room_code;
  }

  @Mutation
  set_state(state: GameState) {
    this.game_state = state;
  }
}
