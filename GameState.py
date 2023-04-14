"""
GameState object represents one possible state of the board.
goalTest() returns True if the board is in a goal state
moveLeft(), moveRight(), moveUp(), moveDown() return the new GameState when the action is completed, or None if the move is invalid
getMoves() returns a list of the moves in case you want to iterate over them
"""
from collections import deque
class GameState:
  state = []
  blankPos = (0,0)
  def __init__(self, state):
    self.state = state
    for row in range(0, len(state)): #get blankPos 
      for item in range(0, len(state[row])):
        if state[row][item] == 0: self.blankPos = (row, item)
  def goalTest(self):
    tileOrder = deque(range(1, len(self.state)*len(self.state[0])))
    for row in self.state:
      for item in row:
        if item == 0: continue
        elif item == tileOrder[0]: tileOrder.popleft()
        else: return False
    return True
  def __move(self, direction): #private function for generalized move logic
    if self.blankPos[0] <= 0 or self.blankPos[0] >= len(self.state[0]) - 1: return None
    if self.blankPos[1] <= 0 or self.blankPos[1] >= len(self.state) - 1: return None #out of bounds checking
    newBlankPos = self.blankPos + direction
    newState = GameState(self.state)
    