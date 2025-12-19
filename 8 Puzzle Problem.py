import heapq
class PuzzleNode:
   def __init__(self, state, parent=None, move=None, cost=0):
       self.state = state
       self.parent = parent
       self.move = move
       self.cost = cost
       self.heuristic = self.calculate_heuristic()
   def __lt__(self, other):
       return (self.cost + self.heuristic) < (other.cost + other.heuristic)
   def calculate_heuristic(self):
       goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
       distance = 0
       for i in range(9):
           if self.state[i] != 0:
               x1, y1 = divmod(i, 3)
               x2, y2 = divmod(goal_state.index(self.state[i]), 3)
               distance += abs(x1 - x2) + abs(y1 - y2)
       return distance
def get_neighbors(node):
   neighbors = []
   blank_pos = node.state.index(0)
   moves = {'U': -3, 'D': 3, 'L': -1, 'R': 1}
   for move, offset in moves.items():
       new_pos = blank_pos + offset
       if new_pos < 0 or new_pos >= len(node.state) or \
          (move == 'L' and blank_pos % 3 == 0) or \
          (move == 'R' and blank_pos % 3 == 2):
           continue
       new_state = node.state[:]
       new_state[blank_pos], new_state[new_pos] = new_state[new_pos], new_state[blank_pos]
       neighbors.append(PuzzleNode(new_state, node, move))
   return neighbors
def solve_8_puzzle(initial_state):
   open_list = []
   closed_set = set()
   heapq.heappush(open_list, PuzzleNode(initial_state))
   while open_list:
       current_node = heapq.heappop(open_list)
       if current_node.state == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
           return reconstruct_path(current_node)
       closed_set.add(tuple(current_node.state))
       for neighbor in get_neighbors(current_node):
           if tuple(neighbor.state) not in closed_set:
               heapq.heappush(open_list, neighbor)
   return None
def reconstruct_path(node):
   path = []
   while node:
       path.append((node.move, node.state))
       node = node.parent
   return path[::-1]
# Example Usage
initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
solution_path = solve_8_puzzle(initial_state)
if solution_path:
   print("Solution found!")
   for move, state in solution_path:
       print(f"Move: {move}, State: {state}")
else:
   print("No solution exists.")