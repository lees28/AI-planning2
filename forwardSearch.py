# forward search class (to be implemented)

from blocksWorld import BlocksWorld
from plan import Plan
from heuristic import Heuristic
from state import State
from action import Action
from heapq import *
import copy
from clear import Clear
from Queue import PriorityQueue


class ForwardSearch:
    def __init__(self,h):
        self.problem = BlocksWorld()

        # start with an empty plan
        self.plan = Plan()

        # h is a "heuristic" object
        self.h=h

    def search(self):
        # your implementation goes here
        init = self.problem.initialState
        cur =init
        hp=[]
        heappush(hp, (self.h.heuristic(init,self.problem),init, []))
        while (len(hp)>0):
            popped = heappop(hp)
            poppedstate= popped[1]
            #return plan if popped state is the goal state
            if poppedstate.entails(self.problem.goal):
                h= heappop(hp)
                a = h[2]
                for i in a:
                    self.plan.pushBack(i)
                self.plan = h[2]
                return self.plan
            applicables = self.getapplicables(poppedstate)
            nextstates= self.getNextStates(poppedstate, applicables)
            for ind in range(len(nextstates)):
                next = nextstates[ind]
                # update heuristic
                new_h = self.h.heuristic(State(next),self.problem)
                a = popped[2]
                b= copy.copy(a)
                b.append(applicables[ind])
                if State(next).entails(self.problem.goal):
                    for i in b:
                        self.plan.pushBack(i)
                    return self.plan
                heappush(hp,(1+ new_h, State(next),b))
        return self.plan

        # return the final plan





    #apply action to the current state
    def getNextStates(self,state, actionlist):
        ret=[]
        cur = state.getLiterals()
        curs = copy.copy(state)
        for action in actionlist:
            add = action.add
            delete = action.delete
            tmp = copy.copy(curs)
            tmplit= tmp.getLiterals()
            abc=[]
            ind =[]
            #get indices to delete from literals
            for i in range(len(tmplit)):
                for j in delete:
                    if tmplit[i].equals(j):
                        ind.append(i)
            for i in range(len(tmplit)):
                if not i in ind:
                    abc.append(tmplit[i])
            for i in add:
                #skip literal if it's Clear(Fl) else append
                if len(i.args) ==1 and i.args[0] == self.problem.floor:
                    pass
                else:
                    abc.append(i)
            ret.append(abc)
        return ret

    #return applicable actions
    def getapplicables(self,state):
        action = []
        for option in self.problem.actions:
            pre = option.getPreconditions()
            if state.entailsLiterals(pre):
                action.append(option)
        return action