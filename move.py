# Move(x,y,z) action

from action import Action
from obj import Object
from on import On
from clear import Clear

class Move(Action):
    def __init__(self,what,fromObj,toObj):
        # arguments (x,y,z)
        self.args = []

        # preconditions
        self.pre = []

        # add list
        self.add = []

        # delete list
        self.delete = []

        self.name = "Move"

        # the first argument (what is being moved); x in Move(x,y,z)
        self.what = what

        # the second argument (from where is it being moved); y in Move(x,y,z)
        self.fromObj = fromObj

        # the third argument (where is it being moved to); z in Move(x,y,z)
        self.toObj = toObj

        self.pre.append(On(what,fromObj))
        self.pre.append(Clear(what))
        self.pre.append(Clear(toObj))

        self.add.append(On(what,toObj))
        self.add.append(Clear(fromObj))

        self.delete.append(On(what,fromObj))
        self.delete.append(Clear(toObj))
        
    def display(self):
        print "Move(",self.what.getName(),",",self.fromObj.getName(),",",self.toObj.getName(),")",
