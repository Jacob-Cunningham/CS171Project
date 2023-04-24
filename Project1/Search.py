from GameState import GameState
from queue import PriorityQueue
class Search:
    startState = None
    h = lambda x : 0
    
    def __init__(self, startState, h):
        self.startState = startState
        self.h = h
    
    def search(self, display = False):
        frontier = PriorityQueue()
        frontier.put((self.h(self.startState), self.startState))
        checkedStates = set()
        inFrontier = set()
        expanded = 0;
        numInQueue = 1;

        while not frontier.empty():
            currentNode = frontier.get()[1] #choose a leaf node and remove it from the frontier
            numInQueue -= 1;
            if display:
                print("Expanding best node with g(n) =", currentNode.depth, "and h(n) =", self.h(currentNode))
                print(currentNode)
                input()
            if currentNode.goalTest(): #if leaf node contains a goal state then return the solution
                return expanded, numInQueue, currentNode.depth, 
            checkedStates.add(currentNode) #add the node to the explored set
            for state in currentNode.getMoves(): #expand the chosen node
                expanded += 1;
                if state not in checkedStates and state not in inFrontier: #only if not in the frontier or explored set
                    frontier.put((self.h(state) + state.depth, state)) #adding the resulting nodes to the frontier 
                    inFrontier.add(state)
                    numInQueue += 1;
        return None #if frontier empty then return failure