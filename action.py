# Action superclass

class Action:
    def __init__(self):
        # action name
        self.name = "NULL"

        # action arguments
        self.args = []

        # preconditions
        self.pre = []

        # add list
        self.add = []

        # delete list
        self.delete = []

    def getName(self):
        return self.name
        
    def getArgs(self):
        return self.args

    def setArgs(self, arguments):
        self.args = []
        for i in range(len(arguments)):
            self.args.append(arguments[i])

    def getPreconditions(self):
        return self.pre

    def setPreconditions(self, pre):
        self.pre = []
        for i in range(len(pre)):
            self.pre.append(pre[i])

    def getAddList(self):
        return self.add

    def setAddList(self, add):
        self.add = []
        for i in range(len(add)):
            self.add.append(add[i])

    def getDeleteList(self):
        return self.delete

    def setDeleteList(self, delete):
        self.delete = []
        for i in range(len(delete)):
            self.delete.append(delete[i])

    def display(self):
        print self.name
