import tkinter as tk

from .behavior import KeyboardBoundWidget, MouseBoundWidget, BilingualWidget
from .utils import get_all_widget_children


def notify_keyboardbound_widgets(root: tk.Tk):
    for widget in get_all_widget_children(root):
        if isinstance(widget, KeyboardBoundWidget):
            widget.init_keyboard_binds()


def notify_mousebound_widgets(root: tk.Tk):
    for widget in get_all_widget_children(root):
        if isinstance(widget, MouseBoundWidget):
            widget.init_mouse_binds()


def notify_bilingual_widgets(root: tk.Tk, lang: str) -> None:
    for widget in get_all_widget_children(root):
        if isinstance(widget, BilingualWidget):
            widget.switch_lang(lang)
