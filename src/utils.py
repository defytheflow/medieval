import tkinter as tk
from typing import Tuple, Callable

from decorators import static_vars


@static_vars(pressed=False)
def lock_key_press(command: Callable):
    if not lock_key_press.pressed:
        lock_key_press.pressed = True
        command()
        lock_key_press.pressed = False


def create_photo_image(path: str,
                       size: Tuple[int, int] = None) -> tk.PhotoImage:
    from PIL import Image, ImageTk
    image = Image.open(path)
    if size:
        image = image.resize(size)
    return ImageTk.PhotoImage(image)


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
