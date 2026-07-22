import pygame as pg

###############
### Set-ups ###
###############

class Game:
  def __init__(self):
    self.reset()

  def reset(self):
    self.grid = [([None] * 3) for _ in range(3)]
    self.gameEnd = False
    self.player = 1
    self.firstPieces = []
    self.secondPieces = []
    self.winner = None
    self.counter = 0
    self.stepsPerSecond = 3

game = Game()

pg.init()
screen = pg.display.set_mode((400, 400))
running = True
clock = pg.time.Clock()

### Screen Size Constants ###

WIDTH = 400
HEIGHT = 400
CELL_SIZE = WIDTH / 3
MID = CELL_SIZE / 2

### Winning Animation Constants ###

FLASH_DURATION = 90
FLASH_PERIOD = FLASH_DURATION / 3

### Colors and Fonts ###

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = pg.Color('dodgerblue4')
LIGHT_BLUE = pg.Color('deepskyblue2')
RED = pg.Color('orangered2')
LIGHT_RED = pg.Color('lightpink2')
PIECE_FONT = pg.font.SysFont(None, 60)
LABEL_FONT = pg.font.SysFont(None, 30)


##############
### Events ###
##############

def onMousePress(game, mouseX, mouseY):
  putPiece(game, mouseX, mouseY)
  if checkEnd(game, game.grid):
    game.gameEnd = True

def onKeyPress(game, key):
  if pg.key.name(key) == 'r':
    game.reset()

### Board Helpers ###

def getGrid(mouseX, mouseY):
  for i in range(3):
    start = CELL_SIZE * i
    end = CELL_SIZE * (i + 1)
    if start < mouseX < end:
      col = i
    if start < mouseY < end:
      row = i
  return row, col

def putPiece(game, mouseX, mouseY):
  if game.gameEnd:
    return
  row, col = getGrid(mouseX, mouseY)
  if game.grid[row][col] == None:
    if game.player == 1:
      game.grid[row][col] = 'O'
      if len(game.firstPieces) == 3:
        (deletedRow, deletedCol) = game.firstPieces.pop(0)
        game.grid[deletedRow][deletedCol] = None
      game.firstPieces.append((row, col))
      game.player = 2
    else:
      game.grid[row][col] = 'X'
      if len(game.secondPieces) == 3:
        (deletedRow, deletedCol) = game.secondPieces.pop(0)
        game.grid[deletedRow][deletedCol] = None
      game.secondPieces.append((row, col))
      game.player = 1


################
### Drawings ###
################

def drawGrid(screen):
  for i in range(1, 3):
    x = CELL_SIZE * i
    pg.draw.line(screen, BLACK, (x, 0), (x, HEIGHT), width=2)
    pg.draw.line(screen, BLACK, (0, x), (WIDTH, x), width=2)

def drawPieces(screen, game):
  if game.gameEnd and game.counter < FLASH_DURATION:
    if game.winner == 'O':
      drawFirstWinnerPieces(screen, game)
      drawSecondRegularPieces(screen, game)
    else:
      drawSecondWinnerPieces(screen, game)
      drawFirstRegularPieces(screen, game)
  else:
    drawFirstRegularPieces(screen, game)
    drawSecondRegularPieces(screen, game)

def drawEnd(screen, game):
  winner = getWinner(game)
  if winner == 'Player 1':
    color = LIGHT_BLUE
  else:
    color = LIGHT_RED
  display = pg.Rect(60, 150, 280, 100)
  pg.draw.rect(screen, color, display, width=0)
  pg.draw.rect(screen, BLACK, display, width=1)
  drawLabel(screen, 'Game Over', 200, 180, BLACK, LABEL_FONT)
  drawLabel(screen, f'{winner} won this round', 200, 220, BLACK, LABEL_FONT)

def drawLabel(screen, text, x, y, color, font):
  surface = font.render(text, True, color)
  rect = surface.get_rect(center=(x, y))
  screen.blit(surface, rect)

### Pieces Helpers ###

def drawFirstRegularPieces(screen, game):
  for row1, col1 in game.firstPieces:
    x = MID + CELL_SIZE * col1
    y = MID + CELL_SIZE * row1
    if (len(game.firstPieces) == 3 and (row1, col1) == game.firstPieces[0]
        and game.player == 1 and not game.gameEnd):
      color = LIGHT_BLUE
    else:
      color = BLUE
    drawLabel(screen, 'O', x, y, color, PIECE_FONT)

def drawSecondRegularPieces(screen, game):
  for row2, col2 in game.secondPieces:
    x = MID + CELL_SIZE * col2
    y = MID + CELL_SIZE * row2
    if (len(game.secondPieces) == 3 and (row2, col2) == game.secondPieces[0]
        and game.player == 2 and not game.gameEnd):
      color = LIGHT_RED
    else:
      color = RED
    drawLabel(screen, 'X', x, y, color, PIECE_FONT)

def drawFirstWinnerPieces(screen, game):
  if game.counter % FLASH_PERIOD < (FLASH_PERIOD / 2):
    color = LIGHT_BLUE
  else:
    color = BLUE
  for row1, col1 in game.firstPieces:
    x = MID + CELL_SIZE * col1
    y = MID + CELL_SIZE * row1
    drawLabel(screen, 'O', x, y, color, PIECE_FONT)

def drawSecondWinnerPieces(screen, game):
  if game.counter % FLASH_PERIOD < (FLASH_PERIOD / 2):
    color = LIGHT_RED
  else:
    color = RED
  for row2, col2 in game.secondPieces:
    x = MID + CELL_SIZE * col2
    y = MID + CELL_SIZE * row2
    drawLabel(screen, 'X', x, y, color, PIECE_FONT)

### End of Game Helpers ###

def checkEnd(game, grid):
  for row in grid:
    if row[0] != None and row[0] == row[1] == row[2]:
      game.winner = row[0]
      return True
  for col in range(len(grid[0])):
    if grid[0][col] != None and grid[0][col] == grid[1][col] == grid[2][col]:
      game.winner = grid[0][col]
      return True
  if grid[1][1] != None:
    if grid[0][0] == grid[1][1] == grid[2][2]:
      game.winner = grid[1][1]
      return True
    if grid[0][2] == grid[1][1] == grid[2][0]:
      game.winner = grid[1][1]
      return True
  return False

def getWinner(game):
  if game.winner == 'O':
    return 'Player 1'
  if game.winner == 'X':
    return 'Player 2'


#################
### Game Loop ###
#################

while running:
  for event in pg.event.get():
    if event.type == pg.MOUSEBUTTONDOWN:
      mouseX, mouseY = event.pos
      onMousePress(game, mouseX, mouseY)
    if event.type == pg.KEYDOWN:
      onKeyPress(game, event.key)
    if event.type == pg.QUIT:
      running = False

  if game.gameEnd:
    game.counter += 1

  screen.fill(WHITE)
  drawGrid(screen)
  drawPieces(screen, game)
  if game.gameEnd and game.counter >= FLASH_DURATION:
    drawEnd(screen, game)

  pg.display.flip()
  clock.tick(60)

pg.quit()