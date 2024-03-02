
from queue import Queue

class PuzzleSolver:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        self.queue = Queue()
        self.queue.put((self.initial_state, []))

    def solve_puzzle(self):
        while not self.queue.empty():
            current_state, path = self.queue.get()

            if current_state == self.goal_state:
                return path

            zero_index = current_state.index(0)

            possible_moves = []
            if zero_index % 3 > 0:
                possible_moves.append(zero_index - 1)
            if zero_index % 3 < 2:
                possible_moves.append(zero_index + 1)
            if zero_index // 3 > 0:
                possible_moves.append(zero_index - 3)
            if zero_index // 3 < 2:
                possible_moves.append(zero_index + 3)

            for move in possible_moves:
                new_state = current_state.copy()
                new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]
                new_path = path + [move]
                self.queue.put((new_state, new_path))

        return None

# Example usage:
initial_state = [2, 8, 1, 0, 4, 3, 7, 6, 5]  # Replace with your initial state
solver = PuzzleSolver(initial_state)
solution = solver.solve_puzzle()

if solution:
    print("Solution found!")
    print("Path:", solution)
else:
    print("No solution found.")