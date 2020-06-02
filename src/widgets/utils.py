import tkinter as tk
from typing import Set, Tuple

from utils import (
    play_sound,
    create_photo_image,
)


def get_all_widget_children(parent: tk.Misc) -> Set[tk.Widget]:
    """
        Recursively collects all parent widget's children.
    """
    children = parent.winfo_children()
    for child in children:
        children.extend(get_all_widget_children(child))
    return set(children)


def get_widget_parent(widget: tk.Widget) -> tk.Widget:
    parent_name = widget.winfo_parent()
    return widget._nametowidget(parent_name)


def bind_image_to_widget(widget: tk.Widget,
                         image_file: str,
                         size: Tuple[int, int]) -> None:
    widget.image = create_photo_image(image_file, size)
    widget.configure(image=widget.image)


def bind_sound_to_widget(widget: tk.Widget, event: str, sound_file: str) -> None:
    widget.bind(event, lambda e: play_sound(sound_file))
