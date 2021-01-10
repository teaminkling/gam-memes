export interface MemeTemplateSerializer {
    url: string;
    likes?: number;
    dislikes?: number;
}

export interface UserMemeSerializer {
    url?: string;
    player?: any;
}

export interface PlayerSerializer {
    name: string;
    game: any;
    ready?: boolean;
    score?: number;
    latest_meme: UserMemeSerializer;
}

export interface GameSerializer {
    room_key?: string;
    meme_templates?: MemeTemplateSerializer[];
    max_players_allowed: number;
    time_per_turn: number;
    max_rounds: number;
    time_until_next_state?: any;
    round?: number;
    state?: any;
    player_set?: PlayerSerializer[];
    vip?: PlayerSerializer;
    vip_name: string;
}

