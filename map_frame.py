from widgets import TitleFrame


class MapFrame(TitleFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            text_dict={
                'eng': 'Map',
                'rus': 'Карта',
            },
            **kwargs
        )
