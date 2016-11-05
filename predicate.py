# Predicate class

class Predicate:

    def __init__(self):
        # name
        self.name = "NULL"

        # arguments
        self.args = []

    def getName(self):
        return self.name

    def equals(self,pred):
        'check if predicates are equal'
        '(two predicates are equal if their names and arguments are identical'

        if not (len(self.args) == len(pred.getArgs())) or not (self.name == pred.getName()):
            return False

        for i in range(len(self.args)):
            if not (self.args[i] == pred.getArgs()[i]):
                return False

        return True
    
    def getArgs(self):
        # returns arguments to this predicate
        return self.args

    def setArgs(self, arguments):
        # sets the argument list (with a list of objects)
        self.args = []
        for i in range(len(arguments)):
            self.args.append(arguments[i])

    
    def display(self):
        print self.name,
