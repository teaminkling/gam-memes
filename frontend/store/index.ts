/**
 * Allow access to the Vuex store from elsewhere in the app.
 *
 * We load an empty store at first and dynamically register modules at a later point.
 */

import { Store } from 'vuex';
import { getModule } from 'vuex-module-decorators'

import AppModule from "~/store/modules/AppModule";

/* Define the modules for the store at the top-level of the store index. */

let appModule: AppModule;

/* Define an initialiser for the modules. */

function initializer(store: Store<any>) : void {
  appModule = getModule(AppModule, store);
}

/* Export the initializer as a plugin. */

export const plugins = [initializer];

/* Re-export the modules such that they can be imported from the store. */

export { appModule };
