import tkinter as tk

from PIL import Image, ImageTk


def create_photo_image(path: str, size: tuple=None) -> tk.PhotoImage:
    """ Creates a new PhotoImage object. """
    image = Image.open(path)
    if size:
        image = image.resize(size)
    return ImageTk.PhotoImage(image)


def get_all_children(parent):
    lst = []

    def recurse(parent):
        children = parent.winfo_children()
        if not children:
            return
        lst.extend(children)
        for child in children:
            lst.extend(get_all_children(child))

    recurse(parent)
    return lst
