' Window Geometry related functions and types. '

from collections import namedtuple


Position = namedtuple('Position', ('x', 'y'))
Dimension = namedtuple('Dimension', ('width', 'height'))


class Oriented:

    def __init__(self, direction):
        self._dir = direction

    @property
    def direction(self):
        return self._dir

    @direction.setter
    def direction(self, new_dir):
        if new_dir.lower() not in ('north', 'south', 'west', 'east'):
            raise ValueError(f"Invalid direction '{new_direction}'")
        self._dir = new_dir


class Movable:

    def __init__(self, speed):
        self._speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        self._speed = new_speed


class Positionable:

    def __init__(self, position):
        self._pos = Position(*position)

    @property
    def position(self):
        return self._pos

    @position.setter
    def position(self, new_pos):
        self._pos = Position(*new_pos)

    @property
    def x(self):
        return self._pos.x

    @property
    def y(self):
        return self._pos.y


class Rectangular:

    def __init__(self, dimension):
        self._dim = Dimension(*dimension)

    @property
    def dimension(self):
        return self._dim

    @property
    def width(self):
        return self._dim.width

    @property
    def height(self):
        return self._dim.height


def get_center_position(dim1, dim2):
    '''
        >>> get_center_position(Dimension(100, 100), Dimension(30, 30))
        Position(x=35, y=35)
    '''
    return Position(dim1.width // 2 - dim2.width // 2,
                    dim1.height // 2 - dim2.height // 2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
