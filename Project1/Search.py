from GameState import GameState
from queue import PriorityQueue
class Search:
    startState = None
    h = lambda x : 0
    
    def __init__(self, startState, h):
        self.startState = startState
        self.h = h
    
    def search(self):
        frontier = PriorityQueue()
        frontier.put((self.h(self.startState), self.startState))
        checkedStates = set()
        inFrontier = set()

        while not frontier.empty():
            currentNode = frontier.get()[1] #choose a leaf node and remove it from the frontier
            if currentNode.goalTest(): #if leaf node contains a goal state then return the solution
                return currentNode
            checkedStates.add(currentNode) #add the node to the explored set
            for state in currentNode.getMoves(): #expand the chosen node
                if state not in checkedStates and state not in inFrontier: #only if not in the frontier or explored set
                    frontier.put((self.h(state) + state.depth, state)) #adding the resulting nodes to the frontier 
                    inFrontier.add(state)
        return None #if frontier empty then return failure