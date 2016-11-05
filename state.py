# class defining State

from predicate import Predicate
    
class State:
    def __init__(self,literals):
        # state literals
        self.literals = literals

    def getLiterals(self):
        # returns state literals (list)
        return self.literals

    def addLiteral(self,lit):
        # adds a literal to state
        self.literals.append(lit)
        
    def entails(self,state):
        # returns True if this state entails the argument state
        # for example, if this state entails a goal, you can call s.entails(goal) and it will return True
        lit = state.getLiterals()

        return self.entailsLiterals(lit)

    def entailsLiterals(self, literals):
        # same as "entails" above, but working directly with the literals
        
        for i in range(len(literals)):
            # if lit[i] is not in this state, entailment is false
            if (not self.containsLiteral(literals[i])):
                return False

        return True
    
    def equals(self,state):
        # returns True if the argument state is equal to this state
        # two states are equal if they contain the same literals
        # the predicate class (each literal is of type "Predicate") allows you 
        # to check if two literals (predicates) are equal
        
        lit = state.getLiterals()

        if not (len(lit) == len(self.literals)):
            return False

        # this state entails the argument state if the argument includes
        # a subset of literals
        for i in range(len(lit)):
            # if lit[i] is not in this state, entailment is false
            if (not self.containsLiteral(lit[i])):
                return False

        return True

    def containsLiteral(self,literal):
        # returns true if this class contains (in the "predicate equal" sense) 
        # the specified literal
        for i in range(len(self.literals)):
            if (self.literals[i].equals(literal)):
                return True

        return False

    def isSatisfied(self,literal):
        # returns true if the specified literal is
        # satisfied (is true) in this state
        return self.containsLiteral(literal)

    def display(self):
        for l in self.literals:
            l.display()
            print ",",
