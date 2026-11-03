import random

#============

AOT = [

    'Eren Yeager',
    'Mikasa Ackerman',
    'Armin Arlert',
    'Levi Ackerman',
    'Erwin Smith',
    'Hange Zoë',
    'Sasha Braus',
    'Jean Kirstein',
    'Connie Springer',
    'Historia Reiss',
    'Ymir',
    'Reiner Braun',
    'Bertolt Hoover',
    'Annie Leonhart',
    'Zeke Yeager',
    'Grisha Jaeger',
    'Carla Jaeger',
    'Kenny Akerman',
    'Hannes',
    'Dot Pixis',
    'Keith Shadis',
    'Marco Bott',
    'Floch Forster',
    'Pieck Finger',
    'Porco Galliard',
    'Colt Grice',
    'Gabi Braun',
    'Falco Grice',
    'Theo Magath',
    'Tom Ksaver',
    'Lara Tybur',
    'Ymir Fritz',
    'Flegel Reeves',
    'Kiyomi Azumabito',
    'Niccolo',
    'Yelena',
    'Onyankopon',

]

#============

JJK = [

    'Kento Nanami',
    'Mei Mei',
    'Ui Ui',
    'Toji Fushiguro',
    'Yuki Tsukumo',
    'Ryu Ishigori',
    'Hajime Kashimo',
    'Hiromi Higuruma',
    'Takuma Ino',
    'Naobito Zenin',
    'Naoya Zenin',
    'Ogi Zenin',
    'Jinichi Zenin',
    'Ranta Zenin',
    'Master Tengen',
    'Ryomen Sukuna',
    'Kenjaku',
    'Suguru Geto',
    'Uraume',
    'Haruta Shigemo',
    'Jiro Awasaka',
    'Juzo Kumiya',
    'Ogami',
    'Shiu Kong',
    'Larue',
    'Mimiko Hasaba',
    'Nanako Hasaba',
    'Junpei Yoshino',
    'Mahito',
    'Jogo',
    'Hanami',
    'Dagon',
    'Choso',
    'Eso',
    'Kechizu',
    'Kurourushi',
    'Rika Orimoto',

]

#============

MHA = [

    'Izuku Midoriya (Deku)',
    'Katsuki Bakugo (Great Explosion Murder God Dynamight)',
    'Ochaco Uraraka (Uravity)',
    'Shoto Todoroki (Shoto)',
    'Tenya Ida (Ingenium)',
    'All Might (Toshinori Yagi)',
    'Tomura Shigaraki (Tenko Shimura)',
    'All For One',
    'Eijiro Kirishima (Red Riot)',
    'Tsuyu Asui (Froppy)',
    'Momo Yaoyorozu (Creati)',
    'Fumikage Tokoyami (Tsukuyomi)',
    'Kyoka Jiro (Earphone Jack)',
    'Mina Ashido (Pinky)',
    'Denki Kaminari (Chargebolt)',
    'Mezo Shoji (Tentacole)',
    'Hanto Sero (Cellophane)',
    'Mashirao Ojiro (Tailman)',
    'Minoru Mineta (Grape Juice)',
    'Toru Hagakure (Invisible Girl)',
    'Koji Koda (Anima)',
    'Rikido Sato (Sugarman)',
    'Yuga Aoyama (Cant Stop Twinkling)',
    'Mirio Togata (Lemillion - The Big 3)',
    'Mei Hatsume (Support Course)',
    'Itsuka Kendo (Battle Fist)',
    'Neito Monoma (Phantom Thief)',
    'Endeavor (Enji Todoroki)',
    'Hawks (Keigo Takami)',
    'Eraser Head (Shota Aizawa)',
    'Best Jeanist (Tsunagu Hakamada)',
    'Gran Torino (Sorahiko Torino)',
    'Mirko (Rumi Usagiyama)',
    'Present Mic (Hizashi Yamada)',
    'Midnight (Nemuri Kayama)',
    'Nezu (Principal Nezu)',
    'Recovery Girl (Chiyo Shuzenji)',
    'Kamui Woods (Shinji Nishiya)',
    'Mt. Lady (Yu Takeyama)',
    'Fat Gum (Taishiro Toyomitsu)',
    'Sir Nighteye (Mirai Sasaki)',
    'Gang Orca (Kugo Sakamata)',
    'Dabi (Toya Todoroki)',
    'Himiko Toga',
    'Twice (Jin Bubaigawara)',
    'Kurogiri (Oboro Shirakumo)',
    'Overhaul (Kai Chisaki)',
    'Stain (Chizome Akaguro)',
    'Lady Nagant (Kaina Tsutsumi)',
    'Gentle Criminal (Danjuro Tobita)',
    'Muscular (Goto Imasuji)',
    'Eri',

]

#============

OPM = [

    'Saitama',
    'Genos',
    'Tatsumaki',
    'Fubuki',
    'Bang',
    'Garou',
    'King',
    "Speed-o'-Sound Sonic",
    'Atomic Samurai',
    'Metal Bat',
    'Child Emperor',
    'Zombieman',
    'Flashy Flash',
    'Mumen Rider',
    'Blast',
    'Bofoi',
    'Metal Knight',
    'Drive Knight',
    'Pig God',
    'Watchdog Man',
    'Superalloy Darkshine',
    'Tanktop Master',
    'Puri-Puri Prisoner',
    'Sweet Mask',
    'Amai Mask',
    'Boros',
    'Orochi',
    'Psykos',
    'Monster God',
    'Empty Void',
    'Suiryu',
    'Charanko',
    'Bomb',
    'Dr. Kuseno',
    'Dr. Genus',
    'Armored Gorilla',
    'Carnage Kabuto',
    'Vaccine Man',
    'Deep Sea King',
    'Melzargard',
    'Geryuganshoop',
    'Groribas',
    'Crablante',
    'Stinger',
    'Lightning Max',
    'Sneck',
    'Iaian',
    'Spring Mustachio',
    'Golden Ball',
    'Death Gatling',
    'Smile Man',
    'Blue Fire',
    'Heavy Tank Fundoshi',
    'Tanktop Tiger',
    'Tanktop Black Hole',
    'Gouketsu',
    'Elder Centipede',
    'Black Sperm',
    'Homeless Emperor',
    'Fuhrer Ugly',
    'Gums',
    'Nyan',
    'Phoenix Man',
    'Overgrown Rover',
    'Evil Natural Water',
    'G4',
    'G5',
    'Awakened Cockroach',
    'Bakuzan',
    'Choze',
    'Marshall Gorilla',
    'Rhino Wrestler',
    'Royal Ripper',
    'Bug God',
    'Pure Blood',
    'Freezer Man',
    'Slacker Sid',
    'Subterranean King',
    'Sky King',
    'Ancient King',
    'Deep Sea King',
    'Pluton',
    'Marugori',
    'Beefcake',
    'Fukegao',
    'Hammerhead',
    'Sonic',
    'Tareo',
    'Zenko',

]

#============

SL = [

    'Sung Jin-Woo (The Shadow Monarch)',
    "Sung Il-Hwan (Jin-Woo's Father / Vessel of the Rulers)",
    'Cha Hae-In (The Radiant Sword / S-Rank Hunter)',
    "Yoo Jin-Ho (Jin-Woo's Loyal Vice-Guild Master)",
    'Go Gun-Hee (The Association President / Sky Above the Sky)',
    'Thomas Andre (The Goliath / National Level Hunter)',
    'Liu Zhigang (The Hero of China / National Level Hunter)',
    'Christopher Reed (National Level Hunter / Vessel of the Rulers)',
    'Siddharth Bachchan (National Level Hunter)',
    'Jonas (National Level Hunter of Brazil)',
    'Choi Jong-In (The Ultimate Soldier / Master of Hunters Guild)',
    'Baek Yoon-Ho (The White Tiger / Guild Master)',
    'Min Byung-Gu (The Retired S-Rank Healer)',
    'Lim Tae-Gyu (Master of Fiend Guild)',
    'Ma Dong-Wook (Master of Fame Guild)',
    'Yoo Myung-Han (Chairman of Yoojin Construction)',
    "Park Heeo-Jin (B-Rank Mage / Jin-Woo's Early Party Member)",
    "Lee Ju-Hee (B-Rank Healer / Jin-Woo's Friend from the Double Dungeon)",
    'Song Chi-Yeul (C-Rank Mage / The Veteran Sword Elder)',
    'Kim Chul (Iron / High Orc Shadow / A-Rank Tanker)',
    'Hwang Dong-Su (Greed / S-Rank Traitor / Scavenger Guild)',
    "Hwang Dong-Suk (C-Rank Villain / Dong-Su's Brother)",
    'Woo Jin-Chul (The Surveillance Chief / Later Association President)',
    'Han Jae-Gu (A-Rank Hunter of White Tiger Guild)',
    'Kim Gu-Bhim (A-Rank Hunter of White Tiger Guild)',
    'Park Jong-Soo (Master of Knights Guild)',
    'Jeong Yun-Ki (Vice-Master of Knights Guild)',
    "Goto Ryuji (Japan's Strongest S-Rank Hunter)",
    'Reiji Sugimoto (Japanese S-Rank Hunter)',
    'Akari Shimizu (Japanese S-Rank Healer)',
    'Kenzo Tanaka (Japanese S-Rank Brawler)',
    'Kanae Tawata (Japanese S-Rank Assassin)',
    'Minoru Hoshino (Japanese S-Rank Hunter)',
    'Kei (Japanese S-Rank Ice Mage)',
    'Mari Ishida (Japanese S-Rank Hunter)',
    'Kumamoto (Japanese S-Rank Berserker)',
    'Yuri Orloff (The Russian S-Rank Barrier King)',
    "Lennart Niermann (Germany's Top S-Rank Hunter)",
    "Laura (Thomas Andre's Personal Manager)",
    'Selner (The Prophet / Madam Selner)',
    'David Brennon (Director of the Federal Bureau of Hunters)',
    'Gina (American S-Rank Hunter)',
    'Norris (American S-Rank Hunter)',
    'Brent (American S-Rank Hunter)',
    "Jong-Soo's Secretary (Knights Guild Staff)",
    "Sung Jin-Ah (Jin-Woo's Younger Sister)",
    "Park Kyung-Hye (Jin-Woo's Mother)",
    "Yoo Jin-Hee (Jin-Ho's Older Sister)",
    "Han Song-Yi (E-Rank Hunter / Jin-Ah's Friend)",
    "The Architect (The Creator of the System / Ashborn's Servant)",
    'Ashborn (The Original Shadow Monarch)',
    'Antares (The Monarch of Destruction / King of Dragons)',
    'Rakan (The Monarch of Fangs / King of Beasts)',
    'Baruka (The Monarch of White Flames / King of Snow Folk)',
    'Querehsha (The Monarch of Plagues / Queen of Insects)',
    'Yogumunt (The Monarch of Transmutation / King of Demonic Spectres)',
    'Tarnak (The Monarch of Iron Body / King of Monstrous Humanoids)',
    'Sillad (The Monarch of Frost / King of Snow Folk)',
    'Legia (The Monarch of the Beginning / King of Giants)',
    'Absolute Being (The Creator Creator of Monarchs and Rulers)',
    "Igris (The Blood Red Commander / Jin-Woo's Shadow)",
    "Beru (The Shadow Ant King / Jin-Woo's Shadow)",
    "Tusk (The High Orc Shaman Shadow / Jin-Woo's Shadow)",
    "Tank (The Ice Bear Shadow / Jin-Woo's Shadow)",
    "Kaisel (The Shadow Wyvern / Jin-Woo's Mount)",
    "Jima (The Naga Shadow / Jin-Woo's Shadow)",
    "Bellion (The Grand Marshal / Ashborn's Original Shadow)",
    "Kamish (The Shadow Dragon / Humanity's Greatest Calamity)",

]

