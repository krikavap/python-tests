
# Code for chapter 02 - Exceptions in Python

# without bug + relative path implementation

import pygame
from pygame import image, Rect, Surface


TILE_POSITIONS = [
    ('#', 0, 0),  # wall
    (' ', 0, 1),  # floor
    ('x', 1, 1),  # exit
    ('.', 2, 0),  # dot
    ('*', 3, 0),  # player
]
SIZE = 32

relpath = 'MazeRun Game/maze_run/'
relpath_images = 'MazeRun Game/maze_run/images/'

def get_tile_rect(x, y):
    """Converts tile indices to a pygame.Rect"""
    return Rect(x * SIZE, y * SIZE, SIZE, SIZE)


def load_tiles():
    """
    Load tiles from an image file into a dictionary.
    Returns a tuple of (image, tile_dict)
    """
   
    tile_img = image.load(relpath_images+'tiles.xpm')

    tiles = {}
    for symbol, x, y in TILE_POSITIONS:
        tiles[symbol] = get_tile_rect(x, y)
    return tile_img, tiles


if __name__ == '__main__':
    tile_img, tiles = load_tiles()
    m = Surface((96, 32))
    m.blit(tile_img, get_tile_rect(0, 0), tiles['#'])
    m.blit(tile_img, get_tile_rect(1, 0), tiles[' '])
    m.blit(tile_img, get_tile_rect(2, 0), tiles['*'])
    image.save(m, relpath+'tile_combo.png')


