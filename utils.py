import tkinter as tk

from PIL import Image, ImageTk


def create_photo_image(path: str, size: tuple=None) -> tk.PhotoImage:
    """ Creates a new PhotoImage object. """
    image = Image.open(path)
    if size:
        image = image.resize(size)
    return ImageTk.PhotoImage(image)
