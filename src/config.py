import os

WINDOW_TITLE = 'Medieval'

# Window dimensions.

WINDOW_WIDTH = 1200

WINDOW_HEIGHT = WINDOW_WIDTH * 3 // 4 + 50

BLOCK_SIZE = WINDOW_WIDTH // 40

GAME_CANVAS_WIDTH = WINDOW_WIDTH * 4 // 5

GAME_CANVAS_HEIGHT = GAME_CANVAS_WIDTH * 3 // 4

# Background colors.

BG = '#c9b662'

ACTIVE_BG = '#7f6f28'

HIGHLIGHT_BG = '#000'

# Foreground colors.

FG = '#000'

# Fonts.

H_FONT = ('DejaVu Serif', 32, 'bold')

P_FONT = ('DejaVu Serif', 20)

# Asset paths.

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ASSETS_ROOT = os.path.join(ROOT, 'assets')

BG_ROOT = os.path.join(ASSETS_ROOT, 'bg')

ICONS_ROOT = os.path.join(ASSETS_ROOT, 'icons')

SPRITES_ROOT = os.path.join(ASSETS_ROOT, 'sprites')

SOUNDS_ROOT = os.path.join(ASSETS_ROOT, 'sounds')

# Bindings.

KEY_BINDS = {
    'show-game':            'G',
    'show-map':             'M',
    'show-settings':        'S',

    'settings-switch-lang': 'L',

    'character-move-north': 'w',
    'character-move-west':  'a',
    'character-move-south': 's',
    'character-move-east':  'd',
}
