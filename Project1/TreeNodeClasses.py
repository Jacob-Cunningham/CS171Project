#PLEASE ADD WHATEVER YOU THINK IS NESSESARY OR HELPFUL 

class Tree:
    def TreeConstructor(self, root):
        self.root = root
    
    #what else could this class need????? IDK

class Node:
    def NodeConstructor(self, state, parent=None, operator=None, edgeCost=0):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.edgeCost=edgeCost #May change???? IDK what the "costs" are 