# a generic planning problem

from state import State
    
class PlanningProblem:
    def __init__(self, name, initialState, goal, actions):
        # problem name
        self.name = name

        # initial state
        self.initialState = initialState

        # goal
        self.goal = goal

        # set of (grounded) actions
        self.actions = actions

    def getInitialState(self):
        return self.initialState

    def getGoal(self):
        return self.goal

    def getActions(self):
        return self.actions

    def reachedGoal(self, state):
        # returns true if the specified state
        # entails the goal (assuming that goals are 
        # conjunctions of positive literals)
        return state.entails(self.goal)

