import os
import tkinter as tk

from utils import create_photo_image


class ToolTip:

    def __init__(self, text):
        self.toplevel = None
        self.text = text
        self.lbl_padx = 10

    def show(self, event):
        x = event.widget.winfo_rootx() - len(self.text) - self.lbl_padx
        y = event.widget.winfo_rooty()
        self.toplevel = tk.Toplevel(event.widget)
        self.toplevel.wm_geometry('+%d+%d' % (x, y))
        self.toplevel.wm_overrideredirect(1)
        label = tk.Label(self.toplevel,
                         text=self.text,
                         background='#c9b662',
                         bd=3,
                         padx=self.lbl_padx,
                         font=('DejaVu Serif', '12', 'italic'),
                         relief=tk.RAISED)
        label.pack(fill=tk.BOTH, expand=True)

    def hide(self, event):
        if self.toplevel:
            self.toplevel.destroy()


class SettingsFrame(tk.Frame):

    BACK_BTN_IMAGE = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        top_frame = tk.Frame(self, background='#c9b662')
        top_frame.pack(side=tk.TOP, fill=tk.BOTH)

        self.BACK_BTN_IMAGE = create_photo_image(
            os.path.join('assets', 'back-btn.png'),
            (80, 60),
        )

        back_btn = tk.Button(top_frame,
                             width=100,
                             height=60,
                             image=self.BACK_BTN_IMAGE,
                             bd=5,
                             background='#c9b662',
                             highlightbackground='#000',
                             activebackground='#7f6f28',
                             relief=tk.RAISED,
                             )
        back_btn.pack(side=tk.LEFT)