#============

DL = [

    'Tanjirō Kamado',
    'Nezuko Kamado',
    'Zenitsu Agatsuma',
    'Inosuke Hashibira',
    'Kanao Tsuyuri',
    'Genya Shinazugawa',
    'Giyū Tomioka (Water Hashira)',
    'Shinobu Kochō (Insect Hashira)',
    'Kyōjurō Rengoku (Flame Hashira)',
    'Tengen Uzui (Sound Hashira)',
    'Mitsuri Kanroji (Love Hashira)',
    'Muichirō Tokitō (Mist Hashira)',
    'Gyōmei Himejima (Stone Hashira)',
    'Obanai Iguro (Serpent Hashira)',
    'Sanemi Shinazugawa (Wind Hashira)',
    'Muzan Kibutsuji (Demon King)',
    'Kokushibō (Upper Moon One)',
    'Dōma (Upper Moon Two)',
    'Akaza (Upper Moon Three)',
    'Hantengu (Upper Moon Four)',
    'Gyokko (Upper Moon Five)',
    'Gyūtarō (Upper Moon Six)',
    'Daki (Upper Moon Six)',
    'Kaigaku (Upper Moon Six)',
    'Nakime (Upper Moon Four)',
    'Enmu (Lower Moon One)',
    'Rui (Lower Moon Five)',
    'Kyōgai (Former Lower Moon Six)',
    'Sakonji Urokodaki (Former Water Hashira)',
    'Jigorō Kuwajima (Former Roaring Hashira)',
    'Shinjurō Rengoku (Former Flame Hashira)',
    'Kanae Kochō (Former Flower Hashira)',
    'Yoriichi Tsugikuni (Creator of Sun Breathing)',
    'Tamayo (Demon Doctor)',
    "Yushirō (Tamayo's Assistant)",
    'Murata (Demon Slayer Corps Member)',
    'Aoi Kanzaki (Butterfly Mansion Helper)',
    'Sumi Nakahara (Butterfly Mansion Helper)',
    'Kiyo Terauchi (Butterfly Mansion Helper)',
    'Naho Takada (Butterfly Mansion Helper)',
    'Sabo (Demon Slayer Cadet)',
    'Makomo (Demon Slayer Cadet)',
    'Hotaru Haganezuka (Swordsmith)',
    'Kozo Kanamori (Swordsmith)',
    'Kotetsu (Swordsmith Village Resident)',
    'Tecchin Tecchikawahara (Swordsmith Village Chief)',
    "Hinatsuru (Tengen's Wife)",
    "Makuo (Tengen's Wife)",
    "Suma (Tengen's Wife)",
    'Kagaya Ubuyashiki (Master of the Mansion)',
    "Amane Ubuyashiki (Kagaya's Wife)",
    "Kiriya Ubuyashiki (Kagaya's Son)",
    "Kanata Ubuyashiki (Kagaya's Daughter)",
    "Kuina Ubuyashiki (Kagaya's Daughter)",
    "Nichika Ubuyashiki (Kagaya's Daughter)",
    "Hinaki Ubuyashiki (Kagaya's Daughter)",
    'Susamaru (Temari Demon)',
    'Yahaba (Arrow Demon)',
    'Spider Demon Mother (Spider Family)',
    'Spider Demon Father (Spider Family)',
    'Spider Demon Brother (Spider Family)',
    'Spider Demon Sister (Spider Family)',
    'Hand Demon (Final Selection Demon)',
    "Kie Kamado (Tanjirō's Mother)",
    "Takeo Kamado (Tanjirō's Brother)",
    "Hanako Kamado (Tanjirō's Sister)",
    "Shigeru Kamado (Tanjirō's Brother)",
    "Rokuta Kamado (Tanjirō's Brother)",
    "Tanjūrō Kamado (Tanjirō's Father)",
    "Senjūrō Rengoku (Kyōjurō's Brother)",
    "Ruka Rengoku (Kyōjurō's Mother)",
    "Kotoha Hashibira (Inosuke's Mother)",
    "Yuichirō Tokitō (Muichirō's Twin Brother)",
    "Tsutako Tomioka (Giyū's Sister)",

]

#============

BL = [

    'Yoichi Isagi',
    'Meguru Bachira',
    'Rensuke Kunigami',
    'Hyoma Chigiri',
    'Rin Itoshi',
    'Sae Itoshi',
    'Seishiro Nagi',
    'Reo Mikage',
    'Zantetsu Tsurugi',
    'Shouei Barou',
    'Gin Gagamaru',
    'Jingo Raichi',
    'Gurimu Igarashi',
    'Asahi Naruhaya',
    'Wataru Kuon',
    'Okuhito Iemon',
    'Yudai Imamura',
    'Ryosuke Kira',
    'Jin Kiyora',
    'Ikki Niko',
    'Junichi Wanima',
    'Keisuke Wanima',
    'Ryusei Shidou',
    'Tabito Karasu',
    'Eita Otoya',
    'Kenyu Yukimiya',
    'Yo Hiyori',
    'Nijiro Nanase',
    'Kurona Ranze',
    'Aoshi Tokimitsu',
    'Jubei Aryu',
    'Anri Teieri',
    'Jinpachi Ego',
    'Yasuhito Fukaku',
    'Oliver Aiku',
    'Shuto Sendo',
    'Kazuma Niou',
    'Teppei Neru',
    'Kento Cho',
    'Teru Kitsunezato',
    'Itsuki Wakatsuki',
    'Haru Hayate',
    'Taiga Tsunzaki',
    'Miroku Darai',
    'Shingen Tanaka',
    'Noel Noa',
    'Chris Prince',
    'Lavinho',
    'Marc Snuffy',
    'Julian Loki',
    'Michael Kaiser',
    'Alexis Ness',
    'Benedict Grim',
    'Erik Gesner',
    'Mensah',
    'Birkenstock',
    'Agi',
    'Don Lorenzo',
    'Drago',
    'Charles Chevalier',
    'Leonardo Luna',
    'Pablo Cavasoz',
    'Adam Blake',
    'Dada Silva',

]

#============

ANIME_LISTS = {

    "AOT": AOT,
    "JJK": JJK,
    "MHA": MHA,
    "OPM": OPM,
    "SL": SL,
    "DL": DL,
    "BL": BL,

}

#============

def register_anime(short_name, characters):

    """Register an anime character list so it is included in every new shuffled pool.

    Example:

        register_anime("OP", OP)

    """
    key = short_name.strip().upper()
    if not key:
        raise ValueError("Anime name cannot be empty.")
    if key in ANIME_LISTS:
        raise ValueError(f"Anime list '{key}' is already registered.")
    if isinstance(characters, str):
        raise TypeError("characters must be a list of character names, not one string.")
    cleaned = [name.strip() for name in characters if isinstance(name, str) and name.strip()]
    if not cleaned:
        raise ValueError("Add at least one character name to the list.")
    ANIME_LISTS[key] = cleaned

#

STAT_SLOTS = [

    "Speed",
    "Intelligence",
    "Strength",
    "Defence",
    "Endurance",
    "Ability",
    "Willpower",
]

#

STARTING_BALANCE = 20

#

def make_character_pool():
    """Build and shuffle characters from every list registered in ANIME_LISTS."""
    pool = []
    for anime_name, characters in ANIME_LISTS.items():
        for character_name in characters:
            pool.append({
                "name": character_name,
                "anime": anime_name,
                "display": f"{character_name} [{anime_name}]",
            })
    random.shuffle(pool)
    return pool

