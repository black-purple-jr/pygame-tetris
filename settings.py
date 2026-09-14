import pygame

# Game size
COLUMNS = 10
ROWS = 20
CELL_SIZE = 33
GAME_WIDTH, GAME_HEIGHT = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE

# Side bar size
SIDEBAR_WIDTH = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION

# Window
PADDING = 20
WINDOW_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH + PADDING * 3
WINDOW_HEIGHT = GAME_HEIGHT + PADDING * 2

# Game behaviour
UPDATE_START_SPEED = 800
MOVE_WAIT_TIME = 200
ROTATE_WAIT_TIME = 200
BLOCK_OFFSET = pygame.Vector2(COLUMNS // 2, -1)

# Colors
YELLOW = '#F1E60D'
RED = '#E51B20'
BLUE = '#204B9B'
GREEN = '#65B32E'
PURPLE = '#7B217F'
CYAN = '#6CC6D9'
ORANGE = '#F07E13'
GRAY = '#1C1C1C'
LINE_COLOR = '#FFFFFF'

# Shapes
TETROMINOS = {
  'T': { 'shape': [(0, 0), (-1, 0), (1, 0), (0, -1)], 'color': PURPLE },
  'O': { 'shape': [(0, 0), (0, -1), (1, 0), (1, -1)], 'color': YELLOW },
  'J': { 'shape': [(0, 0), (0, -1), (0, 1), (-1, 1)], 'color': BLUE },
  'L': { 'shape': [(0, 0), (0, -1), (0, 1), (1, 1)], 'color': ORANGE },
  'I': { 'shape': [(0, 0), (0, -1), (0, 1), (1, 1)], 'color': CYAN },
  'S': { 'shape': [(0, 0), (-1, 0), (0, -1), (1, -1)], 'color': GREEN },
  'Z': { 'shape': [(0, 0), (1, 0), (0, -1), (-1, -1)], 'color': RED },
}

SCORE_DATA = { 1: 40, 2: 100, 3: 300, 4: 1200 }