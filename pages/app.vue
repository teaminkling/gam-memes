<template lang="pug">

  div#app
    div.columns
      col_00_state_00_name_assign(
        v-if="GameState.CREATING_STATE === current_game_state"
      )

      col_00_state_01_lobby(
        v-if="GameState.WAITING_FOR_PLAYERS_STATE === current_game_state"
      )

      col_00_state_02_03_04_players(
        v-if=`[
          GameState.FORGING_MEMES_STATE,
          GameState.JUDGING_MEMES_STATE,
          GameState.PRESENTING_WINNERS_STATE,
        ].includes(current_game_state)`
      )

      col_01_state_00_join_room(
        v-if="GameState.CREATING_STATE === current_game_state"
      )

      col_01_state_01_settings(
        v-if="GameState.WAITING_FOR_PLAYERS_STATE === current_game_state"
      )

      col_02_state_00_game_creator(
        v-if="GameState.CREATING_STATE === current_game_state"
      )

      col_02_state_01_room_code(
        v-if="GameState.WAITING_FOR_PLAYERS_STATE === current_game_state"
      )

      col_03_state_02_editor(
        v-if="GameState.FORGING_MEMES_STATE === current_game_state"
      )

      col_03_state_03_judgement(
        v-if="GameState.JUDGING_MEMES_STATE === current_game_state"
      )

      col_03_state_04_awards(
        v-if="GameState.PRESENTING_WINNERS_STATE === current_game_state"
      )

</template>

<script lang="ts">

import col_00_state_02_03_04_players from "~/components/app/col_00_state_02_03_04_players.vue";
import col_00_state_01_lobby from "~/components/app/col_00_state_01_lobby.vue";
import col_00_state_00_name_assign from "~/components/app/col_00_state_00_name_assign.vue";

import col_01_state_00_join_room from "~/components/app/col_01_state_00_join_room.vue";
import col_01_state_01_settings from "~/components/app/col_01_state_01_settings.vue";

import col_02_state_00_game_creator from "~/components/app/col_02_state_00_game_creator.vue";
import col_02_state_01_room_code from "~/components/app/col_02_state_01_room_code.vue";

import col_03_state_02_editor from "~/components/app/col_03_state_02_editor.vue";
import col_03_state_03_judgement from "~/components/app/col_03_state_03_judgement.vue";
import col_03_state_04_awards from "~/components/app/col_03_state_04_awards.vue";

import GameState from "~/data/structs/GameState";

import { appModuleStore } from '@/store';

export default {
  name: 'app',
  layout: 'base',
  components: {
    col_00_state_00_name_assign,
    col_00_state_01_lobby,
    col_00_state_02_03_04_players,
    col_01_state_00_join_room,
    col_01_state_01_settings,
    col_02_state_00_game_creator,
    col_02_state_01_room_code,
    col_03_state_02_editor,
    col_03_state_03_judgement,
    col_03_state_04_awards,
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
