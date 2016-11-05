
from action import Action
    
class Plan:
    def __init__(self):
        self.actions = []

    def pushBack(self,action):
        self.actions.append(action)

    def pushFront(self,action):
        self.actions.insert(0,action)

    def getActions(self):
        return self.actions


    def display(self):
        for a in self.actions:
            a.display()
            print ",",

        print ""
