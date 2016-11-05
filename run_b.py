
from obj import Object
from predicate import Predicate
from on import On
from clear import Clear
from state import State
from action import Action
from move import Move
from moveToFloor import MoveToFloor
from plan import Plan

from blocksWorld import BlocksWorld

from forwardSearch import ForwardSearch
from heuristic import Heuristic
from gpheuristic import GPHeuristic

h = GPHeuristic()
s = ForwardSearch(h)
p = s.search()
p.display()
