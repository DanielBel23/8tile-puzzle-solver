from collections import deque
import copy
from SolutionParts import SolutionParts

class BFSolver:
    def __init__(self, initial_state):
        self.root = SolutionParts(initial_state)
        self.visited = set()
        self.queue = deque()
        self.expand_counter = 0

    def solve(self):
        # Start with the initial state
        self.visited.add(self.root)
        self.queue.append(self.root)
        while self.queue:
            state = self.queue.popleft()
            if self.is_goal(state):
                print("Solution found after expanding", self.expand_counter, "nodes.")
                return state
            self.expand(state)
        print("No solution found.")
        return None

    def expand(self, state):
        # Try each move: LEFT, RIGHT, UP & DOWN
        moves = [state.moveLEFT, state.moveRIGHT, state.moveUP, state.moveDOWN]
        for move_func in moves:
            child = move_func()
            if child is not None and child not in self.visited:
                self.visited.add(child)
                self.queue.append(child)
                self.expand_counter += 1

    def is_goal(self, state):
        return state.tiles == SolutionParts.target_state

    def get_solution_path(self, goal_state):
        """
        Reconstruct the path from the initial state to the goal state.
        Returns a list of the non-zero numbers (tiles moved) in the order they were moved.
        """
        path = []
        current = goal_state
        while current.parent is not None:
            path.append(current.action)
            current = current.parent
        path.reverse()
        return path

    def get_path_length(self, goal_state):
        """
        Return the length (number of moves) of the solution path.
        """
        return len(self.get_solution_path(goal_state))
