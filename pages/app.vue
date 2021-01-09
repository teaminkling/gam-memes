<template lang="pug">

  div#app
    // This part of the app determines which panel components to show.

    div.columns
      // Left panel.

      name_assign_panel(
        v-if="GameState.CREATING_STATE === current_game_state"
      )

      lobby_panel(
        v-if="GameState.WAITING_FOR_PLAYERS_STATE === current_game_state"
      )

      in_game_players_panel(
        v-if=`[
          GameState.FORGING_MEMES_STATE, GameState.JUDGING_MEMES_STATE, GameState.PRESENTING_WINNERS_STATE,
        ].includes(current_game_state)`
      )

      // Middle panel.

      join_room_panel(
        v-if="GameState.CREATING_STATE === current_game_state"
      )

      settings_panel(
        v-if="GameState.WAITING_FOR_PLAYERS_STATE === current_game_state"
      )

      // Right panel.

      game_creation_panel(
        v-if="GameState.CREATING_STATE === current_game_state"
      )

      room_code_panel(
        v-if="GameState.WAITING_FOR_PLAYERS_STATE === current_game_state"
      )

      // Large right panel.

      editor_panel(
        v-if="GameState.FORGING_MEMES_STATE === current_game_state"
      )

      judging_panel(
        v-if="GameState.JUDGING_MEMES_STATE === current_game_state"
      )

      winner_panel(
        v-if="GameState.PRESENTING_WINNERS_STATE === current_game_state"
      )

</template>

<script lang="ts">

/* Left. */

import in_game_players_panel from "~/components/game/left/in_game_players_panel.vue";
import lobby_panel from "~/components/game/left/lobby_panel.vue";
import name_assign_panel from "~/components/game/left/name_assign_panel.vue";

/* Middle. */

import join_room_panel from "~/components/game/middle/join_room_panel.vue";
import settings_panel from "~/components/game/middle/settings_panel.vue";

/* Right. */

import editor_panel from "~/components/game/right/editor_panel.vue";
import game_creation_panel from "~/components/game/right/game_creation_panel.vue";
import judging_panel from "~/components/game/right/judging_panel.vue";
import room_code_panel from "~/components/game/right/room_code_panel.vue";
import winner_panel from "~/components/game/right/winner_panel.vue";

/* Store/state. */

import GameState from "@/data/GameState";

import { appModuleStore } from '@/store';

export default {
  name: 'app',
  layout: 'base',
  components: {
    winner_panel,
    settings_panel,
    room_code_panel,
    lobby_panel,
    judging_panel,
    join_room_panel,
    in_game_players_panel,
    game_creation_panel,
    editor_panel,
    name_assign_panel
  },
  computed: {
    current_game_state(): GameState {
      /* Allow read-only access to the current state to determine what panels to show. */

      return appModuleStore.game_state;
    },
  },
  data() {
    return {
      /* Allow template to use GameState enum. */

      GameState,
    }
  },
};

</script>
