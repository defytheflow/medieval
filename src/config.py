import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

WINDOW = {
    'title': 'Medieval',
    'width':  1200,
    'height': 1200 * 3 // 4,
}

GAME_CANVAS = {
    'width':      WINDOW['width'] * 4 // 5,
    'height':     WINDOW['width'] * 4 // 5 * 3 // 4,
    'block_size': WINDOW['width'] // 40,
}

COLORS = {
    'fg':           '#000',
    'bg':           '#c9b662',
    'active_bg':    '#7f6f28',
    'highlight_bg': '#000',
}

FONTS = {
    'h': ('DejaVu Serif', 32, 'bold'),
    'p': ('DejaVu Serif', 20, 'normal'),
}

ASSETS = {
    'bg':      os.path.join(ASSETS_DIR, 'bg'),
    'icons':   os.path.join(ASSETS_DIR, 'icons'),
    'sounds':  os.path.join(ASSETS_DIR, 'sounds'),
    'sprites': os.path.join(ASSETS_DIR, 'sprites'),
}

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
