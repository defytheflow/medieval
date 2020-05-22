import os
import tkinter as tk

from PIL import Image, ImageTk


BTN_WIDTH = 110
BTN_HEIGHT = 110


# Create a main window.
window = tk.Tk()

# Configure main window.
window.title('Medieval')
window.geometry('1200x900')
window.attributes('-alpha', 1.0)

# Create top frame.
# --------------------------------------------------------------------------------
top_frame = tk.Frame(window, height=150)
top_frame.pack(fill=tk.BOTH)

hint_label = tk.Label(
    top_frame, text='Hint: Pirates are bad!', font=('Helvetica', '24'), bg='#181c21', fg='#c9b662',
    anchor=tk.NW, relief=tk.FLAT, pady=10, padx=10, bd=2,
)
hint_label.pack(fill=tk.BOTH)

# Create middle frame.
# --------------------------------------------------------------------------------
middle_frame = tk.Frame(window, height=600)
middle_frame.pack(fill=tk.BOTH)

# middle left frame
middle_left_frame = tk.Frame(middle_frame, height=600, width=120)
middle_left_frame.pack(fill=tk.BOTH, side=tk.LEFT)

# settings button
settings_btn_img = ImageTk.PhotoImage(
    Image.open(os.path.join('assets', 'settings-btn.png')).resize((BTN_WIDTH, BTN_HEIGHT))
)
settings_btn = tk.Button(
    middle_left_frame, image=settings_btn_img, bg='#c9b662', bd=5,
    highlightbackground='#000', activebackground='#7f6f28',
)
settings_btn.pack(fill=tk.BOTH)

# main canvas.
main_canvas = tk.Canvas(middle_frame, width=960, height=600, bg='#000', relief=tk.FLAT)
main_canvas.pack(fill=tk.BOTH, side=tk.LEFT)

main_canvas_image = ImageTk.PhotoImage(Image.open(os.path.join('assets', 'bazaar.jpg')))
main_canvas_image_id = main_canvas.create_image(0, 0, image=main_canvas_image, anchor=tk.NW)

# middle right frame.
middle_right_frame = tk.Frame(middle_frame, height=600, width=120)
middle_right_frame.pack(fill=tk.BOTH, side=tk.LEFT)

# map button.
map_btn_img = ImageTk.PhotoImage(
    Image.open(os.path.join('assets', 'map-btn.png')).resize((BTN_WIDTH, BTN_HEIGHT))
)
map_btn = tk.Button(
    middle_right_frame, image=map_btn_img, bg='#c9b662', bd=5,
    highlightbackground='#000', activebackground='#7f6f28',
)
map_btn.pack(fill=tk.BOTH)

# inventory button.
inventory_btn_img = ImageTk.PhotoImage(
    Image.open(os.path.join('assets', 'inventory-btn.png')).resize((BTN_WIDTH, BTN_HEIGHT))
)
inventory_btn = tk.Button(
    middle_right_frame, image=inventory_btn_img, bg='#c9b662', bd=5,
    highlightbackground='#000', activebackground='#7f6f28',
)
inventory_btn.pack(fill=tk.BOTH)


# Create bottom frame.
# --------------------------------------------------------------------------------
bottom_frame = tk.Frame(window, height=150)
bottom_frame.pack(fill=tk.BOTH, expand=True)

# bottom left frame
bottom_left_frame = tk.Frame(
    bottom_frame, width=950, height=150, bg='#c9b662'
)
bottom_left_frame.pack(fill=tk.BOTH, side=tk.LEFT)

# bottom canvas.
bottom_canvas = tk.Canvas(
    bottom_frame, width=250, height=150, bg='#c9b662', relief=tk.FLAT, highlightbackground='#000'
)
bottom_canvas.pack(fill=tk.BOTH, side=tk.LEFT)

bottom_canvas_image = ImageTk.PhotoImage(
    Image.open(os.path.join('assets', 'wizard.png')).resize((250, 250))
)
bottom_canvas_image_id = bottom_canvas.create_image(0, 0, image=bottom_canvas_image, anchor=tk.NW)

if __name__ == '__main__':
    window.mainloop()
