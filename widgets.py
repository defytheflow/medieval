import tkinter as tk


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
