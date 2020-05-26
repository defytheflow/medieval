import os
import tkinter as tk

import utils
from widgets import ToolTipButton, BilingualLabel, Radiobutton


class GameCanvas(tk.Canvas):

    SQUARE = 20

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ROCK_IMAGE = utils.create_photo_image(
            os.path.join('assets', 'rock.jpeg'), (self.SQUARE, self.SQUARE))
        self.WATER_IMAGE = utils.create_photo_image(
            os.path.join('assets', 'water.jpeg'), (self.SQUARE, self.SQUARE))
        self.GRASS_IMAGE = utils.create_photo_image(
            os.path.join('assets', 'grass.png'), (self.SQUARE, self.SQUARE))

    # Public
    def generate_level(self, level_num):
        if level_num == 1:
            self._generate_level_one()

    # Private
    def _generate_level_one(self):
        x, y = 0, 0

        # LINE OF ROCKS
        for i in range(int(self['width']) // self.SQUARE):
            self.create_image(x, y, image=self.ROCK_IMAGE, anchor='nw')
            x += self.SQUARE
        y += self.SQUARE

        # MIDDLE GRASS
        for i in range(int(self['height']) // self.SQUARE - 2):  # two lines of rocks.

            # LEFT ROCK
            x = 0
            self.create_image(x, y, image=self.ROCK_IMAGE, anchor='nw')
            x += self.SQUARE

            # GRASS ROW
            for j in range(int(self['width']) // self.SQUARE - 2): # two rocks.
                self.create_image(x, y, image=self.GRASS_IMAGE, anchor='nw')
                x += self.SQUARE

            # RIGHT ROCK
            self.create_image(x, y, image=self.ROCK_IMAGE, anchor='nw')

            y += self.SQUARE

        # LINE OF ROCKS
        x = 0
        for i in range(int(self['width']) // self.SQUARE):
            self.create_image(x, y, image=self.ROCK_IMAGE, anchor='nw')
            x += self.SQUARE


class MainFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Public bindable Buttons.
        self.settings_btn = None
        self.map_btn = None
        self.inventory_btn = None
        self.market_btn = None
        self.bank_btn = None
        self.smith_btn = None

        # Public bindable Labels.
        self.hint_lbl = None
        self.dialogue_lbl = None

        # Public canvases.
        self.game_canvas = None
        self.bottom_canvas = None

        # Public Variables.
        self.choice_var = tk.IntVar(self)

        self._init_top_frame()
        self._init_middle_frame()
        self._init_bottom_frame()

    def _init_top_frame(self):
        """
            Handles construction of the top frame.
        """
        top_frame = tk.Frame(self)
        top_frame.pack(fill=tk.BOTH)

        self.hint_lbl = BilingualLabel(
            top_frame,
            text_dict={
                'eng': 'Hint:',
                'rus': 'Подсказка:'
            },
            background=self['background'],
            foreground='#000',
            borderwidth=5,
            padx=10,
            relief=tk.RAISED,
            anchor=tk.NW,
        )
        self.hint_lbl.pack(fill=tk.BOTH)

    def _init_middle_frame(self):
        """
            Handles construction of middle frame.
        """
        middle_frame = tk.Frame(self)
        middle_frame.pack(fill=tk.BOTH)

        self.game_canvas = GameCanvas(
            middle_frame,
            width=self['width'] * 0.9,
            height=self['height'] * 7 / 9,
            highlightbackground='#000',
            relief=tk.FLAT,
        )
        self.game_canvas.pack(side=tk.LEFT, fill=tk.BOTH)
        self.game_canvas.generate_level(1)

        middle_right_frame = tk.Frame(middle_frame)
        middle_right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.settings_btn = ToolTipButton(
            middle_right_frame,
            file=os.path.join('assets', 'settings-icon.png'),
            text_dict={
                'eng': 'Settings',
                'rus': 'Настройки'
            }
        )
        self.settings_btn.pack(fill=tk.BOTH, expand=True)

        self.map_btn = ToolTipButton(
            middle_right_frame,
            file=os.path.join('assets', 'map-icon.png'),
            text_dict={
                'eng': 'Map',
                'rus': 'Карта'
            }
        )
        self.map_btn.pack(fill=tk.BOTH, expand=True)

        self.inventory_btn = ToolTipButton(
            middle_right_frame,
            file=os.path.join('assets', 'inventory-icon.png'),
            text_dict={
                'eng': 'Inventory',
                'rus': 'Инвентарь'
            }
        )
        self.inventory_btn.pack(fill=tk.BOTH, expand=True)
        self.inventory_btn.configure(state=tk.DISABLED)

        self.market_btn = ToolTipButton(
            middle_right_frame,
            file=os.path.join('assets', 'market-icon.png'),
            text_dict={
                'eng': 'Market',
                'rus': 'Магазин'
            }
        )
        self.market_btn.pack(fill=tk.BOTH, expand=True)
        self.market_btn.configure(state=tk.DISABLED)

        self.bank_btn = ToolTipButton(
            middle_right_frame,
            file=os.path.join('assets', 'coin-icon.png'),
            text_dict={
                'eng': 'Bank',
                'rus': 'Банк'
            }
        )
        self.bank_btn.pack(fill=tk.BOTH, expand=True)
        self.bank_btn.configure(state=tk.DISABLED)

        self.smith_btn = ToolTipButton(
            middle_right_frame,
            file=os.path.join('assets', 'smith-icon.png'),
            text_dict={
                'eng': 'Smith',
                'rus': 'Кузнец'
            },
        )
        self.smith_btn.pack(fill=tk.BOTH, expand=True)
        self.smith_btn.configure(state=tk.DISABLED)

    def _init_bottom_frame(self):
        """
            Handles construction of the bottom frame.
        """
        bottom_frame = tk.Frame(self)
        bottom_frame.pack(fill=tk.BOTH)

        self.bottom_canvas = tk.Canvas(
            bottom_frame,
            width=180,
            background=self['background'],
            borderwidth=5,
            highlightbackground='#000',
            relief=tk.RAISED,
        )
        self.bottom_canvas.pack(side=tk.LEFT, fill=tk.BOTH)

        self.bottom_canvas_image = utils.create_photo_image(
            os.path.join('assets', 'witch.png'),
            (200, 200),
        )
        self.bottom_canvas.create_image(
            0, 0, image=self.bottom_canvas_image, anchor=tk.NW
        )

        bottom_right_frame = tk.Frame(
            bottom_frame,
            width=(self['width'] - int(self.bottom_canvas['width'])),
            background=self['background'],
            borderwidth=5,
            relief=tk.RAISED
        )
        bottom_right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.dialogue_lbl = BilingualLabel(
            bottom_right_frame,
            text_dict={
                'eng': 'Question',
                'rus': 'Вопрос'
            },
            background=self['background'],
            foreground='#000',
            borderwidth=5,
            padx=10,
            relief=tk.RAISED,
            anchor=tk.NW
        )
        self.dialogue_lbl.pack(fill=tk.BOTH)

        choice_btn1 = Radiobutton(
            bottom_right_frame,
            text='Yes',
            value=1,
            variable=self.choice_var
        )
        choice_btn1.pack(side=tk.LEFT, expand=True)

        choice_btn2 = Radiobutton(
            bottom_right_frame,
            text='No',
            value=2,
            variable=self.choice_var
        )
        choice_btn2.pack(side=tk.LEFT, expand=True)
