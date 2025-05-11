import sys
from SolutionParts import SolutionParts
from BFSolver import BFSolver
from ASolver import ASRunner

if __name__ == "__main__":
    # Expect exactly 9 integers (the puzzle tiles in row-major order)
    args = sys.argv[1:]  # Skip the script name
    if len(args) != 9:
        print("Please provide exactly 9 numbers for the puzzle, e.g.:")
        print("  python Tiles.py 1 4 0 5 8 2 3 6 7")
        sys.exit(1)

    # Convert args to integers and reshape into 3×3
    tiles_list = list(map(int, args))
    initial_tiles = [
        tiles_list[0:3],
        tiles_list[3:6],
        tiles_list[6:9]
    ]

    print("Initial state:")
    for row in initial_tiles:
        print(row)

    # ---------------------------------------------------
    # BFS Algorithm
    # ---------------------------------------------------
    print("\nAlgorithm: BFS")
    print("-----------------------------")
    bfs_solver = BFSolver(initial_tiles)
    goal_state_bfs = bfs_solver.solve()  # BFS prints "No solution found." internally if it fails
    if goal_state_bfs is not None:
        solution_path_bfs = bfs_solver.get_solution_path(goal_state_bfs)
        path_length_bfs = bfs_solver.get_path_length(goal_state_bfs)
        print("Solution Path (tiles moved):", solution_path_bfs)
        print("Number of moves in the solution path:", path_length_bfs)

    print("\n*******************************\n")

    # ---------------------------------------------------
    # A* Algorithm
    # ---------------------------------------------------
    print("Algorithm: A*")
    a_solver = ASRunner(SolutionParts(initial_tiles))
    goal_state_astar = a_solver.solve()
    print("-----------------------------")
    if goal_state_astar is not None:
        solution_path_astar = a_solver.get_solution_path(goal_state_astar)
        path_length_astar = a_solver.get_path_length(goal_state_astar)
        expands_astar = a_solver.get_expands_count()
        print("Solution found after expanding", expands_astar, "nodes.")
        print("Solution Path (tiles moved):", solution_path_astar)
        print("Number of moves in the solution path:", path_length_astar, "\n")
