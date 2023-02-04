# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]
class Node:
    def __init__(self, state, path):
        self.state = state
        self.path = path

def depthFirstSearch(problem):

    "*** YOUR CODE HERE ***"
    node = Node (problem.getStartState () , [])
    
    stack = [node]
    
    visited = []
    
    while stack:
       
        node = stack.pop ()

        if node. state in visited:
            continue
        visited.append (node.state)
        if problem.isGoalState (node.state):

            return node.path
        else:

            for s in problem.getSuccessors(node.state) :
                if s[0] not in visited:
                    print(s[0],s[1])
                    
                    neighbor_path = node.path + [s [1]]
                    
                    neighbor_node = Node(s [0], neighbor_path )
                    
                    stack.append(neighbor_node)
    

    util.raiseNotDefined()
class Node:
    def __init__(self, state, path):
        self.state = state
        self.path = path
def breadthFirstSearch(problem):

    "*** YOUR CODE HERE ***"
    node = Node(problem.getStartState(), [])
    
    queue = [node]
    
    visited = []    
    while queue:
        node = queue.pop(0)
        
        if node.state in visited:
            continue
        visited.append(node.state)

        if problem.isGoalState(node.state):
            return node.path
        else:
            for s in problem.getSuccessors(node.state):
                if s[0] not in visited:
                    
                    neighbor_path = node.path + [s[1]]
                    
                    neighbor_node = Node(s[0], neighbor_path)
                    
                    queue.append(neighbor_node)

    util.raiseNotDefined()
import queue as qu
fakecost = 0
class Node:
    def __init__(self, state, path):
        self.state = state
        self.path = path
def uniformCostSearch(problem):

    "*** YOUR CODE HERE ***"
    global fakecost
    priority_queue = qu.PriorityQueue ()
    
    node = Node(problem.getStartState () , [])
    
    priority_queue.put((0, fakecost, node))
    
    visited = []
    
    while not priority_queue.empty () :
        node_cost,_,node = priority_queue.get()
        
        if node.state in visited:
            continue
        
        visited.append(node.state)
    
        if problem.isGoalState(node.state):
            
            return node.path
        else:
            for s in problem.getSuccessors(node.state):
                
                if s[0] not in visited :

                    neighbor_path = node.path + [s[1]]
                    
                    neighbor_node = Node(s[0], neighbor_path)
                    
                    neighbor_cost = problem.getCostOfActions(node.path)
                    
                    fakecost=fakecost + 1
                    
                    priority_queue.put((neighbor_cost, fakecost,neighbor_node))


    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