import tkinter as tk
from tkinter import messagebox

#

#*GUI THEME*

BG = "#0b1020"
PANEL = "#141c31"
PANEL_ALT = "#1a2540"
ACCENT = "#7c9cff"
ACCENT_HOVER = "#9db4ff"
TEXT = "#edf2ff"
MUTED = "#a4b0cc"
GREEN = "#75e0b2"
RED = "#ff8795"
GOLD = "#ffd479"
PLAYER_COLORS = ("#ff5c6c", "#5ca8ff")

#
class Player:

    def __init__(self, name, balance=STARTING_BALANCE):

        self.name = name
        self.balance = balance
        self.build = {}
        self.consecutive_passes = 0
        self.force_next_pick = False

    #

    def has_empty_slots(self):
        return len(self.build) < len(STAT_SLOTS)

    #

    def next_slot(self):
        for slot in STAT_SLOTS:
            if slot not in self.build:
                return slot
        return None

    #

    def add_character(self, slot, character, cost=0):
        if slot in self.build:
            raise ValueError(f"{self.name} already has a character for {slot}.")
        if cost > self.balance:
            raise ValueError("The player cannot afford that amount.")
        self.balance -= cost
        self.build[slot] = {"character": character, "cost": cost}
        self.consecutive_passes = 0
        self.force_next_pick = False

#
def make_character_pool():
    pool = []
    for anime_name, characters in ANIME_LISTS.items():
        for character_name in characters:
            pool.append({
                "name": character_name,
                "anime": anime_name,
                "display": f"{character_name} [{anime_name}]",
            })
    random.shuffle(pool)
    return pool

#

class AnimeDraftGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Anime Character Draft")
        self.root.geometry("1180x790")
        self.root.minsize(980, 680)
        self.root.configure(bg=BG)
        self.players = []
        self.character_pool = make_character_pool()
        self.current_player_index = 0
        self.current_character = None
        self.current_slot = None
        self.high_bid = 0
        self.high_bidder_index = None
        self.game_finished = False
        self.show_setup()

    #

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    #

    def make_label(self, parent, text, size=11, color=TEXT, bold=False, **kwargs):
        return tk.Label(
            parent, text=text, bg=kwargs.pop("bg", parent.cget("bg")),
            fg=color, font=("Segoe UI", size, "bold" if bold else "normal"),
            **kwargs
        )

    #

    def make_button(self, parent, text, command, bg=ACCENT, fg="#081020", **kwargs):
        return tk.Button(
            parent, text=text, command=command, bg=bg, fg=fg,
            activebackground=ACCENT_HOVER, activeforeground="#081020",
            relief="flat", bd=0, cursor="hand2", padx=16, pady=10,
            font=("Segoe UI", 10, "bold"), **kwargs
        )

    #

    def show_setup(self):
        self.clear_window()
        outer = tk.Frame(self.root, bg=BG)
        outer.pack(fill="both", expand=True, padx=30, pady=25)
        self.make_label(outer, "ANIME CHARACTER DRAFT", 25, TEXT, True).pack(pady=(65, 8))
        self.make_label(
            outer, "Build your team. Manage your money. Decide who deserves each stat.",
            11, MUTED
        ).pack(pady=(0, 30))
        card = tk.Frame(outer, bg=PANEL, padx=32, pady=28)
        card.pack()
        self.make_label(card, "PLAYER NAMES", 12, ACCENT, True, bg=PANEL).pack(anchor="w", pady=(0, 18))
        self.make_label(card, "Player 1", 10, MUTED, True, bg=PANEL).pack(anchor="w")
        self.name1 = tk.Entry(card, width=34, font=("Segoe UI", 12), bg=PANEL_ALT, fg=TEXT,
                              insertbackground=TEXT, relief="flat", bd=0)
        self.name1.pack(ipady=10, pady=(6, 16))
        self.name1.insert(0, "Player 1")
        self.make_label(card, "Player 2", 10, MUTED, True, bg=PANEL).pack(anchor="w")
        self.name2 = tk.Entry(card, width=34, font=("Segoe UI", 12), bg=PANEL_ALT, fg=TEXT,
                              insertbackground=TEXT, relief="flat", bd=0)
        self.name2.pack(ipady=10, pady=(6, 22))
        self.name2.insert(0, "Player 2")
        self.make_button(card, "START DRAFT  →", self.start_game).pack(fill="x")
        self.make_label(
            outer,
            "Each player starts with £20 and fills Speed, Intelligence, Strength, Defence,\n"
            "Endurance, Ability and Willpower. Players alternate bids; passing offers the character to the other player for free.",
            10, MUTED, justify="center"
        ).pack(pady=24)
        self.name1.focus_set()

    #

    def start_game(self):
        name1 = self.name1.get().strip() or "Player 1"
        name2 = self.name2.get().strip() or "Player 2"
        if name1.casefold() == name2.casefold():
            if not messagebox.askyesno("Same names", "Both players have the same name. Continue?"):
                return
        self.players = [Player(name1), Player(name2)]
        self.current_player_index = 0
        self.current_character = None
        self.game_finished = False
        self.show_game()
        self.prepare_turn()

    #

    def show_game(self):
        self.clear_window()
        header = tk.Frame(self.root, bg=BG)
        header.pack(fill="x", padx=22, pady=(18, 10))
        self.make_label(header, "ANIME CHARACTER DRAFT", 18, TEXT, True, bg=BG).pack(side="left")
        self.pool_label = self.make_label(header, "", 10, MUTED, True, bg=BG)
        self.pool_label.pack(side="right", pady=6)
        body = tk.Frame(self.root, bg=BG)
        body.pack(fill="both", expand=True, padx=18, pady=(0, 18))
        body.grid_columnconfigure(0, weight=2, uniform="auction_columns")
        body.grid_columnconfigure(1, weight=5, uniform="auction_columns")
        body.grid_columnconfigure(2, weight=2, uniform="auction_columns")
        body.grid_rowconfigure(0, weight=1)
        self.player_panels = []
        for index, column in enumerate((0, 2)):
            player_panel = tk.Frame(body, bg=PANEL, padx=12, pady=14)
            player_panel.grid(row=0, column=column, sticky="nsew",
                              padx=(0, 8) if column == 0 else (8, 0))
            top = tk.Frame(player_panel, bg=PANEL)
            top.pack(fill="x")
            player_color = PLAYER_COLORS[index]
            name_label = self.make_label(top, "", 12, player_color, True, bg=PANEL)
            name_label.pack(anchor="w")
            money_label = self.make_label(player_panel, "", 11, player_color, True, bg=PANEL)
            money_label.pack(anchor="w", pady=(5, 0))
            progress_label = self.make_label(player_panel, "", 9, MUTED, bg=PANEL)
            progress_label.pack(anchor="w", pady=(3, 8))
            slot_labels = {}
            for slot in STAT_SLOTS:
                row = tk.Frame(player_panel, bg=PANEL_ALT, padx=7, pady=8)
                row.pack(fill="x", pady=3)
                self.make_label(row, slot, 8, MUTED, True, bg=PANEL_ALT).pack(anchor="w")
                value = self.make_label(row, "—", 9, TEXT, bg=PANEL_ALT,
                                        anchor="w", justify="left", wraplength=170)
                value.pack(fill="x", expand=True, pady=(3, 0))
                slot_labels[slot] = value
            self.player_panels.append({"frame": player_panel, "name": name_label,
                                       "color": player_color, "money": money_label,
                                       "progress": progress_label, "slots": slot_labels})
        center = tk.Frame(body, bg=PANEL, padx=20, pady=18)
        center.grid(row=0, column=1, sticky="nsew", padx=4)
        self.turn_label = self.make_label(center, "", 11, ACCENT, True, bg=PANEL)
        self.turn_label.pack(anchor="center")
        self.slot_label = self.make_label(center, "", 20, TEXT, True, bg=PANEL)
        self.slot_label.pack(anchor="center", pady=(8, 14))
        self.character_card = tk.Frame(center, bg=PANEL_ALT, padx=16, pady=18)
        self.character_card.pack(fill="both", expand=True)
        self.make_label(self.character_card, "CURRENT CHARACTER", 9, MUTED, True,
                        bg=PANEL_ALT).pack(pady=(8, 12))
        self.character_name_label = self.make_label(
            self.character_card, "Waiting for draft...", 23, TEXT, True,
            bg=PANEL_ALT, wraplength=440, justify="center"
        )
        self.character_name_label.pack(expand=True, fill="x", padx=10)
        self.anime_tag_label = self.make_label(self.character_card, "", 11, ACCENT,
                                               True, bg=PANEL_ALT)
        self.anime_tag_label.pack(pady=(12, 8))
        self.status_label = self.make_label(center, "", 10, MUTED, bg=PANEL,
                                            wraplength=470, justify="center")
        self.status_label.pack(fill="x", pady=(12, 6))
        actions = tk.Frame(center, bg=PANEL)
        actions.pack(fill="x", pady=(6, 0))
        bid_area = tk.Frame(actions, bg=PANEL)
        bid_area.pack(side="left", fill="x", expand=True)
        self.make_label(bid_area, "YOUR BID (£)", 9, MUTED, True, bg=PANEL).pack(anchor="w")
        self.bid_entry = tk.Entry(
            bid_area, width=10, font=("Segoe UI", 13, "bold"), bg=PANEL_ALT, fg=TEXT,
            insertbackground=TEXT, relief="flat", justify="center"
        )
        self.bid_entry.pack(anchor="w", ipady=8, pady=(5, 0))
        self.bid_entry.insert(0, "1")
        self.bid_entry.bind("<Return>", lambda _event: self.buy_character())
        self.pass_button = self.make_button(actions, "PASS", self.pass_character,
                                            bg="#2a3652", fg=TEXT)
        self.pass_button.pack(side="right", padx=(6, 0), pady=(16, 0))
        self.buy_button = self.make_button(actions, "PLACE BID", self.buy_character, bg=GREEN)
        self.buy_button.pack(side="right", padx=(6, 0), pady=(16, 0))
        footer = tk.Frame(self.root, bg=BG)
        footer.pack(fill="x", padx=22, pady=(0, 14))
        self.log_label = self.make_label(footer, "", 9, MUTED, bg=BG, anchor="w")
        self.log_label.pack(fill="x")

    #

    def update_builds(self):
        for index, player in enumerate(self.players):
            panel = self.player_panels[index]
            panel["name"].config(text=player.name, fg=panel["color"])
            panel["money"].config(text=f"£{player.balance}", fg=panel["color"])
            panel["progress"].config(text=f"{len(player.build)}/{len(STAT_SLOTS)} slots filled")
            for slot in STAT_SLOTS:
                entry = player.build.get(slot)
                if entry:
                    character = entry["character"]
                    text = f"{character['name']} [{character['anime']}]"
                    panel["slots"][slot].config(text=text, fg=panel["color"])
                else:
                    panel["slots"][slot].config(text="—", fg=MUTED)
        self.pool_label.config(text=f"{len(self.character_pool)} CHARACTERS LEFT")

    #

    def prepare_turn(self):
        """Reveal one character and begin an alternating two-player auction."""
        if all(not player.has_empty_slots() for player in self.players):
            self.finish_game()
            return
        attempts = 0
        while not self.players[self.current_player_index].has_empty_slots() and attempts < 2:
            self.current_player_index = (self.current_player_index + 1) % 2
            attempts += 1
        if not self.character_pool:
            self.finish_game(pool_exhausted=True)
            return
        self.current_character = self.character_pool.pop()
        self.high_bid = 0
        self.high_bidder_index = None
        self.current_slot = self.players[self.current_player_index].next_slot()
        self.update_builds()
        self.show_current_auction()

    #

    def show_current_auction(self):
        player = self.players[self.current_player_index]
        self.current_slot = player.next_slot()
        player_color = PLAYER_COLORS[self.current_player_index]
        self.turn_label.config(
            text=f"{player.name.upper()}'S BID  •  £{player.balance} AVAILABLE",
            fg=player_color
        )
        self.slot_label.config(text=f"Choose for: {self.current_slot}")
        self.character_name_label.config(text=self.current_character["name"])
        self.anime_tag_label.config(text=f"FROM {self.current_character['anime']}")
        if self.high_bidder_index is None:
            bid_text = "No bids yet. Enter at least £1 to start the auction."
        else:
            leader = self.players[self.high_bidder_index]
            bid_text = f"Highest bid: £{self.high_bid} by {leader.name}. Enter a higher bid or pass."
        minimum = self.high_bid + 1
        can_bid = player.has_empty_slots() and player.balance >= minimum
        if not player.has_empty_slots():
            bid_text = f"{player.name} has filled all stat slots and cannot bid. Pass to continue."
        elif not can_bid:
            if self.high_bidder_index is None:
                bid_text = f"{player.name} has £{player.balance}. No bid required to receive a character for free; pass to continue."
            else:
                bid_text = f"You have £{player.balance} and cannot beat £{self.high_bid}. Pass to close the auction."
        status_color = (PLAYER_COLORS[self.high_bidder_index] if self.high_bidder_index is not None
                        else PLAYER_COLORS[self.current_player_index])
        self.status_label.config(text=bid_text, fg=status_color)
        self.buy_button.config(text="PLACE BID", state="normal" if can_bid else "disabled")
        self.pass_button.config(state="normal")
        self.bid_entry.config(state="normal" if can_bid else "disabled")
        self.bid_entry.delete(0, "end")
        self.bid_entry.insert(0, str(minimum) if can_bid else "0")
        if can_bid:
            self.bid_entry.focus_set()
        self.update_builds()

    #

    def buy_character(self):
        """Place a bid, then give the other player the next bidding turn."""
        if self.game_finished or self.current_character is None:
            return
        player = self.players[self.current_player_index]
        try:
            bid = int(self.bid_entry.get().strip())
        except ValueError:
            messagebox.showerror("Invalid bid", "Enter a whole number for your bid.")
            return
        minimum = self.high_bid + 1
        if bid < minimum:
            messagebox.showerror("Invalid bid", f"Your bid must be at least £{minimum}.")
            return
        if bid > player.balance:
            messagebox.showerror("Not enough money", f"You only have £{player.balance} available.")
            return
        self.high_bid = bid
        self.high_bidder_index = self.current_player_index
        self.log_label.config(
            text=f"{player.name} bids £{bid} for {self.current_character['name']} "
                 f"[{self.current_character['anime']}].",
            fg=PLAYER_COLORS[self.current_player_index]
        )
        self.current_player_index = (self.current_player_index + 1) % 2
        other = self.players[self.current_player_index]
        if not other.has_empty_slots():
            self.award_character(self.high_bidder_index, self.high_bid)
            return
        if other.balance <= self.high_bid:
            self.award_character(self.high_bidder_index, self.high_bid)
            return
        self.show_current_auction()

    #

    def pass_character(self):
        """Offer a passed character to the other player for free.

        If they decline, discard this character and let the passer start
        the next character's auction.
        """
        if self.game_finished or self.current_character is None:
            return
        passer_index = self.current_player_index
        passer = self.players[passer_index]
        other_index = (passer_index + 1) % 2
        other = self.players[other_index]
        character = self.current_character
        if other.has_empty_slots():
            wants_character = messagebox.askyesno(
                "Free character offer",
                f"{passer.name} passed on {character['name']} "
                f"[{character['anime']}].\\n\\n"
                f"{other.name}, would you like to take this character for FREE?"
            )
        else:
            wants_character = False
            self.log_label.config(
                text=f"{other.name} has no empty stat slots, so cannot take "
                     f"{character['name']} for free."
            )
        if wants_character:
            self.log_label.config(
                text=f"{other.name} accepted {character['name']} "
                     f"[{character['anime']}] for free."
            )
            self.award_character(other_index, 0)
            return
        self.log_label.config(
            text=f"{other.name} declined {character['name']} "
                 f"[{character['anime']}]. Moving to the next character."
        )
        self.current_player_index = passer_index
        self.prepare_turn()

    #

    def award_character(self, winner_index, cost):
        winner = self.players[winner_index]
        character = self.current_character
        slot = winner.next_slot()
        if slot is None:
            self.current_player_index = (winner_index + 1) % 2
            self.prepare_turn()
            return
        winner.add_character(slot, character, cost)
        self.log_label.config(
            text=f"{winner.name} drafted {character['name']} [{character['anime']}] "
                 f"for {slot} at £{cost}."
        )
        self.current_player_index = (winner_index + 1) % 2
        self.prepare_turn()

    #

    def finish_game(self, pool_exhausted=False):
        self.game_finished = True
        self.clear_window()
        outer = tk.Frame(self.root, bg=BG, padx=24, pady=22)
        outer.pack(fill="both", expand=True)
        title = "DRAFT COMPLETE" if not pool_exhausted else "CHARACTER POOL EMPTY"
        self.make_label(outer, title, 23, TEXT, True, bg=BG).pack(pady=(8, 4))
        subtitle = "Compare both builds and decide who wins." if not pool_exhausted else "The pool ran out before both builds were complete."
        self.make_label(outer, subtitle, 10, MUTED, bg=BG).pack(pady=(0, 18))
        columns = tk.Frame(outer, bg=BG)
        columns.pack(fill="both", expand=True)
        columns.grid_columnconfigure(0, weight=1, uniform="final")
        columns.grid_columnconfigure(1, weight=1, uniform="final")
        for i, player in enumerate(self.players):
            panel = tk.Frame(columns, bg=PANEL, padx=18, pady=18)
            panel.grid(row=0, column=i, sticky="nsew", padx=(0, 8) if i == 0 else (8, 0))
            self.make_label(panel, player.name, 16, ACCENT, True, bg=PANEL).pack(anchor="w")
            self.make_label(panel, f"Money remaining: £{player.balance}", 10, GREEN, True, bg=PANEL).pack(anchor="w", pady=(3, 12))
            for slot in STAT_SLOTS:
                entry = player.build.get(slot)
                if entry:
                    character = entry["character"]
                    text = f"{character['name']} [{character['anime']}]\nPaid: £{entry['cost']}"
                    color = TEXT
                else:
                    text = "Not filled"
                    color = MUTED
                row = tk.Frame(panel, bg=PANEL_ALT, padx=10, pady=8)
                row.pack(fill="x", pady=3)
                self.make_label(row, slot.upper(), 8, MUTED, True, bg=PANEL_ALT, width=14, anchor="w").pack(side="left")
                self.make_label(row, text, 9, color, bg=PANEL_ALT, justify="left", wraplength=300, anchor="w").pack(side="left", fill="x", expand=True)
        bottom = tk.Frame(outer, bg=BG)
        bottom.pack(fill="x", pady=(18, 0))
        self.make_button(bottom, "NEW GAME", self.show_setup).pack(side="left")
        self.make_button(bottom, "CLOSE", self.root.destroy, bg="#2a3652", fg=TEXT).pack(side="right")

#

def main():
    root = tk.Tk()
    AnimeDraftGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()
    import random

