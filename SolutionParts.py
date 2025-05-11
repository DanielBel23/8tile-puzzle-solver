import copy

class SolutionParts:
    # target state of the complete puzzle
    target_state = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]

    # movement vectors
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    def __init__(self, tiles):
        self.tiles = tiles
        self.parent = None      # To trace back the solution path
        self.action = None      # The non-zero tile that moved into the blank space
        # find the position of the empty tile (represented by 0)
        for i in range(len(tiles)):
            for j in range(len(tiles[i])):
                if tiles[i][j] == 0:
                    self.empty = (i, j)
                    break

    def move(self, direction):
        i, j = self.empty
        x, y = direction
        new_i, new_j = i + x, j + y
        # Check for valid move boundaries
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_tiles = copy.deepcopy(self.tiles)
            # Identify the tile that will be moved into the empty space
            moved_tile = new_tiles[new_i][new_j]
            # Swap the empty space with the adjacent tile
            new_tiles[i][j], new_tiles[new_i][new_j] = new_tiles[new_i][new_j], new_tiles[i][j]
            child = SolutionParts(new_tiles)
            child.parent = self
            child.action = moved_tile
            return child
        # Invalid move returns None
        return None

    def moveUP(self):
        return self.move(self.UP)

    def moveDOWN(self):
        return self.move(self.DOWN)

    def moveLEFT(self):
        return self.move(self.LEFT)

    def moveRIGHT(self):
        return self.move(self.RIGHT)

    def get_state(self):
        return self.tiles

    def __eq__(self, other):
        if not isinstance(other, SolutionParts):
            return False
        return self.tiles == other.tiles

    def __hash__(self):
        return hash(str(self.tiles))

    def __str__(self):
        return '\n'.join(str(row) for row in self.tiles)
