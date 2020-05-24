import os
import tkinter as tk

from widgets import Button, Label, Radiobutton
from utils import create_photo_image


class MainFrame(tk.Frame):

    BG_COLOR = '#c9b662'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.top_frame = tk.Frame(self)
        self.top_frame.pack(fill=tk.BOTH)

        hint_lbl = Label(self.top_frame,
                         text_dict={
                             'eng': 'Hint:',
                             'rus': 'Подсказка:'
                         })
        hint_lbl.pack(fill=tk.BOTH)

        self.middle_frame = tk.Frame(self, bg='red')
        self.middle_frame.pack(fill=tk.BOTH)

        main_canvas = tk.Canvas(self.middle_frame,
                                width=self.winfo_reqwidth() * 0.9,
                                height=self.winfo_reqheight() * 7 / 9,
                                highlightbackground='#000',
                                relief=tk.FLAT)
        main_canvas.pack(side=tk.LEFT, fill=tk.BOTH)

        self.main_canvas_image = create_photo_image(
            os.path.join('assets', 'bazaar.jpg'),
            (main_canvas.winfo_reqwidth(), main_canvas.winfo_reqheight()),
        )
        main_canvas.create_image(
            0, 0, image=self.main_canvas_image, anchor=tk.NW
        )

        self.middle_right_frame = tk.Frame(self.middle_frame)
        self.middle_right_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        self.settings_btn = Button(self.middle_right_frame,
                                   file=os.path.join('assets', 'settings-icon.png'),
                                   tooltip={
                                       'eng': 'Settings',
                                       'rus': 'Настройки'
                                   })
        self.settings_btn.pack(fill=tk.BOTH)

        self.map_btn = Button(self.middle_right_frame,
                              file=os.path.join('assets', 'map-icon.png'),
                              tooltip={
                                  'eng': 'Map',
                                  'rus': 'Карта'
                              })
        self.map_btn.pack(fill=tk.BOTH)

        self.inventory_btn = Button(self.middle_right_frame,
                                    file=os.path.join('assets', 'inventory-icon.png'),
                                    tooltip={
                                        'eng': 'Inventory',
                                        'rus': 'Инвентарь'
                                    })
        self.inventory_btn.pack(fill=tk.BOTH)

        btn4 = Button(self.middle_right_frame)
        btn4.pack(fill=tk.BOTH, expand=True)

        btn5 = Button(self.middle_right_frame)
        btn5.pack(fill=tk.BOTH, expand=True)

        btn6 = Button(self.middle_right_frame)
        btn6.pack(fill=tk.BOTH, expand=True)

        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack(fill=tk.BOTH)

        bottom_canvas = tk.Canvas(self.bottom_frame,
                                  width=180,
                                  background=self.BG_COLOR,
                                  borderwidth=5,
                                  highlightbackground='#000',
                                  relief=tk.RAISED)
        bottom_canvas.pack(side=tk.LEFT, fill=tk.BOTH)

        self.bottom_canvas_image = create_photo_image(
            os.path.join('assets', 'witch.png'),
            (200, 200),
        )
        bottom_canvas.create_image(
            0, 0, image=self.bottom_canvas_image, anchor=tk.NW
        )

        self.bottom_right_frame = tk.Frame(self.bottom_frame,
                                           width=(self.winfo_reqwidth() -
                                                  bottom_canvas.winfo_reqwidth()),
                                           background=self.BG_COLOR,
                                           borderwidth=5,
                                           relief=tk.RAISED)
        self.bottom_right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        dialogue_lbl = Label(self.bottom_right_frame,
                             text_dict={
                                 'eng': 'Question',
                                 'rus': 'Вопрос'
                             })
        dialogue_lbl.pack(fill=tk.BOTH)

        choice_var = tk.IntVar()
        choice_btn1 = Radiobutton(self.bottom_right_frame,
                                  text='Yes',
                                  value=1,
                                  variable=choice_var)
        choice_btn1.pack(side=tk.LEFT, expand=True)

        choice_btn2 = Radiobutton(self.bottom_right_frame,
                                  text='No',
                                  value=2,
                                  variable=choice_var)
        choice_btn2.pack(side=tk.LEFT, expand=True)
