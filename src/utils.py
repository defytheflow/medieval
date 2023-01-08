import platform
import tkinter as tk
from typing import Callable, Tuple


def create_photo_image(path: str,
                       size: Tuple[int, int] = None) -> tk.PhotoImage:
    from PIL import Image, ImageTk
    image = Image.open(path)
    if size:
        image = image.resize(size)
    return ImageTk.PhotoImage(image)


def play_sound(sound_file: str) -> None:
    if not platform.machine().endswith('arm'):
        import simpleaudio as sa
        wave_obj = sa.WaveObject.from_wave_file(sound_file)
        wave_obj.play()
