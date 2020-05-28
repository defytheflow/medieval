import os
import tkinter as tk
from typing import List

import simpleaudio as sa
from PIL import Image, ImageTk

import config
from widgets import BilingualWidget, BilingualTooltip


def create_photo_image(path, size=None) -> tk.PhotoImage:
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


def set_current_frame(current: tk.Frame, previous: tk.Frame):
    previous.forget()
    current.pack(fill=tk.BOTH, expand=True)


def notify_bilingual_children(parent, lang):
    for child in get_all_widget_children(parent):
        if isinstance(child, BilingualWidget):
            child.switch_lang(lang)


def play_sound(sound_file):
    wave_obj = sa.WaveObject.from_wave_file(sound_file)
    play_obj = wave_obj.play()


def bind_image(widget, image_file, size):
    if not isinstance(widget, tk.Widget):
        raise TypeError('widget parameter must be a tk.Widget instance')

    widget.image = create_photo_image(image_file, size)
    widget.configure(image=widget.image)


def bind_sound(widget, sound_file):
    if not isinstance(widget, tk.Widget):
        raise TypeError('widget parameter must be a tk.Widget instance')

    widget.bind('<Button-1>', lambda e: play_sound(sound_file))
