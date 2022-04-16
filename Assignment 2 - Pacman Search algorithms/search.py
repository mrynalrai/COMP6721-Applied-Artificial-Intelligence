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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    #initialized openlist as stack
    openList = util.Stack()
    #seperate list for nodes in openList for faster indexing
    nodesInOpenList = []
    #initialized closedlist for visited nodes
    closedList = []
    #initialize initial state
    root = problem.getStartState()
    startNode = (root, [])
    #populate openlist with root node
    openList.push(startNode)
    nodesInOpenList.append(startNode[0])
        
    #while states remain to explore
    while not openList.isEmpty():
        #remove leftmost state from openList
        visitedState, actionList = openList.pop()
        
        #if goal return actionlist
        if problem.isGoalState(visitedState):
            return actionList
        else:
            #generate children of visitedState
            children = problem.getSuccessors(visitedState)
            #put visitedState on closed
            closedList.append(visitedState)
            #push each child to openList
            for child, action, cost in children:
                #discard children if already in closedlist or openlist
                if (child not in closedList) or (child not in nodesInOpenList):
                    newAction = actionList + [action]
                    newNode = (child, newAction)
                    #put child on left end of the queue
                    #handled by stack
                    openList.push(newNode)
                    nodesInOpenList.append(newNode[0])

    return actionList

        

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    #initialized openlist as queue
    openList = util.Queue()
    #seperate list for nodes in openList for faster indexing
    nodesInOpenList = []
    #initialized closedlist for visited nodes
    closedList = []
    #initialize initial state
    root = problem.getStartState()
    startNode = (root, [])
    #populate openlist with root node
    openList.push(startNode)
    nodesInOpenList.append(startNode[0])
        
    #while states remain to explore
    while not openList.isEmpty():
        #remove leftmost state from openList
        visitedState, actionList = openList.pop()
        #if goal return actionlist
        if problem.isGoalState(visitedState):
            return actionList
        else:
            #generate children of visitedState
            children = problem.getSuccessors(visitedState)
            #put visitedState on closed
            closedList.append(visitedState)
            #push each child to openList
            for child, action, cost in children:
                #discard children if already in closedlist or openlist
                if (child not in closedList) and (child not in nodesInOpenList):
                    newAction = actionList + [action]
                    newNode = (child, newAction)
                    #put child on right end of the queue
                    #handled by queue
                    openList.push(newNode)
                    nodesInOpenList.append(newNode[0])

    return actionList
    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    #initialized openlist as PriorityQueue
    #PriorityQueue has retrieval time complexity of O(1) 
    openList = util.PriorityQueue()
    #initialized closedlist for visited nodes
    #node:cost dictionary
    closedList = {}
    #initialize initial state
    root = problem.getStartState()
    startNode = (root, [], 0)
    #populate openlist with root node
    openList.push(startNode, 0)
    #while states remain to explore
    while not openList.isEmpty():
        #removes the state with lowest priority/cost from openList
        visitedState, actionList, currCost = openList.pop()
        #discard current visited state if already in closedlist or 
        #it replaces the previous entry in closedlist if it's cost is lower
        if ((visitedState not in closedList) or closedList[visitedState] > currCost) :
            #if goal return actionlist
            if problem.isGoalState(visitedState):
                return actionList
            #generate children of visitedState
            closedList[visitedState] = currCost
            children = problem.getSuccessors(visitedState)
            #push each child to openList
            for child, action, cost in children:                
                #put visitedState on closed
                newAction = actionList + [action]
                newCost = currCost + cost
                newNode = (child, newAction, newCost)
                #push child into the PriorityQueue with current cost as priority
                openList.push(newNode, newCost)

    return actionList

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    #initialized openlist as PriorityQueue
    #PriorityQueue has retrieval time complexity of O(1) 
    openList = util.PriorityQueue()
    #initialized closedlist for visited nodes
    #node:cost dictionary
    closedList = {}
    #initialize initial state
    root = problem.getStartState()
    startNode = (root, [], 0)
    #populate openlist with root node
    openList.push(startNode, 0)
    #while states remain to explore
    while not openList.isEmpty():
        #removes the state with lowest priority/cost from openList
        visitedState, actionList, currCost = openList.pop()
        #discard current visited state if already in closedlist or 
        #it replaces the previous entry in closedlist if it's cost is lower
        if ((visitedState not in closedList) or closedList[visitedState] > currCost) :
            #if goal return actionlist
            if problem.isGoalState(visitedState):   
                return actionList
            #generate children of visitedState
            closedList[visitedState] = currCost
            children = problem.getSuccessors(visitedState)
            #push each child to openList
            for child, action, cost in children:  
                #put visitedState on closed
                newAction = actionList + [action]
                #storing f(n) = g(n)+h(n) as cost of the child node
                newCost = problem.getCostOfActions(newAction) + heuristic(child, problem)
                newNode = (child, newAction, newCost)
                #push child into the PriorityQueue with current cost or f(n) as priority
                openList.push(newNode, newCost)

    return actionList
    


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
