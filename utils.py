import tkinter as tk
from typing import List

from PIL import Image, ImageTk


def create_photo_image(path: str, size: tuple = None) -> tk.PhotoImage:
    """
        Creates a new PhotoImage object.
    """
    image = Image.open(path)

    if size:
        image = image.resize(size)

    return ImageTk.PhotoImage(image)


def get_all_widget_children(parent: tk.Widget) -> List[tk.Widget]:
    """
        Recursively collects all parent widget children.
    """
    children = parent.winfo_children()

    for child in children:
        children.extend(get_all_widget_children(child))

    return set(children)
