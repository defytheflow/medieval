import os


WIDTH = 1200
HEIGHT = WIDTH * 3 // 4

BG_COLOR = '#c9b662'
ACTIVE_BG_COLOR = '#7f6f28'

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_ROOT = os.path.join(ROOT, 'assets')
ICONS_ROOT = os.path.join(ASSETS_ROOT, 'icons')
SPRITES_ROOT = os.path.join(ASSETS_ROOT, 'sprites')
SOUNDS_ROOT = os.path.join(ASSETS_ROOT, 'sounds')
