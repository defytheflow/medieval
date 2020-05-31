import os

# Window dimensions.

WIDTH = 1200

HEIGHT = WIDTH * 3 // 4

BLOCK_SIZE = 30

# Background colors.

BG = '#c9b662'

ACTIVE_BG = '#7f6f28'

HIGHLIGHT_BG = '#000'

# Fonts.

H_FONT = ('DejaVu Serif', 32, 'bold')

P_FONT = ('DejaVu Serif', 20)

# Asset paths.

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ASSETS_ROOT = os.path.join(ROOT, 'assets')

ICONS_ROOT = os.path.join(ASSETS_ROOT, 'icons')

SPRITES_ROOT = os.path.join(ASSETS_ROOT, 'sprites')

SOUNDS_ROOT = os.path.join(ASSETS_ROOT, 'sounds')

# Bindings.

KEYBOARD_BINDS = {
    'show-game-frame':      'G',
    'show-map-frame':       'M',
    'show-settings-frame':  'S',
    'settings-switch-lang': 'L',
}
