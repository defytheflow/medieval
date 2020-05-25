#!/usr/bin/python3

from PIL import Image, ImageDraw


WIDTH = 1080
HEIGHT = 700

SIDE = 20

image = Image.new('RGB', (1080, 700), color=(255, 255, 255))
draw = ImageDraw.Draw(image)

# ROCK = (190, 190, 190)
# GRASS = (0, 255, 0)
# WATER = (0, 0, 255)

ROCK = Image.open('rock.jpeg').resize((SIDE, SIDE))
WATER = Image.open('water.jpeg').resize((SIDE, SIDE))
GRASS = Image.open('grass.png').resize((SIDE, SIDE))

WATER_WIDTH = 20
WATER_HEIGHT = 14

WATER_BEGIN_X = (WIDTH - WATER_WIDTH * SIDE) // 2 // SIDE - 1
WATER_END_X = WATER_BEGIN_X + WATER_WIDTH - 1

WATER_BEGIN_Y = (HEIGHT - WATER_HEIGHT * SIDE) // 2 // SIDE - 1
WATER_END_Y = WATER_BEGIN_Y + WATER_HEIGHT - 1


def generate_map1():
    x, y = 0, 0

    # LINE OF ROCKS
    for i in range(WIDTH // SIDE):
        image.paste(ROCK, (x, y))
        # draw.rectangle([x, y, x + SIDE, y + SIDE], fill=ROCK)
        x += SIDE
    y += SIDE

    # MIDDLE GRASS
    for i in range(HEIGHT // SIDE - 2):
        # FIRST ROCK
        x = 0
        image.paste(ROCK, (x, y))
        # draw.rectangle([x, y, x + SIDE, y + SIDE], fill=ROCK)
        x += SIDE

        # GRASS ROW
        for j in range(WIDTH // SIDE - 2):
            if WATER_BEGIN_X < j < WATER_END_X and WATER_BEGIN_Y < i < WATER_END_Y:
                image.paste(WATER, (x, y))
                # draw.rectangle([x, y, x + SIDE, y + SIDE], fill=WATER)
            else:
                image.paste(GRASS, (x, y))
                # draw.rectangle([x, y, x + SIDE, y + SIDE], fill=GRASS)
            x += SIDE

        # LAST ROCK
        image.paste(ROCK, (x, y))
        # draw.rectangle([x, y, x + SIDE, y + SIDE], fill=ROCK)
        y += SIDE

    # LINE OF ROCKS
    x = 0
    for i in range(WIDTH // SIDE):
        image.paste(ROCK, (x, y))
        # draw.rectangle([x, y, x + SIDE, y + SIDE], fill=ROCK)
        x += SIDE
    y += SIDE


generate_map1()
# y = 0
# for col in range(HEIGHT // SQUARE_SIDE):
#     x = 0
#     for row in range(WIDTH // SQUARE_SIDE):
#         draw.rectangle([x, y, x + SQUARE_SIDE, y + SQUARE_SIDE],
#                        fill=random.choice(COLORS))
#         x += SQUARE_SIDE
#     y += SQUARE_SIDE

image.save('test.jpg')
