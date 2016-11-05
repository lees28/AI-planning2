# MoveToFloor(b,y) action

from action import Action
from obj import Object
from on import On
from clear import Clear

class MoveToFloor(Action):
    def __init__(self,what,fromObj,floorObj):
        # arguments (b,y)
        self.args = []

        # preconditions
        self.pre = []

        # add list
        self.add = []

        # delete list
        self.delete = []

        self.name = "MoveToFloor"

        # the first argument (what is being moved); b in MoveToFloor(b,y)
        self.what = what

        # the second argument (from where is it being moved); y in MoveToFloor(b,y)
        self.fromObj = fromObj

        # the floor object
        self.floorObj = floorObj

        self.pre.append(On(what,fromObj))
        self.pre.append(Clear(what))

        self.add.append(On(what,floorObj))
        self.add.append(Clear(fromObj))

        self.delete.append(On(what,fromObj))
        
    def display(self):
        print "MoveToFloor(",self.what.getName(),",",self.fromObj.getName(),")",
