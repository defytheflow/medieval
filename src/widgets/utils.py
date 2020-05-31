import tkinter as tk

from typing import Set


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
