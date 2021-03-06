from game.shared.color import Color

DEBUG = False

MAX_X = 1040
MAX_Y = 680
CENTER_X = int(MAX_X / 2)
CENTER_Y = int(MAX_Y / 2)

FRAME_RATE = 60
WINDOW_TITLE = "Galaxy Defenders"

#SOUNDS
GAME_THEME = "galdef/assets/sounds/game_theme.mp3"
ALIEN_BULLET_SOUND = "galdef/assets/sounds/phaser.wav"
BULLET_SOUND = "galdef/assets/sounds/laser.wav"
EXPLOSION_SOUNDS = [
    "galdef/assets/sounds/explosion1.wav",
    "galdef/assets/sounds/explosion2.wav"
]

# FONT
FONT_FILE = "galdef/assets/fonts/Revamped.ttf" # "galdef/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# HIGH SCORE
HIGH_SCORE_FILE = "galdef/assets/save_game/high_score.txt"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# MESSAGES
MESSAGE_GROUP = "messages"


GAME_OVER_MESS_GROUP = "game_over"
GAME_START_MESS_GROUP = "start_game"
GAME_OVER_MESS_FORMAT = "{}"
GAME_START_MESS_FORMAT = "{}"

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
KILLS_GROUP = "kills"
RESTART_MESS_GROUP = "restart"
EXIT_MESS_GROUP = "exit"
RESTART_MESS_FORMAT = "{}"
EXIT_MESS_FORMAT = "{}"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {:,}"
KILLS_FORMAT = "KILLS: {:,}"

#COLORS
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
PURPLE = Color(255,0,255)

# PROJECTILE
SHIP_PROJECTILE_GROUP = "ship_projectiles".lower()
ALIEN_PROJECTILE_GROUP = "alien_projectiles".lower()
SHIP_PROJECTILE_BULLET_IMAGE = "galdef/assets/images/bullet.png"
ALIEN_PROJECTILE_BULLET_IMAGE = "galdef/assets/images/alien_bullet.png"
PROJECTILE_WIDTH = 11
PROJECTILE_HEIGHT = 11
PROJECTILE_VELOCITY = 10

# LEVEL BACKGROUNDS
BACKGROUND_GROUP = "Background".lower()
BACKGROUND_WIDTH = "1040"
BACKGROUND_HEIGHT = "680"
BACKGROUND_IMAGES = [
    "galdef/assets/images/backgrounds/future_city_background.png",
    "galdef/assets/images/backgrounds/cosmic_cliffs_background.png",
    "galdef/assets/images/backgrounds/stellar_ring_of_death_background.png",
    "galdef/assets/images/backgrounds/stephans_quintet_background.png",
    "galdef/assets/images/backgrounds/arawn_dystopia.png",
    "galdef/assets/images/backgrounds/nebula_background.png",
    "galdef/assets/images/backgrounds/snippet_of_creation_background.png",
    "galdef/assets/images/backgrounds/dark_city_background.png",
    
]

# SHIP
SHIP_GROUP = "ship".lower()
SHIP_IMAGE = "galdef/assets/images/spaceship.png"
SHIP_WIDTH = 60
SHIP_HEIGHT = 60
SHIP_RATE = 6
SHIP_VELOCITY = 7

# ALIEN
ALIEN_GROUP = "aliens".lower()
ALIEN_IMAGES = [
    [f"galdef/assets/images/{i:03}.png" for i in range(10,11)],
    [f"galdef/assets/images/{i:03}.png" for i in range(20,21)],
    [f"galdef/assets/images/{i:03}.png" for i in range(30,31)],
    [f"galdef/assets/images/{i:03}.png" for i in range(40,41)],
    [f"galdef/assets/images/{i:03}.png" for i in range(50,51)]
]
    
ALIEN_WIDTH = 50
ALIEN_HEIGHT = 40
ALIEN_DELAY = 0.5
ALIEN_RATE = 4
ALIEN_GRID_ROWS = 5
ALIEN_GRID_COLUMNS = 10

EXPLOSION_GROUP = "explosions".lower()
EXPLOSION_IMAGES = {
    "explosions": [f"galdef/assets/images/{i:03}.png" for i in range(500,506)],
}
EXPLOSION_WIDTH = 80
EXPLOSION_HEIGHT = 80
EXPLOSION_VELOCITY = 0

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"
MUTE = "m"
RESET = "r"
HARDCORE = "h"
PLUS = "+"
MINUS = "-"

# GAME PHASES
INPUT = "input"
UPDATE = "update"
OUTPUT = "output"