#============

AOT = [

    'Eren Yeager',
    'Mikasa Ackerman',
    'Armin Arlert',
    'Levi Ackerman',
    'Erwin Smith',
    'Hange Zoë',
    'Sasha Braus',
    'Jean Kirstein',
    'Connie Springer',
    'Historia Reiss',
    'Ymir',
    'Reiner Braun',
    'Bertolt Hoover',
    'Annie Leonhart',
    'Zeke Yeager',
    'Grisha Jaeger',
    'Carla Jaeger',
    'Kenny Akerman',
    'Hannes',
    'Dot Pixis',
    'Keith Shadis',
    'Marco Bott',
    'Floch Forster',
    'Pieck Finger',
    'Porco Galliard',
    'Colt Grice',
    'Gabi Braun',
    'Falco Grice',
    'Theo Magath',
    'Tom Ksaver',
    'Lara Tybur',
    'Ymir Fritz',
    'Flegel Reeves',
    'Kiyomi Azumabito',
    'Niccolo',
    'Yelena',
    'Onyankopon',

]

#============

JJK = [

    'Kento Nanami',
    'Mei Mei',
    'Ui Ui',
    'Toji Fushiguro',
    'Yuki Tsukumo',
    'Ryu Ishigori',
    'Hajime Kashimo',
    'Hiromi Higuruma',
    'Takuma Ino',
    'Naobito Zenin',
    'Naoya Zenin',
    'Ogi Zenin',
    'Jinichi Zenin',
    'Ranta Zenin',
    'Master Tengen',
    'Ryomen Sukuna',
    'Kenjaku',
    'Suguru Geto',
    'Uraume',
    'Haruta Shigemo',
    'Jiro Awasaka',
    'Juzo Kumiya',
    'Ogami',
    'Shiu Kong',
    'Larue',
    'Mimiko Hasaba',
    'Nanako Hasaba',
    'Junpei Yoshino',
    'Mahito',
    'Jogo',
    'Hanami',
    'Dagon',
    'Choso',
    'Eso',
    'Kechizu',
    'Kurourushi',
    'Rika Orimoto',

]

#============

MHA = [

    'Izuku Midoriya (Deku)',
    'Katsuki Bakugo (Great Explosion Murder God Dynamight)',
    'Ochaco Uraraka (Uravity)',
    'Shoto Todoroki (Shoto)',
    'Tenya Ida (Ingenium)',
    'All Might (Toshinori Yagi)',
    'Tomura Shigaraki (Tenko Shimura)',
    'All For One',
    'Eijiro Kirishima (Red Riot)',
    'Tsuyu Asui (Froppy)',
    'Momo Yaoyorozu (Creati)',
    'Fumikage Tokoyami (Tsukuyomi)',
    'Kyoka Jiro (Earphone Jack)',
    'Mina Ashido (Pinky)',
    'Denki Kaminari (Chargebolt)',
    'Mezo Shoji (Tentacole)',
    'Hanto Sero (Cellophane)',
    'Mashirao Ojiro (Tailman)',
    'Minoru Mineta (Grape Juice)',
    'Toru Hagakure (Invisible Girl)',
    'Koji Koda (Anima)',
    'Rikido Sato (Sugarman)',
    'Yuga Aoyama (Cant Stop Twinkling)',
    'Mirio Togata (Lemillion - The Big 3)',
    'Mei Hatsume (Support Course)',
    'Itsuka Kendo (Battle Fist)',
    'Neito Monoma (Phantom Thief)',
    'Endeavor (Enji Todoroki)',
    'Hawks (Keigo Takami)',
    'Eraser Head (Shota Aizawa)',
    'Best Jeanist (Tsunagu Hakamada)',
    'Gran Torino (Sorahiko Torino)',
    'Mirko (Rumi Usagiyama)',
    'Present Mic (Hizashi Yamada)',
    'Midnight (Nemuri Kayama)',
    'Nezu (Principal Nezu)',
    'Recovery Girl (Chiyo Shuzenji)',
    'Kamui Woods (Shinji Nishiya)',
    'Mt. Lady (Yu Takeyama)',
    'Fat Gum (Taishiro Toyomitsu)',
    'Sir Nighteye (Mirai Sasaki)',
    'Gang Orca (Kugo Sakamata)',
    'Dabi (Toya Todoroki)',
    'Himiko Toga',
    'Twice (Jin Bubaigawara)',
    'Kurogiri (Oboro Shirakumo)',
    'Overhaul (Kai Chisaki)',
    'Stain (Chizome Akaguro)',
    'Lady Nagant (Kaina Tsutsumi)',
    'Gentle Criminal (Danjuro Tobita)',
    'Muscular (Goto Imasuji)',
    'Eri',

]

#============

OPM = [

    'Saitama',
    'Genos',
    'Tatsumaki',
    'Fubuki',
    'Bang',
    'Garou',
    'King',
    "Speed-o'-Sound Sonic",
    'Atomic Samurai',
    'Metal Bat',
    'Child Emperor',
    'Zombieman',
    'Flashy Flash',
    'Mumen Rider',
    'Blast',
    'Bofoi',
    'Metal Knight',
    'Drive Knight',
    'Pig God',
    'Watchdog Man',
    'Superalloy Darkshine',
    'Tanktop Master',
    'Puri-Puri Prisoner',
    'Sweet Mask',
    'Amai Mask',
    'Boros',
    'Orochi',
    'Psykos',
    'Monster God',
    'Empty Void',
    'Suiryu',
    'Charanko',
    'Bomb',
    'Dr. Kuseno',
    'Dr. Genus',
    'Armored Gorilla',
    'Carnage Kabuto',
    'Vaccine Man',
    'Deep Sea King',
    'Melzargard',
    'Geryuganshoop',
    'Groribas',
    'Crablante',
    'Stinger',
    'Lightning Max',
    'Sneck',
    'Iaian',
    'Spring Mustachio',
    'Golden Ball',
    'Death Gatling',
    'Smile Man',
    'Blue Fire',
    'Heavy Tank Fundoshi',
    'Tanktop Tiger',
    'Tanktop Black Hole',
    'Gouketsu',
    'Elder Centipede',
    'Black Sperm',
    'Homeless Emperor',
    'Fuhrer Ugly',
    'Gums',
    'Nyan',
    'Phoenix Man',
    'Overgrown Rover',
    'Evil Natural Water',
    'G4',
    'G5',
    'Awakened Cockroach',
    'Bakuzan',
    'Choze',
    'Marshall Gorilla',
    'Rhino Wrestler',
    'Royal Ripper',
    'Bug God',
    'Pure Blood',
    'Freezer Man',
    'Slacker Sid',
    'Subterranean King',
    'Sky King',
    'Ancient King',
    'Deep Sea King',
    'Pluton',
    'Marugori',
    'Beefcake',
    'Fukegao',
    'Hammerhead',
    'Sonic',
    'Tareo',
    'Zenko',

]

#============

SL = [

    'Sung Jin-Woo (The Shadow Monarch)',
    "Sung Il-Hwan (Jin-Woo's Father / Vessel of the Rulers)",
    'Cha Hae-In (The Radiant Sword / S-Rank Hunter)',
    "Yoo Jin-Ho (Jin-Woo's Loyal Vice-Guild Master)",
    'Go Gun-Hee (The Association President / Sky Above the Sky)',
    'Thomas Andre (The Goliath / National Level Hunter)',
    'Liu Zhigang (The Hero of China / National Level Hunter)',
    'Christopher Reed (National Level Hunter / Vessel of the Rulers)',
    'Siddharth Bachchan (National Level Hunter)',
    'Jonas (National Level Hunter of Brazil)',
    'Choi Jong-In (The Ultimate Soldier / Master of Hunters Guild)',
    'Baek Yoon-Ho (The White Tiger / Guild Master)',
    'Min Byung-Gu (The Retired S-Rank Healer)',
    'Lim Tae-Gyu (Master of Fiend Guild)',
    'Ma Dong-Wook (Master of Fame Guild)',
    'Yoo Myung-Han (Chairman of Yoojin Construction)',
    "Park Heeo-Jin (B-Rank Mage / Jin-Woo's Early Party Member)",
    "Lee Ju-Hee (B-Rank Healer / Jin-Woo's Friend from the Double Dungeon)",
    'Song Chi-Yeul (C-Rank Mage / The Veteran Sword Elder)',
    'Kim Chul (Iron / High Orc Shadow / A-Rank Tanker)',
    'Hwang Dong-Su (Greed / S-Rank Traitor / Scavenger Guild)',
    "Hwang Dong-Suk (C-Rank Villain / Dong-Su's Brother)",
    'Woo Jin-Chul (The Surveillance Chief / Later Association President)',
    'Han Jae-Gu (A-Rank Hunter of White Tiger Guild)',
    'Kim Gu-Bhim (A-Rank Hunter of White Tiger Guild)',
    'Park Jong-Soo (Master of Knights Guild)',
    'Jeong Yun-Ki (Vice-Master of Knights Guild)',
    "Goto Ryuji (Japan's Strongest S-Rank Hunter)",
    'Reiji Sugimoto (Japanese S-Rank Hunter)',
    'Akari Shimizu (Japanese S-Rank Healer)',
    'Kenzo Tanaka (Japanese S-Rank Brawler)',
    'Kanae Tawata (Japanese S-Rank Assassin)',
    'Minoru Hoshino (Japanese S-Rank Hunter)',
    'Kei (Japanese S-Rank Ice Mage)',
    'Mari Ishida (Japanese S-Rank Hunter)',
    'Kumamoto (Japanese S-Rank Berserker)',
    'Yuri Orloff (The Russian S-Rank Barrier King)',
    "Lennart Niermann (Germany's Top S-Rank Hunter)",
    "Laura (Thomas Andre's Personal Manager)",
    'Selner (The Prophet / Madam Selner)',
    'David Brennon (Director of the Federal Bureau of Hunters)',
    'Gina (American S-Rank Hunter)',
    'Norris (American S-Rank Hunter)',
    'Brent (American S-Rank Hunter)',
    "Jong-Soo's Secretary (Knights Guild Staff)",
    "Sung Jin-Ah (Jin-Woo's Younger Sister)",
    "Park Kyung-Hye (Jin-Woo's Mother)",
    "Yoo Jin-Hee (Jin-Ho's Older Sister)",
    "Han Song-Yi (E-Rank Hunter / Jin-Ah's Friend)",
    "The Architect (The Creator of the System / Ashborn's Servant)",
    'Ashborn (The Original Shadow Monarch)',
    'Antares (The Monarch of Destruction / King of Dragons)',
    'Rakan (The Monarch of Fangs / King of Beasts)',
    'Baruka (The Monarch of White Flames / King of Snow Folk)',
    'Querehsha (The Monarch of Plagues / Queen of Insects)',
    'Yogumunt (The Monarch of Transmutation / King of Demonic Spectres)',
    'Tarnak (The Monarch of Iron Body / King of Monstrous Humanoids)',
    'Sillad (The Monarch of Frost / King of Snow Folk)',
    'Legia (The Monarch of the Beginning / King of Giants)',
    'Absolute Being (The Creator Creator of Monarchs and Rulers)',
    "Igris (The Blood Red Commander / Jin-Woo's Shadow)",
    "Beru (The Shadow Ant King / Jin-Woo's Shadow)",
    "Tusk (The High Orc Shaman Shadow / Jin-Woo's Shadow)",
    "Tank (The Ice Bear Shadow / Jin-Woo's Shadow)",
    "Kaisel (The Shadow Wyvern / Jin-Woo's Mount)",
    "Jima (The Naga Shadow / Jin-Woo's Shadow)",
    "Bellion (The Grand Marshal / Ashborn's Original Shadow)",
    "Kamish (The Shadow Dragon / Humanity's Greatest Calamity)",

]

