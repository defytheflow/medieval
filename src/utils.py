import tkinter as tk

from typing import Tuple, Set


def create_photo_image(path: str,
                       size: Tuple[int, int] = None) -> tk.PhotoImage:
    from PIL import Image, ImageTk
    image = Image.open(path)
    if size:
        image = image.resize(size)
    return ImageTk.PhotoImage(image)


def get_all_widget_children(parent: tk.Misc) -> Set[tk.Widget]:
    """
        Recursively collects all parent widget's children.
    """
    children = parent.winfo_children()
    for child in children:
        children.extend(get_all_widget_children(child))
    return set(children)

def play_sound(sound_file: str) -> None:
    import simpleaudio as sa
    wave_obj = sa.WaveObject.from_wave_file(sound_file)
    play_obj = wave_obj.play()


def bind_image(widget: tk.Widget,
               image_file: str,
               size: Tuple[int, int]) -> None:
    widget.image = create_photo_image(image_file, size)
    widget.configure(image=widget.image)


def bind_sound(widget: tk.Widget, event: str, sound_file: str) -> None:
    widget.bind(event, lambda e: play_sound(sound_file))
