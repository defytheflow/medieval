import os
import tkinter as tk

from widgets import ToolTipButton, BilingualLabel, Radiobutton
from utils import create_photo_image


class MainFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Buttons.
        self.settings_btn = None
        self.map_btn = None
        self.inventory_btn = None
        self.store_btn = None

        # Labels.
        self.hint_lbl = None
        self.dialogue_lbl = None

        # Canvases.
        self.main_canvas = None
        self.bottom_canvas = None

        # Variables.
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

        self.main_canvas = tk.Canvas(
            middle_frame,
            width=self['width'] * 0.9,
            height=self['height'] * 7 / 9,
            highlightbackground='#000',
            relief=tk.FLAT,
        )
        self.main_canvas.pack(side=tk.LEFT, fill=tk.BOTH)

        self.main_canvas_image = create_photo_image(
            os.path.join('assets', 'bazaar.jpg'),
            (int(self.main_canvas['width']), int(self.main_canvas['height'])),
        )
        self.main_canvas.create_image(
            0, 0, image=self.main_canvas_image, anchor=tk.NW
        )

        middle_right_frame = tk.Frame(middle_frame)
        middle_right_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        self.settings_btn = ToolTipButton(
            middle_right_frame,
            file=os.path.join('assets', 'settings-icon.png'),
            text_dict={
                'eng': 'Settings',
                'rus': 'Настройки'
            }
        )
        self.settings_btn.pack(fill=tk.BOTH)

        self.map_btn = ToolTipButton(
            middle_right_frame,
            file=os.path.join('assets', 'map-icon.png'),
            text_dict={
                'eng': 'Map',
                'rus': 'Карта'
            }
        )
        self.map_btn.pack(fill=tk.BOTH)

        self.inventory_btn = ToolTipButton(
            middle_right_frame,
            file=os.path.join('assets', 'inventory-icon.png'),
            text_dict={
                'eng': 'Inventory',
                'rus': 'Инвентарь'
            }
        )
        self.inventory_btn.pack(fill=tk.BOTH)

        # TODO store button.
        # btn4 = ToolTipButton(self.middle_right_frame)
        # btn4.pack(fill=tk.BOTH, expand=True)

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

        self.bottom_canvas_image = create_photo_image(
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