#============

DL = [

    'Tanjirō Kamado',
    'Nezuko Kamado',
    'Zenitsu Agatsuma',
    'Inosuke Hashibira',
    'Kanao Tsuyuri',
    'Genya Shinazugawa',
    'Giyū Tomioka (Water Hashira)',
    'Shinobu Kochō (Insect Hashira)',
    'Kyōjurō Rengoku (Flame Hashira)',
    'Tengen Uzui (Sound Hashira)',
    'Mitsuri Kanroji (Love Hashira)',
    'Muichirō Tokitō (Mist Hashira)',
    'Gyōmei Himejima (Stone Hashira)',
    'Obanai Iguro (Serpent Hashira)',
    'Sanemi Shinazugawa (Wind Hashira)',
    'Muzan Kibutsuji (Demon King)',
    'Kokushibō (Upper Moon One)',
    'Dōma (Upper Moon Two)',
    'Akaza (Upper Moon Three)',
    'Hantengu (Upper Moon Four)',
    'Gyokko (Upper Moon Five)',
    'Gyūtarō (Upper Moon Six)',
    'Daki (Upper Moon Six)',
    'Kaigaku (Upper Moon Six)',
    'Nakime (Upper Moon Four)',
    'Enmu (Lower Moon One)',
    'Rui (Lower Moon Five)',
    'Kyōgai (Former Lower Moon Six)',
    'Sakonji Urokodaki (Former Water Hashira)',
    'Jigorō Kuwajima (Former Roaring Hashira)',
    'Shinjurō Rengoku (Former Flame Hashira)',
    'Kanae Kochō (Former Flower Hashira)',
    'Yoriichi Tsugikuni (Creator of Sun Breathing)',
    'Tamayo (Demon Doctor)',
    "Yushirō (Tamayo's Assistant)",
    'Murata (Demon Slayer Corps Member)',
    'Aoi Kanzaki (Butterfly Mansion Helper)',
    'Sumi Nakahara (Butterfly Mansion Helper)',
    'Kiyo Terauchi (Butterfly Mansion Helper)',
    'Naho Takada (Butterfly Mansion Helper)',
    'Sabo (Demon Slayer Cadet)',
    'Makomo (Demon Slayer Cadet)',
    'Hotaru Haganezuka (Swordsmith)',
    'Kozo Kanamori (Swordsmith)',
    'Kotetsu (Swordsmith Village Resident)',
    'Tecchin Tecchikawahara (Swordsmith Village Chief)',
    "Hinatsuru (Tengen's Wife)",
    "Makuo (Tengen's Wife)",
    "Suma (Tengen's Wife)",
    'Kagaya Ubuyashiki (Master of the Mansion)',
    "Amane Ubuyashiki (Kagaya's Wife)",
    "Kiriya Ubuyashiki (Kagaya's Son)",
    "Kanata Ubuyashiki (Kagaya's Daughter)",
    "Kuina Ubuyashiki (Kagaya's Daughter)",
    "Nichika Ubuyashiki (Kagaya's Daughter)",
    "Hinaki Ubuyashiki (Kagaya's Daughter)",
    'Susamaru (Temari Demon)',
    'Yahaba (Arrow Demon)',
    'Spider Demon Mother (Spider Family)',
    'Spider Demon Father (Spider Family)',
    'Spider Demon Brother (Spider Family)',
    'Spider Demon Sister (Spider Family)',
    'Hand Demon (Final Selection Demon)',
    "Kie Kamado (Tanjirō's Mother)",
    "Takeo Kamado (Tanjirō's Brother)",
    "Hanako Kamado (Tanjirō's Sister)",
    "Shigeru Kamado (Tanjirō's Brother)",
    "Rokuta Kamado (Tanjirō's Brother)",
    "Tanjūrō Kamado (Tanjirō's Father)",
    "Senjūrō Rengoku (Kyōjurō's Brother)",
    "Ruka Rengoku (Kyōjurō's Mother)",
    "Kotoha Hashibira (Inosuke's Mother)",
    "Yuichirō Tokitō (Muichirō's Twin Brother)",
    "Tsutako Tomioka (Giyū's Sister)",

]

#============

BL = [

    'Yoichi Isagi',
    'Meguru Bachira',
    'Rensuke Kunigami',
    'Hyoma Chigiri',
    'Rin Itoshi',
    'Sae Itoshi',
    'Seishiro Nagi',
    'Reo Mikage',
    'Zantetsu Tsurugi',
    'Shouei Barou',
    'Gin Gagamaru',
    'Jingo Raichi',
    'Gurimu Igarashi',
    'Asahi Naruhaya',
    'Wataru Kuon',
    'Okuhito Iemon',
    'Yudai Imamura',
    'Ryosuke Kira',
    'Jin Kiyora',
    'Ikki Niko',
    'Junichi Wanima',
    'Keisuke Wanima',
    'Ryusei Shidou',
    'Tabito Karasu',
    'Eita Otoya',
    'Kenyu Yukimiya',
    'Yo Hiyori',
    'Nijiro Nanase',
    'Kurona Ranze',
    'Aoshi Tokimitsu',
    'Jubei Aryu',
    'Anri Teieri',
    'Jinpachi Ego',
    'Yasuhito Fukaku',
    'Oliver Aiku',
    'Shuto Sendo',
    'Kazuma Niou',
    'Teppei Neru',
    'Kento Cho',
    'Teru Kitsunezato',
    'Itsuki Wakatsuki',
    'Haru Hayate',
    'Taiga Tsunzaki',
    'Miroku Darai',
    'Shingen Tanaka',
    'Noel Noa',
    'Chris Prince',
    'Lavinho',
    'Marc Snuffy',
    'Julian Loki',
    'Michael Kaiser',
    'Alexis Ness',
    'Benedict Grim',
    'Erik Gesner',
    'Mensah',
    'Birkenstock',
    'Agi',
    'Don Lorenzo',
    'Drago',
    'Charles Chevalier',
    'Leonardo Luna',
    'Pablo Cavasoz',
    'Adam Blake',
    'Dada Silva',

]

#============

ANIME_LISTS = {

    "AOT": AOT,
    "JJK": JJK,
    "MHA": MHA,
    "OPM": OPM,
    "SL": SL,
    "DL": DL,
    "BL": BL,

}

#============

def register_anime(short_name, characters):

    """Register an anime character list so it is included in every new shuffled pool.

    Example:

        register_anime("OP", OP)

    """
    key = short_name.strip().upper()
    if not key:
        raise ValueError("Anime name cannot be empty.")
    if key in ANIME_LISTS:
        raise ValueError(f"Anime list '{key}' is already registered.")
    if isinstance(characters, str):
        raise TypeError("characters must be a list of character names, not one string.")
    cleaned = [name.strip() for name in characters if isinstance(name, str) and name.strip()]
    if not cleaned:
        raise ValueError("Add at least one character name to the list.")
    ANIME_LISTS[key] = cleaned

#

STAT_SLOTS = [

    "Speed",
    "Intelligence",
    "Strength",
    "Defence",
    "Endurance",
    "Ability",
    "Willpower",
]

#

STARTING_BALANCE = 20

#

def make_character_pool():
    """Build and shuffle characters from every list registered in ANIME_LISTS."""
    pool = []
    for anime_name, characters in ANIME_LISTS.items():
        for character_name in characters:
            pool.append({
                "name": character_name,
                "anime": anime_name,
                "display": f"{character_name} [{anime_name}]",
            })
    random.shuffle(pool)
    return pool

