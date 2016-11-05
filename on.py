# On(x,y) predicate

from predicate import Predicate
from obj import Object

class On(Predicate):
    def __init__(self, what, onWhat):
        # On(x,y) : On(what, onWhat)
        # meaning "what" is On "onWhat"
        self.what = what
        self.onWhat = onWhat
        self.name = "On"
        self.args = []
        self.args.append(self.what)
        self.args.append(self.onWhat)

    def setWhat(self,o):
        # set the first argument of On(x,y)
        self.what = o
        self.args[0] = o

    def getWhat(self):
        # return the first argument (object) of On(x,y)
        return self.what

    def setOnWhat(self,o):
        # set the second argument of On(x,y)
        self.onWhat = o
        self.args[1] = o

    def getOnWhat(self):
        # return the second argument (object) of On(x,y)
        return self.onWhat
    
    def display(self):
        print "On(",self.what.getName(),",",self.onWhat.getName(),")",
