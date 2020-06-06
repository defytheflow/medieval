from geometry import Rectangular


class GameMap(Rectangular):

    def __init__(self, dimension, canvas):
        super().__init__(dimension)
        self.canvas = canvas
        self.register = {}

    def __repr__(self):
        return f'{self.__class__.__name__}({self.dimension})'

    def draw(self):
        pass

    def redraw(self):
        pass

    def place_rectangle(self, pos, dim, fill):
        self.register[pos] = {
            'rectangle': {
                'dim': dim,
                'fill': fill,
            }
        }
