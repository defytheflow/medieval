#!/usr/bin/python3

import os


WORLD_TILE = 0
WORLD_WIDTH = 20
WORLD_HEIGHT = 20

PLAYER_TILE = 1
PLAYER_WIDTH = 1
PLAYER_HEIGHT = 1
PLAYER_X = WORLD_WIDTH // 2
PLAYER_Y = WORLD_HEIGHT // 2

CAMERA_TILE = 2
CAMERA_WIDTH = 5
CAMERA_HEIGHT = 5
CAMERA_X = PLAYER_X - CAMERA_WIDTH // 2
CAMERA_Y = PLAYER_Y - CAMERA_HEIGHT // 2

NORTH, SOUTH, WEST, EAST = range(4)

QUIT = 'q'


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


class Matrix:

    def __init__(self, width, height, tile):
        self.rows = [[tile] * width for x in range(height)]
        self.width = width
        self.height = height
        self.tile = tile

    def __getitem__(self, key):
        return self.rows[key]

    def __setitem__(self, key, val):
        self.rows[key] = val

    def __len__(self):
        return len(self.rows)

    def __iter__(self):
        return self.rows

    def __str__(self):
        return '\n'.join([' '.join([str(item) for item in row]) for row in self.rows]) + '\n'


class World(Matrix):

    def __init__(self, width, height, tile):
        super().__init__(width, height, tile)

    def plot(self, matrix):
        for col in range(matrix.x, matrix.x + matrix.width):
            for row in range(matrix.y, matrix.y + matrix.height):
                self[row][col] = matrix.tile

    def erase(self, matrix):
        for col in range(matrix.x, matrix.x + matrix.width):
            for row in range(matrix.y, matrix.y + matrix.height):
                self[row][col] = self.tile


class WorldMatrix(Matrix):

    def __init__(self, x, y, world, width, height, tile):
        super().__init__(width, height, tile)
        self.world = world
        self.x, self.y = x, y

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y}, width={self.width}, height={self.height})'


class Player(WorldMatrix):

    def __init__(self, x, y, world, width, height, tile):
        super().__init__(x, y, world, width, height, tile)
        self.world.plot(self)

    def move(self, direction):
        self.world.erase(self)

        if direction == NORTH:
            self.y -= 1
        elif direction == SOUTH:
            self.y += 1
        elif direction == WEST:
            self.x -= 1
        elif direction == EAST:
            self.x += 1

        self.world.plot(self)


class Camera(WorldMatrix):

    def __init__(self, player, x, y, world, width, height, tile):
        self.player = player
        super().__init__(x, y, world, width, height, tile)
        self.world.plot(self)

    def move(self, direction):
        self.player.move(direction)
        self.world.erase(self)

        if direction == NORTH:
            self.y -= 1
        elif direction == SOUTH:
            self.y += 1
        elif direction == WEST:
            self.x -= 1
        elif direction == EAST:
            self.x += 1

        self.world.plot(self)
        self.world.plot(self.player)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        if not self.fits_on_x():
            raise ValueError('Camera does not fit on x.')
        self._x = val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        if not self.fits_on_y():
            raise ValueError('Camera does not fit on y.')
        self._y = val

    def fits_on_x(self):
        return (0 <= self.player.x - self.width // 2 and
                self.player.x + self.width // 2 <= self.world.width)

    def fits_on_y(self):
        return (0 <= self.player.y - self.height // 2 and
                self.player.y + self.height // 2 <= self.world.height)


def mainloop():

    world = World(WORLD_WIDTH, WORLD_HEIGHT, WORLD_TILE)
    player = Player(PLAYER_X, PLAYER_Y, world, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_TILE)
    camera = Camera(player, CAMERA_X, CAMERA_Y, world, CAMERA_WIDTH, CAMERA_HEIGHT, CAMERA_TILE)

    os.system('clear')
    print(world)

    while True:
        ch = getch()

        if ch == QUIT:
            break

        if ch == 'w':
            camera.move(NORTH)
        elif ch == 's':
            camera.move(SOUTH)
        elif ch == 'a':
            camera.move(WEST)
        elif ch == 'd':
            camera.move(EAST)

        os.system('clear')
        print(world)


if __name__ == '__main__':
    mainloop()
