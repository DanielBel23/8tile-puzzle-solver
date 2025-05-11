from SolutionParts import SolutionParts
import heapq


class ASRunner:
    def __init__(self, initial_state):
        self.root = initial_state
        self.expands = 0
        self.goal = None

    def solve(self):
        # A* search using heapq as priority queue.
        open_list = []
        # g_score holds the cost from start to the current state.
        g_score = {self.root: 0}
        h = ASHeuristic(self.root).cost
        f_score = g_score[self.root] + h
        counter = 0  # tie-breaker counter
        heapq.heappush(open_list, (f_score, counter, self.root, 0))  # (f, counter, state, g)
        while open_list:
            f, _, current, g = heapq.heappop(open_list)
            if self.is_goal(current):
                self.goal = current
                return current
            self.expands += 1
            # Expand neighbors: LEFT, RIGHT, UP, DOWN
            for move_func in [current.moveLEFT, current.moveRIGHT, current.moveUP, current.moveDOWN]:
                neighbor = move_func()
                if neighbor is None:
                    continue
                tentative_g = g + 1
                if neighbor in g_score and tentative_g >= g_score[neighbor]:
                    continue
                g_score[neighbor] = tentative_g
                h_neighbor = ASHeuristic(neighbor).cost
                f_neighbor = tentative_g + h_neighbor
                counter += 1
                heapq.heappush(open_list, (f_neighbor, counter, neighbor, tentative_g))
        return None

    def is_goal(self, state):
        return state.tiles == SolutionParts.target_state

    def get_solution_path(self, goal_state):
        """
        Reconstructs the simplified solution path as a list of tiles moved.
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
        Returns the number of moves in the solution path.
        """
        return len(self.get_solution_path(goal_state))

    def get_expands_count(self):
        """
        Returns the number of node expansions performed.
        """
        return self.expands


class ASHeuristic:
    def __init__(self, state):
        self.cost = 0
        self.estimate_heuristic(state)

    def estimate_heuristic(self, state):
        # Manhattan distance + 2*(linear conflicts in rows and columns)
        self.cost = self.calc_manhattan(state) + 2 * (self.conflict_rows(state) + self.conflict_columns(state))

    def conflict_rows(self, state):
        conf_sum = 0
        for i in range(len(state.tiles)):
            conf_sum += self.line_conflict_counter(i, state.tiles[i])
        return conf_sum

    def conflict_columns(self, state):
        conf_sum = 0
        board_size = len(state.tiles)
        for j in range(board_size):
            col_indices = []
            for i in range(board_size):
                tile = state.tiles[i][j]
                if tile != 0 and (tile % board_size) == j:
                    col_indices.append(i)
            count_con = 0
            for m in range(len(col_indices)):
                for n in range(m + 1, len(col_indices)):
                    if col_indices[m] > col_indices[n]:
                        count_con += 1
            conf_sum += count_con
        return conf_sum

    def line_conflict_counter(self, line_num, line):
        inplace = []
        board_size = len(SolutionParts.target_state)
        for i in range(len(line)):
            if line[i] != 0 and line_num == line[i] // board_size:
                inplace.append(i)
        count_con = 0
        for m in range(len(inplace)):
            for n in range(m + 1, len(inplace)):
                if inplace[m] > inplace[n]:
                    count_con += 1
        return count_con

    def calc_manhattan(self, state):
        man_cost = 0
        board_size = len(state.tiles)
        for i in range(board_size):
            for j in range(board_size):
                tile = state.tiles[i][j]
                if tile != 0:
                    i_calc = tile // board_size
                    j_calc = tile % board_size
                    man_cost += abs(i_calc - i) + abs(j_calc - j)
        return man_cost
