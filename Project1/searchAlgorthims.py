
import numpy as np
from queue import PriorityQueue
from TreeNodeClasses import Node, Tree
#PLEASE ADD YIUR FILE HERE

#READ!!!!!! The "__move" is the fucntion jsuggles wrote in discord, the actions the nodes can take. 
            #please look at the code and see what edits it might need to work with your code



# "startState"/"goalState" assumed to be a matrix represented as a numpy array.
def uniformCostSearch(startState, goalState):
    #WRITE THE CRAP:

    # useing priority queue
    frontier = PriorityQueue()
    startNode = Node(startState)
    #Uniform Cost Search is just A* with h(n) hardcoded to equal zero
    frontier.put((0, startNode)) 
    checkedStates = set()

    while not frontier.empty():
        #gets highest prio (lowest cost) from queue, the [1] will then set startState (2nd parameter) to currentNode
        currentNode = frontier.get()[1] 
       
        #if goal state is reached
        if currentNode.state == goalState:
            #  DO THE EXPANDING INTERFACE  HERE?!
            while currentNode.parent is not None: #while not root node
                __move.append(currentNode.operator) #Do the moves/actions
                currentNode = currentNode.parent #go up a level
            return __move[::-1]  #-1 makes sure the operator states are in order (from initial state to goal state)
    
        checkedStates.add(currentNode.state) #current node was checked so add to checkedStates

        for continuedNode in currentNode.expand():

            #only add the states that have not been seen/checked before to the queue
            if continuedNode.state not in checkedStates:
                #frontier.put((continuedNode.edgeCost, continuedNode)) IDK if we have an edge cost
                frontier.put((0, continuedNode))

    
    return #goal? #do the expanding interface here????




def MisplacedTile(matrix):
    #write the crap
    #do the expanding interface here
    return #goal?

def EuclideanDistance(matrix):
    #write the crap
    #do the expanding interface here
    return #goal?


