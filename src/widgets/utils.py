from utils import (
    play_sound,
    create_photo_image,
)


def get_all_widget_children(parent):
    ' Recursively collects all parent widget children.'
    children = parent.winfo_children()
    for child in children:
        children.extend(get_all_widget_children(child))
    return set(children)


def get_widget_parent(widget):
    parent_name = widget.winfo_parent()
    return widget._nametowidget(parent_name)


def notify_widget_class(root, widget_cls, method_name, args=None):
    for widget in get_all_widget_children(root) | {root}:
        if isinstance(widget, widget_cls):
            method = getattr(widget, method_name)
            method(args) if args else method()


def bind_image_to_widget(widget, image_file, size):
    widget.image = create_photo_image(image_file, size)
    widget.configure(image=widget.image)


def bind_sound_to_widget(widget, event, sound_file):
    widget.bind(event, lambda e: play_sound(sound_file))
