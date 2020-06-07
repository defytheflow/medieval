#!/usr/bin/python3

import os


WORLD_TILE = 0
WORLD_WIDTH = 20
WORLD_HEIGHT = 20

PLAYER_TILE = 1
PLAYER_X = WORLD_WIDTH // 2
PLAYER_Y = WORLD_HEIGHT // 2

CAMERA_TILE = 2
CAMERA_WIDTH = 5
CAMERA_HEIGHT = 5

NORTH, SOUTH, WEST, EAST = range(4)

QUIT = 'q'


class _GetchUnix:

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

getch = _GetchUnix()


def create_matrix(width, height, val):
    return [[val for col in range(width)] for row in range(height)]


class Movable:

    def move(self, direction):
        self.erase()
        if direction == NORTH:
            self.y -= 1
        elif direction == SOUTH:
            self.y += 1
        elif direction == WEST:
            self.x -= 1
        elif direction == EAST:
            self.x += 1
        self.plot()


class World:

    def __init__(self, width, height, tile):
        self.width = width
        self.height = height
        self.tile = tile
        self.matrix = create_matrix(width, height, tile)

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, key):
        return self.matrix[key]

    def __setitem__(self, key, value):
        self.matrix[key] = value

    def __delitem__(self, key):
        del self.matrix[key]

    def __iter__(self):
        return self.matrix

    def __str__(self):
        return '|\n'.join([''.join([f'|{col}' for col in row]) for row in self.matrix]) + '|'


class Player(Movable):

    def __init__(self, x, y, world, tile):
        self.x = x
        self.y = y
        self.world = world
        self.tile = tile
        self.plot()

    def plot(self):
        self.world[self.y][self.x] = self.tile

    def erase(self):
        self.world[self.y][self.x] = self.world.tile


class Camera(Movable):

    def __init__(self, width, height, player, world, tile):
        self.width = width
        self.height = height
        self.player = player
        self.world = world
        self.tile = tile

        # Can I create a matrix of width, height around player.x in world?
        if not self.fits_on_x():
            print('Camera does not fit on x.')

        if not self.fits_on_y():
            print('Camera does not fit on y.')

        # Plot around player.
        self.x = self.player.x - self.width // 2
        self.y = self.player.y - self.height // 2

        self.plot()

    def fits_on_x(self):
        return (0 <= self.player.x - self.width // 2 and
                self.player.x + self.width // 2 <= self.world.width)

    def fits_on_y(self):
        return (0 <= self.player.y - self.height // 2 and
                self.player.y + self.height // 2 <= self.world.height)

    def plot(self):
        for x in range(self.x, self.x + self.width):
            for y in range(self.y, self.y + self.height):
                self.world[y][x] = self.tile
        self.player.plot()

    def erase(self):
        for x in range(self.x, self.x + self.width):
            for y in range(self.y, self.y + self.height):
                self.world[y][x] = self.world.tile


def main():

    world = World(WORLD_WIDTH, WORLD_HEIGHT, WORLD_TILE)
    player = Player(PLAYER_X, PLAYER_Y, world, PLAYER_TILE)
    camera = Camera(CAMERA_WIDTH, CAMERA_HEIGHT, player, world, CAMERA_TILE)

    os.system('clear')
    print(world)

    while True:
        ch = getch()

        if ch == QUIT:
            break

        if ch == 'w':
            player.move(NORTH)
        elif ch == 's':
            player.move(SOUTH)
        elif ch == 'a':
            player.move(WEST)
        elif ch == 'd':
            player.move(EAST)

        os.system('clear')
        print(world)


if __name__ == '__main__':
    main()
