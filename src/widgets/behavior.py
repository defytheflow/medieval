import abc


class KeyboardBoundWidget(abc.ABC):

    @abc.abstractmethod
    def init_keyboard_binds(self) -> None:
        pass


class MouseBoundWidget(abc.ABC):

    @abc.abstractmethod
    def init_mouse_binds(self) -> None:
        pass


class BilingualWidget(abc.ABC):

    @abc.abstractmethod
    def switch_lang(self, lang: str) -> None:
        pass
