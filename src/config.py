import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class WindowConfig:
    title = 'Medieval'
    width = 1200
    height = width // 16 * 10


class GameCanvasConfig:
    width = WindowConfig.width
    height = WindowConfig.height


class GameMapConfig:
    width = WindowConfig.width * 10
    height = WindowConfig.height * 10
    size = (width, height)


class ColorsConfig:
    fg = '#000'
    bg = '#c9b662'
    active_bg = '#7f6f28'
    highlight_bg = '#000'


class FontsConfig:
    h = ('DejaVu Serif', 32, 'bold')
    p = ('DejaVu Serif', 20, 'normal')


class AssetsConfig:
    assets = os.path.join(BASE_DIR, 'assets')
    bg = os.path.join(assets, 'bg')
    icons = os.path.join(assets, 'icons')
    sounds = os.path.join(assets, 'sounds')
    sprites = os.path.join(assets, 'sprites')


class KeyBindsConfig:
    show_game = 'G'
    show_map = 'M'
    character_move_north = 'w'
    character_move_west  = 'a'
    character_move_south = 's'
    character_move_east = 'd'
