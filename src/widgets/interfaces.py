import abc


class StyledWidget(abc.ABC):

    @abc.abstractmethod
    def init_style(self):
        pass


class KeyBoundWidget(abc.ABC):

    @abc.abstractmethod
    def init_key_binds(self):
        pass


class MouseBoundWidget(abc.ABC):

    @abc.abstractmethod
    def init_mouse_binds(self):
        pass
