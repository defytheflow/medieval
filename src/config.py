import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')


class WindowConfig:
    title = 'Medieval'
    width = 1200
    height = width // 16 * 10


class GameCanvasConfig:
    width = WindowConfig.width * 4 // 5
    height = width * 3 // 4
    block_size = WindowConfig.width // 50


class ColorsConfig:
    fg = '#000'
    bg = '#c9b662'
    active_bg = '#7f6f28'
    highlight_bg = '#000'


class FontsConfig:
    h = ('DejaVu Serif', 32, 'bold')
    p = ('DejaVu Serif', 20, 'normal')


class AssetsConfig:
    bg = os.path.join(ASSETS_DIR, 'bg')
    icons = os.path.join(ASSETS_DIR, 'icons')
    sounds = os.path.join(ASSETS_DIR, 'sounds')
    sprites = os.path.join(ASSETS_DIR, 'sprites')


class KeyBindsConfig:
    show_game = 'G',
    show_map = 'M',
    show_settings = 'S'
    settings_switch_lang = 'L',
    character_move_north = 'w',
    character_move_west  = 'a',
    character_move_south = 's',
    character_move_east = 'd',
