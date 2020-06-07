TILE = 0
WORLD_WIDTH = 20
WORLD_HEIGHT = 20

CAMERA = 2
CAMERA_WIDTH = 5
CAMERA_HEIGHT = 5

PLAYER = 1
PLAYER_X = WORLD_WIDTH // 2
PLAYER_Y = WORLD_HEIGHT // 2


def create_matrix(width, height, val):
    return [[val for col in range(width)] for row in range(height)]


class World:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = create_matrix(width, height, TILE)

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
        string = [f'{str(row)}\n' for row in self.matrix]
        return ''.join(string)


class Player:

    def __init__(self, x, y, world):
        self.x = x
        self.y = y
        self.world = world

    def plot(self, num):
        self.world[self.y][self.x] = num


class Camera:

    def __init__(self, width, height, player, world):
        self.width = width
        self.height = height
        self.player = player
        self.world = world

        self.x = self.player.x - self.width // 2
        self.y = self.player.y - self.height // 2

        # Can I create a matrix of width, height around player.x in world?
        if not self.fits_on_x():
            print('Camera does not fit on x.')

        if not self.fits_on_y():
            print('Camera does not fit on y.')

    def fits_on_x(self):
        return (0 <= self.player.x - self.width // 2 and
                self.player.x + self.width // 2 <= self.world.width)

    def fits_on_y(self):
        return (0 <= self.player.y - self.height // 2 and
                self.player.y + self.height // 2 <= self.world.height)

    def plot(self, num):
        for x in range(self.x, self.x + self.width):
            for y in range(self.y, self.y + self.height):
                self.world[y][x] = num


def main():
    world = World(WORLD_WIDTH, WORLD_HEIGHT)
    player = Player(PLAYER_X, PLAYER_Y, world)
    camera = Camera(CAMERA_WIDTH, CAMERA_HEIGHT, player, world)

    camera.plot(CAMERA)
    player.plot(PLAYER)
    print(world)


if __name__ == '__main__':
    main()
