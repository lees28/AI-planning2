# The Blocks World planning problem

from planningProblem import PlanningProblem
from action import Action
from move import Move
from moveToFloor import MoveToFloor
from obj import Object
from predicate import Predicate
from on import On
from clear import Clear
from state import State

class BlocksWorld(PlanningProblem):

    def __init__(self):
        self.name = "BlocksWorld"

        # define objects
        A = Object("A")
        B = Object("B")
        C = Object("C")
        floor = Object("Fl")
        blocks = [A,B,C]

        self.A = A
        self.B = B
        self.C = C
        self.floor = floor

        # define goal (C on B on A on floor)
        goalLiterals = []
        goalLiterals.append(On(A,floor))
        goalLiterals.append(On(B,A))
        goalLiterals.append(On(C,B))

        self.goal = State(goalLiterals)

        # define initial state (C on B, B on floor, A on floor)
        initStateLiterals = []
        initStateLiterals.append(On(C,B))
        initStateLiterals.append(On(B,floor))
        initStateLiterals.append(On(A,floor))
        initStateLiterals.append(Clear(A))
        initStateLiterals.append(Clear(C))

        self.initialState = State(initStateLiterals)

        # create actions
        self.actions = []
        for b in blocks:
            for bprime in blocks:
                if not (bprime == b):
                    # move to floor
                    self.actions.append(MoveToFloor(b,bprime,floor))
                    # move from floor
                    self.actions.append(Move(b,floor,bprime))

                for bpp in blocks:
                    if not (bprime == b) and not (bprime == bpp) and not (b == bpp):
                        self.actions.append(Move(b,bprime,bpp))


    def display(self):
        print "Initial State: ",
        self.initialState.display()
        print "\n"

        print "Goal: ",
        self.goal.display()
        print "\n"

        print "Actions: "
        for a in self.actions:
            a.display()
            print ""

        
