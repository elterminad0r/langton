import random as random_

blocks = [-1, 1, -1]
DIRECTIONS = [(0, 1),
              (1, 0),
              (0, -1),
              (-1, 0)]
BLOCK_SIZE = 2

DEFAULT_SPEED = 64
DEFAULT_PATS = ["LR", "RLL", "RLR", "LLRR", "LRRRRRLLR", "LLRRRLRLRLLR", "RRLLLRLLLRRR"]

chrand = True

lr_dict = {"R": -1, "L": 1,
           "0": -1, "1": 1}

def blocks_from_lr(lr):
    return [lr_dict[c] for c in lr]

def blocks_from_int(i):
    return blocks_from_lr(bin(i)[2:])

def setup():
    global ant_field, ant_dir, x, y, width_, height_, speed, blocks
    size(1280, 720)
    background(0)
    noStroke()
    colorMode(HSB, 255, 255, 255)

    if chrand:
        blocks = blocks_from_lr(random_.choice(DEFAULT_PATS))

    width_ = width // BLOCK_SIZE
    height_ = height // BLOCK_SIZE
    ant_field = [[0 for _ in xrange(height_)] for _ in xrange(width_)]
    x, y = width_ // 2, height_ // 2
    ant_dir = 0
    speed = DEFAULT_SPEED

def advance_ant():
    global ant_dir, x, y
    ant_field[x][y] = (ant_field[x][y] + 1) % len(blocks)
    ant_dir = (ant_dir + blocks[ant_field[x][y]]) % len(DIRECTIONS)
    chx, chy = DIRECTIONS[ant_dir]
    fill(map(ant_field[x][y], 0, len(blocks), 0, 255), 255, 255)
    rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    x = (x + chx) % width_
    y = (y + chy) % height_

def draw():
    for _ in xrange(speed):
        advance_ant()

def keyPressed():
    global speed, blocks, chrand
    if keyCode == UP:
        speed *= 2
    elif keyCode == DOWN:
        speed //= 2
    elif 0 <= keyCode - ord("1") < len(DEFAULT_PATS):
        chrand = False
        blocks = blocks_from_lr(DEFAULT_PATS[keyCode - ord("1")])
        setup()
    elif keyCode == ord(" "):
        chrand = True
        setup()
    print(speed)
