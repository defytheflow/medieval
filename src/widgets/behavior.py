import abc


class StyledWidget(abc.ABC):

    @abc.abstractmethod
    def init_style(self):
        pass


class KeyboardBoundWidget(abc.ABC):

    @abc.abstractmethod
    def init_keyboard_binds(self):
        pass


class MouseBoundWidget(abc.ABC):

    @abc.abstractmethod
    def init_mouse_binds(self):
        pass


class BilingualWidget(abc.ABC):

    @abc.abstractmethod
    def switch_lang(self, lang):
        pass