import tkinter as tk
from tkinter import messagebox

#

#*GUI THEME*

BG = "#0b1020"
PANEL = "#141c31"
PANEL_ALT = "#1a2540"
ACCENT = "#7c9cff"
ACCENT_HOVER = "#9db4ff"
TEXT = "#edf2ff"
MUTED = "#a4b0cc"
GREEN = "#75e0b2"
RED = "#ff8795"
GOLD = "#ffd479"
PLAYER_COLORS = ("#ff5c6c", "#5ca8ff")

#
class Player:

    def __init__(self, name, balance=STARTING_BALANCE):

        self.name = name
        self.balance = balance
        self.build = {}
        self.consecutive_passes = 0
        self.force_next_pick = False

    #

    def has_empty_slots(self):
        return len(self.build) < len(STAT_SLOTS)

    #

    def next_slot(self):
        for slot in STAT_SLOTS:
            if slot not in self.build:
                return slot
        return None

    #

    def add_character(self, slot, character, cost=0):
        if slot in self.build:
            raise ValueError(f"{self.name} already has a character for {slot}.")
        if cost > self.balance:
            raise ValueError("The player cannot afford that amount.")
        self.balance -= cost
        self.build[slot] = {"character": character, "cost": cost}
        self.consecutive_passes = 0
        self.force_next_pick = False

#
def make_character_pool():
    pool = []
    for anime_name, characters in ANIME_LISTS.items():
        for character_name in characters:
            pool.append({
                "name": character_name,
                "anime": anime_name,
                "display": f"{character_name} [{anime_name}]",
            })
    random.shuffle(pool)
    return pool

#

class AnimeDraftGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Anime Character Draft")
        self.root.geometry("1180x790")
        self.root.minsize(980, 680)
        self.root.configure(bg=BG)
        self.players = []
        self.character_pool = make_character_pool()
        self.current_player_index = 0
        self.current_character = None
        self.current_slot = None
        self.high_bid = 0
        self.high_bidder_index = None
        self.game_finished = False
        self.show_setup()

    #

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    #

    def make_label(self, parent, text, size=11, color=TEXT, bold=False, **kwargs):
        return tk.Label(
            parent, text=text, bg=kwargs.pop("bg", parent.cget("bg")),
            fg=color, font=("Segoe UI", size, "bold" if bold else "normal"),
            **kwargs
        )

    #

    def make_button(self, parent, text, command, bg=ACCENT, fg="#081020", **kwargs):
        return tk.Button(
            parent, text=text, command=command, bg=bg, fg=fg,
            activebackground=ACCENT_HOVER, activeforeground="#081020",
            relief="flat", bd=0, cursor="hand2", padx=16, pady=10,
            font=("Segoe UI", 10, "bold"), **kwargs
        )

    #

    def show_setup(self):
        self.clear_window()
        outer = tk.Frame(self.root, bg=BG)
        outer.pack(fill="both", expand=True, padx=30, pady=25)
        self.make_label(outer, "ANIME CHARACTER DRAFT", 25, TEXT, True).pack(pady=(65, 8))
        self.make_label(
            outer, "Build your team. Manage your money. Decide who deserves each stat.",
            11, MUTED
        ).pack(pady=(0, 30))
        card = tk.Frame(outer, bg=PANEL, padx=32, pady=28)
        card.pack()
        self.make_label(card, "PLAYER NAMES", 12, ACCENT, True, bg=PANEL).pack(anchor="w", pady=(0, 18))
        self.make_label(card, "Player 1", 10, MUTED, True, bg=PANEL).pack(anchor="w")
        self.name1 = tk.Entry(card, width=34, font=("Segoe UI", 12), bg=PANEL_ALT, fg=TEXT,
                              insertbackground=TEXT, relief="flat", bd=0)
        self.name1.pack(ipady=10, pady=(6, 16))
        self.name1.insert(0, "Player 1")
        self.make_label(card, "Player 2", 10, MUTED, True, bg=PANEL).pack(anchor="w")
        self.name2 = tk.Entry(card, width=34, font=("Segoe UI", 12), bg=PANEL_ALT, fg=TEXT,
                              insertbackground=TEXT, relief="flat", bd=0)
        self.name2.pack(ipady=10, pady=(6, 22))
        self.name2.insert(0, "Player 2")
        self.make_button(card, "START DRAFT  →", self.start_game).pack(fill="x")
        self.make_label(
            outer,
            "Each player starts with £20 and fills Speed, Intelligence, Strength, Defence,\n"
            "Endurance, Ability and Willpower. Players alternate bids; passing offers the character to the other player for free.",
            10, MUTED, justify="center"
        ).pack(pady=24)
        self.name1.focus_set()

    #

    def start_game(self):
        name1 = self.name1.get().strip() or "Player 1"
        name2 = self.name2.get().strip() or "Player 2"
        if name1.casefold() == name2.casefold():
            if not messagebox.askyesno("Same names", "Both players have the same name. Continue?"):
                return
        self.players = [Player(name1), Player(name2)]
        self.current_player_index = 0
        self.current_character = None
        self.game_finished = False
        self.show_game()
        self.prepare_turn()

    #

    def show_game(self):
        self.clear_window()
        header = tk.Frame(self.root, bg=BG)
        header.pack(fill="x", padx=22, pady=(18, 10))
        self.make_label(header, "ANIME CHARACTER DRAFT", 18, TEXT, True, bg=BG).pack(side="left")
        self.pool_label = self.make_label(header, "", 10, MUTED, True, bg=BG)
        self.pool_label.pack(side="right", pady=6)
        body = tk.Frame(self.root, bg=BG)
        body.pack(fill="both", expand=True, padx=18, pady=(0, 18))
        body.grid_columnconfigure(0, weight=2, uniform="auction_columns")
        body.grid_columnconfigure(1, weight=5, uniform="auction_columns")
        body.grid_columnconfigure(2, weight=2, uniform="auction_columns")
        body.grid_rowconfigure(0, weight=1)
        self.player_panels = []
        for index, column in enumerate((0, 2)):
            player_panel = tk.Frame(body, bg=PANEL, padx=12, pady=14)
            player_panel.grid(row=0, column=column, sticky="nsew",
                              padx=(0, 8) if column == 0 else (8, 0))
            top = tk.Frame(player_panel, bg=PANEL)
            top.pack(fill="x")
            player_color = PLAYER_COLORS[index]
            name_label = self.make_label(top, "", 12, player_color, True, bg=PANEL)
            name_label.pack(anchor="w")
            money_label = self.make_label(player_panel, "", 11, player_color, True, bg=PANEL)
            money_label.pack(anchor="w", pady=(5, 0))
            progress_label = self.make_label(player_panel, "", 9, MUTED, bg=PANEL)
            progress_label.pack(anchor="w", pady=(3, 8))
            slot_labels = {}
            for slot in STAT_SLOTS:
                row = tk.Frame(player_panel, bg=PANEL_ALT, padx=7, pady=8)
                row.pack(fill="x", pady=3)
                self.make_label(row, slot, 8, MUTED, True, bg=PANEL_ALT).pack(anchor="w")
                value = self.make_label(row, "—", 9, TEXT, bg=PANEL_ALT,
                                        anchor="w", justify="left", wraplength=170)
                value.pack(fill="x", expand=True, pady=(3, 0))
                slot_labels[slot] = value
            self.player_panels.append({"frame": player_panel, "name": name_label,
                                       "color": player_color, "money": money_label,
                                       "progress": progress_label, "slots": slot_labels})
        center = tk.Frame(body, bg=PANEL, padx=20, pady=18)
        center.grid(row=0, column=1, sticky="nsew", padx=4)
        self.turn_label = self.make_label(center, "", 11, ACCENT, True, bg=PANEL)
        self.turn_label.pack(anchor="center")
        self.slot_label = self.make_label(center, "", 20, TEXT, True, bg=PANEL)
        self.slot_label.pack(anchor="center", pady=(8, 14))
        self.character_card = tk.Frame(center, bg=PANEL_ALT, padx=16, pady=18)
        self.character_card.pack(fill="both", expand=True)
        self.make_label(self.character_card, "CURRENT CHARACTER", 9, MUTED, True,
                        bg=PANEL_ALT).pack(pady=(8, 12))
        self.character_name_label = self.make_label(
            self.character_card, "Waiting for draft...", 23, TEXT, True,
            bg=PANEL_ALT, wraplength=440, justify="center"
        )
        self.character_name_label.pack(expand=True, fill="x", padx=10)
        self.anime_tag_label = self.make_label(self.character_card, "", 11, ACCENT,
                                               True, bg=PANEL_ALT)
        self.anime_tag_label.pack(pady=(12, 8))
        self.status_label = self.make_label(center, "", 10, MUTED, bg=PANEL,
                                            wraplength=470, justify="center")
        self.status_label.pack(fill="x", pady=(12, 6))
        actions = tk.Frame(center, bg=PANEL)
        actions.pack(fill="x", pady=(6, 0))
        bid_area = tk.Frame(actions, bg=PANEL)
        bid_area.pack(side="left", fill="x", expand=True)
        self.make_label(bid_area, "YOUR BID (£)", 9, MUTED, True, bg=PANEL).pack(anchor="w")
        self.bid_entry = tk.Entry(
            bid_area, width=10, font=("Segoe UI", 13, "bold"), bg=PANEL_ALT, fg=TEXT,
            insertbackground=TEXT, relief="flat", justify="center"
        )
        self.bid_entry.pack(anchor="w", ipady=8, pady=(5, 0))
        self.bid_entry.insert(0, "1")
        self.bid_entry.bind("<Return>", lambda _event: self.buy_character())
        self.pass_button = self.make_button(actions, "PASS", self.pass_character,
                                            bg="#2a3652", fg=TEXT)
        self.pass_button.pack(side="right", padx=(6, 0), pady=(16, 0))
        self.buy_button = self.make_button(actions, "PLACE BID", self.buy_character, bg=GREEN)
        self.buy_button.pack(side="right", padx=(6, 0), pady=(16, 0))
        footer = tk.Frame(self.root, bg=BG)
        footer.pack(fill="x", padx=22, pady=(0, 14))
        self.log_label = self.make_label(footer, "", 9, MUTED, bg=BG, anchor="w")
        self.log_label.pack(fill="x")

    #

    def update_builds(self):
        for index, player in enumerate(self.players):
            panel = self.player_panels[index]
            panel["name"].config(text=player.name, fg=panel["color"])
            panel["money"].config(text=f"£{player.balance}", fg=panel["color"])
            panel["progress"].config(text=f"{len(player.build)}/{len(STAT_SLOTS)} slots filled")
            for slot in STAT_SLOTS:
                entry = player.build.get(slot)
                if entry:
                    character = entry["character"]
                    text = f"{character['name']} [{character['anime']}]"
                    panel["slots"][slot].config(text=text, fg=panel["color"])
                else:
                    panel["slots"][slot].config(text="—", fg=MUTED)
        self.pool_label.config(text=f"{len(self.character_pool)} CHARACTERS LEFT")

    #

    def prepare_turn(self):
        """Reveal one character and begin an alternating two-player auction."""
        if all(not player.has_empty_slots() for player in self.players):
            self.finish_game()
            return
        attempts = 0
        while not self.players[self.current_player_index].has_empty_slots() and attempts < 2:
            self.current_player_index = (self.current_player_index + 1) % 2
            attempts += 1
        if not self.character_pool:
            self.finish_game(pool_exhausted=True)
            return
        self.current_character = self.character_pool.pop()
        self.high_bid = 0
        self.high_bidder_index = None
        self.current_slot = self.players[self.current_player_index].next_slot()
        self.update_builds()
        self.show_current_auction()

    #

    def show_current_auction(self):
        player = self.players[self.current_player_index]
        self.current_slot = player.next_slot()
        player_color = PLAYER_COLORS[self.current_player_index]
        self.turn_label.config(
            text=f"{player.name.upper()}'S BID  •  £{player.balance} AVAILABLE",
            fg=player_color
        )
        self.slot_label.config(text=f"Choose for: {self.current_slot}")
        self.character_name_label.config(text=self.current_character["name"])
        self.anime_tag_label.config(text=f"FROM {self.current_character['anime']}")
        if self.high_bidder_index is None:
            bid_text = "No bids yet. Enter at least £1 to start the auction."
        else:
            leader = self.players[self.high_bidder_index]
            bid_text = f"Highest bid: £{self.high_bid} by {leader.name}. Enter a higher bid or pass."
        minimum = self.high_bid + 1
        can_bid = player.has_empty_slots() and player.balance >= minimum
        if not player.has_empty_slots():
            bid_text = f"{player.name} has filled all stat slots and cannot bid. Pass to continue."
        elif not can_bid:
            if self.high_bidder_index is None:
                bid_text = f"{player.name} has £{player.balance}. No bid required to receive a character for free; pass to continue."
            else:
                bid_text = f"You have £{player.balance} and cannot beat £{self.high_bid}. Pass to close the auction."
        status_color = (PLAYER_COLORS[self.high_bidder_index] if self.high_bidder_index is not None
                        else PLAYER_COLORS[self.current_player_index])
        self.status_label.config(text=bid_text, fg=status_color)
        self.buy_button.config(text="PLACE BID", state="normal" if can_bid else "disabled")
        self.pass_button.config(state="normal")
        self.bid_entry.config(state="normal" if can_bid else "disabled")
        self.bid_entry.delete(0, "end")
        self.bid_entry.insert(0, str(minimum) if can_bid else "0")
        if can_bid:
            self.bid_entry.focus_set()
        self.update_builds()

    #

    def buy_character(self):
        """Place a bid, then give the other player the next bidding turn."""
        if self.game_finished or self.current_character is None:
            return
        player = self.players[self.current_player_index]
        try:
            bid = int(self.bid_entry.get().strip())
        except ValueError:
            messagebox.showerror("Invalid bid", "Enter a whole number for your bid.")
            return
        minimum = self.high_bid + 1
        if bid < minimum:
            messagebox.showerror("Invalid bid", f"Your bid must be at least £{minimum}.")
            return
        if bid > player.balance:
            messagebox.showerror("Not enough money", f"You only have £{player.balance} available.")
            return
        self.high_bid = bid
        self.high_bidder_index = self.current_player_index
        self.log_label.config(
            text=f"{player.name} bids £{bid} for {self.current_character['name']} "
                 f"[{self.current_character['anime']}].",
            fg=PLAYER_COLORS[self.current_player_index]
        )
        self.current_player_index = (self.current_player_index + 1) % 2
        other = self.players[self.current_player_index]
        if not other.has_empty_slots():
            self.award_character(self.high_bidder_index, self.high_bid)
            return
        if other.balance <= self.high_bid:
            self.award_character(self.high_bidder_index, self.high_bid)
            return
        self.show_current_auction()

    #

    def pass_character(self):
        """Offer a passed character to the other player for free.

        If they decline, discard this character and let the passer start
        the next character's auction.
        """
        if self.game_finished or self.current_character is None:
            return
        passer_index = self.current_player_index
        passer = self.players[passer_index]
        other_index = (passer_index + 1) % 2
        other = self.players[other_index]
        character = self.current_character
        if other.has_empty_slots():
            wants_character = messagebox.askyesno(
                "Free character offer",
                f"{passer.name} passed on {character['name']} "
                f"[{character['anime']}].\\n\\n"
                f"{other.name}, would you like to take this character for FREE?"
            )
        else:
            wants_character = False
            self.log_label.config(
                text=f"{other.name} has no empty stat slots, so cannot take "
                     f"{character['name']} for free."
            )
        if wants_character:
            self.log_label.config(
                text=f"{other.name} accepted {character['name']} "
                     f"[{character['anime']}] for free."
            )
            self.award_character(other_index, 0)
            return
        self.log_label.config(
            text=f"{other.name} declined {character['name']} "
                 f"[{character['anime']}]. Moving to the next character."
        )
        self.current_player_index = passer_index
        self.prepare_turn()

    #

    def award_character(self, winner_index, cost):
        winner = self.players[winner_index]
        character = self.current_character
        slot = winner.next_slot()
        if slot is None:
            self.current_player_index = (winner_index + 1) % 2
            self.prepare_turn()
            return
        winner.add_character(slot, character, cost)
        self.log_label.config(
            text=f"{winner.name} drafted {character['name']} [{character['anime']}] "
                 f"for {slot} at £{cost}."
        )
        self.current_player_index = (winner_index + 1) % 2
        self.prepare_turn()

    #

    def finish_game(self, pool_exhausted=False):
        self.game_finished = True
        self.clear_window()
        outer = tk.Frame(self.root, bg=BG, padx=24, pady=22)
        outer.pack(fill="both", expand=True)
        title = "DRAFT COMPLETE" if not pool_exhausted else "CHARACTER POOL EMPTY"
        self.make_label(outer, title, 23, TEXT, True, bg=BG).pack(pady=(8, 4))
        subtitle = "Compare both builds and decide who wins." if not pool_exhausted else "The pool ran out before both builds were complete."
        self.make_label(outer, subtitle, 10, MUTED, bg=BG).pack(pady=(0, 18))
        columns = tk.Frame(outer, bg=BG)
        columns.pack(fill="both", expand=True)
        columns.grid_columnconfigure(0, weight=1, uniform="final")
        columns.grid_columnconfigure(1, weight=1, uniform="final")
        for i, player in enumerate(self.players):
            panel = tk.Frame(columns, bg=PANEL, padx=18, pady=18)
            panel.grid(row=0, column=i, sticky="nsew", padx=(0, 8) if i == 0 else (8, 0))
            self.make_label(panel, player.name, 16, ACCENT, True, bg=PANEL).pack(anchor="w")
            self.make_label(panel, f"Money remaining: £{player.balance}", 10, GREEN, True, bg=PANEL).pack(anchor="w", pady=(3, 12))
            for slot in STAT_SLOTS:
                entry = player.build.get(slot)
                if entry:
                    character = entry["character"]
                    text = f"{character['name']} [{character['anime']}]\nPaid: £{entry['cost']}"
                    color = TEXT
                else:
                    text = "Not filled"
                    color = MUTED
                row = tk.Frame(panel, bg=PANEL_ALT, padx=10, pady=8)
                row.pack(fill="x", pady=3)
                self.make_label(row, slot.upper(), 8, MUTED, True, bg=PANEL_ALT, width=14, anchor="w").pack(side="left")
                self.make_label(row, text, 9, color, bg=PANEL_ALT, justify="left", wraplength=300, anchor="w").pack(side="left", fill="x", expand=True)
        bottom = tk.Frame(outer, bg=BG)
        bottom.pack(fill="x", pady=(18, 0))
        self.make_button(bottom, "NEW GAME", self.show_setup).pack(side="left")
        self.make_button(bottom, "CLOSE", self.root.destroy, bg="#2a3652", fg=TEXT).pack(side="right")

#

def main():
    root = tk.Tk()
    AnimeDraftGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()