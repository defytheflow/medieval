import os
import tkinter as tk

from PIL import Image, ImageTk

WIN_WIDTH = 1200
WIN_HEIGHT = 900

BTN_WIDTH = 110
BTN_HEIGHT = 110

BG_COLOR = '#c9b662'

# --------------------------------------------------------------------------------
# MAIN WINDOW.
# --------------------------------------------------------------------------------

window = tk.Tk()
window.title('Medieval')
window.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')
window.resizable(0, 0)

# --------------------------------------------------------------------------------
# TOP FRAME.
# --------------------------------------------------------------------------------

top_frame = tk.Frame(window, height=WIN_HEIGHT // 9)
top_frame.pack(fill=tk.BOTH)

hint_label = tk.Label(
    top_frame, text='Hint: Pirates are bad!', fg='#181c21', bg=BG_COLOR,
    anchor=tk.NW, relief=tk.RAISED, bd=5, padx=10
)
hint_label.pack(fill=tk.BOTH)

# --------------------------------------------------------------------------------
# MIDDLE FRAME.
# --------------------------------------------------------------------------------

middle_frame = tk.Frame(window)
middle_frame.pack(fill=tk.BOTH)

# MAIN CANVAS.
main_canvas = tk.Canvas(
    middle_frame, width=WIN_WIDTH * 0.9, height=WIN_HEIGHT * 7 / 9,  bg='#000', relief=tk.FLAT
)
main_canvas.pack(fill=tk.BOTH, side=tk.LEFT)

main_canvas_image = ImageTk.PhotoImage(
    Image.open(os.path.join('assets','bazaar.jpg')).resize((int(WIN_WIDTH * 0.8), int(WIN_HEIGHT * 7 / 9)))
)
main_canvas_image_id = main_canvas.create_image(0, 0, image=main_canvas_image, anchor=tk.NW)

# MIDDLE RIGHT FRAME.
middle_right_frame = tk.Frame(middle_frame)
middle_right_frame.pack(fill=tk.BOTH, side=tk.LEFT)

# SETTINGS BUTTON.
settings_btn_img = ImageTk.PhotoImage(
    Image.open(os.path.join('assets', 'settings-btn.png')).resize((BTN_WIDTH, BTN_HEIGHT))
)
settings_btn = tk.Button(
    middle_right_frame, image=settings_btn_img, bg=BG_COLOR, bd=5,
    highlightbackground='#000', activebackground='#7f6f28',
)
settings_btn.pack(fill=tk.BOTH)

# MAP BUTTON.
map_btn_img = ImageTk.PhotoImage(
    Image.open(os.path.join('assets', 'map-btn.png')).resize((BTN_WIDTH, BTN_HEIGHT))
)
map_btn = tk.Button(
    middle_right_frame, image=map_btn_img, bg=BG_COLOR, bd=5,
    highlightbackground='#000', activebackground='#7f6f28',
)
map_btn.pack(fill=tk.BOTH)

# INVENTORY BUTTON.
inventory_btn_img = ImageTk.PhotoImage(
    Image.open(os.path.join('assets', 'inventory-btn.png')).resize((BTN_WIDTH, BTN_HEIGHT))
)
inventory_btn = tk.Button(
    middle_right_frame, image=inventory_btn_img, bg=BG_COLOR, bd=5,
    highlightbackground='#000', activebackground='#7f6f28',
)
inventory_btn.pack(fill=tk.BOTH)

# OTHER BUTTONS.
btn4 = tk.Button(
    middle_right_frame, bg=BG_COLOR, bd=5, text='4',
    highlightbackground='#000', activebackground='#7f6f28',
)
btn4.pack(fill=tk.BOTH, expand=True)

btn5 = tk.Button(
    middle_right_frame, bg=BG_COLOR, bd=5, text='5',
    highlightbackground='#000', activebackground='#7f6f28',
)
btn5.pack(fill=tk.BOTH, expand=True)

btn6 = tk.Button(
    middle_right_frame, bg=BG_COLOR, bd=5, text='6',
    highlightbackground='#000', activebackground='#7f6f28',
)
btn6.pack(fill=tk.BOTH, expand=True)

# --------------------------------------------------------------------------------
# BOTTOM FRAME.
# --------------------------------------------------------------------------------

bottom_frame = tk.Frame(window)
bottom_frame.pack(fill=tk.BOTH, expand=True)

# BOTTOM CANVAS.
bottom_canvas = tk.Canvas(
    bottom_frame, width=180, bg=BG_COLOR, relief=tk.RAISED, highlightbackground='#000', bd=5
)
bottom_canvas.pack(fill=tk.BOTH, side=tk.LEFT)

bottom_canvas_image = ImageTk.PhotoImage(
    Image.open(os.path.join('assets', 'witch.png')).resize((200, 200))
)
bottom_canvas_image_id = bottom_canvas.create_image(0, 0, image=bottom_canvas_image, anchor=tk.NW)

# BOTTOM RIGHT FRAME.
bottom_right_frame = tk.Frame(bottom_frame, width=WIN_WIDTH - 180, bg=BG_COLOR, bd=5, relief=tk.RAISED)
bottom_right_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# DIALOGUE LABEL.
dialogue_label = tk.Label(
    bottom_right_frame, text='Do you want to start?', fg='#181c21', bg=BG_COLOR,
    anchor=tk.NW, relief=tk.RAISED, bd=5, padx=10
)
dialogue_label.pack(fill=tk.BOTH)

# CHOICE BUTTONS.
choice_var = tk.IntVar()

choice_btn_img = ImageTk.PhotoImage(
    Image.open(os.path.join('assets', 'choice-btn.png')).resize((180, 90))
)

choice_btn1 = tk.Radiobutton(
    bottom_right_frame, text='Yes', variable=choice_var, value=1, image=choice_btn_img,
    bg=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BG_COLOR, compound=tk.CENTER
)
choice_btn1.pack(side=tk.LEFT, expand=True)

choice_btn2 = tk.Radiobutton(
    bottom_right_frame, text='No', variable=choice_var, value=2, image=choice_btn_img,
    bg=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BG_COLOR, compound=tk.CENTER
)
choice_btn2.pack(side=tk.LEFT, expand=True)

if __name__ == '__main__':
    window.mainloop()
