# Clear(x)

from predicate import Predicate
from obj import Object

class Clear(Predicate):

    def __init__(self, obj):
        # argument to "Clear"
        # Clear(x): Clear(obj)
        self.obj = obj
        self.name = "Clear"
        self.args = []
        self.args.append(self.obj)

    def setObj(self,o):
        # set the argument of Clear
        self.obj = o
        self.args[0] = o

    def getObj(self):
        # return the argument of Clear
        return self.obj

    def display(self):
        print "Clear(",self.obj.getName(),")",
