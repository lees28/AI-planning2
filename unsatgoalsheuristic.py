
from heuristic import Heuristic
from state import State
from planningProblem import PlanningProblem

class UnsatGoalsHeuristic(Heuristic):
    def heuristic(self, state, problem):
        # "number of unsatisfied goals" heuristic
        cost = 0

        # your code goes here
        goal = problem.goal
        #goal.display()
        #print ""
        #state.display()

        cur_lit =state.getLiterals()
        for goal_lit in goal.getLiterals():
            if not state.containsLiteral(goal_lit):
                cost += 1
        return cost
