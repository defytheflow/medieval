' Window Geometry related functions and types. '

from collections import namedtuple


Position = namedtuple('Position', ('x', 'y'))
Size = namedtuple('Size', ('width', 'height'))


def get_center_position(size1, size2):
    '''
        >>> get_center_position(Size(100, 100), Size(30, 30))
        Position(x=35, y=35)
    '''
    return Position(size1.width // 2 - size2.width // 2,
                    size1.height // 2 - size2.height // 2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
