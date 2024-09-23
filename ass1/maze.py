
import tracemalloc


'''1 represents a wall, 0 represents a path, 2 represents the start, 3 represents the end'''
maze = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1],
        [1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,0,1],
        [1,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1],
        [1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,0,0,0,0,0,1],
        [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1],
        [1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1],
        [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,0,1,1],
        [1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0,0,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,3,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]


directions = [(0,1), (1,0), (0,-1), (-1,0)]

def find_start(maze):
    '''function to find the starting point of the maze, which is represented by a 2, returns the coordinates as a tuple. 
    The reason for choosing a tuple is because it is immutable, and therefore cannot be changed.'''
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 2:
                return (i,j)
            
def find_end(maze):
    '''function to find the end point of the maze, which is represented by a 3, returns the coordinates as a tuple. 
    The reason for choosing a tuple is because it is immutable, and therefore cannot be changed.'''
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 3:
                return (i,j)


def bfs(maze):
    '''breadth first search'''
    start = find_start(maze)
    end = find_end(maze)
    queue = [start]
    visited = {start: None}  # Store the previous node for each visited node
    while queue:
        current = queue.pop(0)
        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = visited[current]
            return path[::-1]  # Reverse the path to go from start to end
        for direction in directions:
            next = (current[0] + direction[0], current[1] + direction[1])
            if maze[next[0]][next[1]] != 1 and next not in visited:
                visited[next] = current  # Store the current node as the previous node for the next node
                queue.append(next)
    return False

def dfs_rec(maze, current, visited, end):
    '''recursive depth first search'''
    if current == end:
        return [current]
    for direction in directions:
        next = (current[0] + direction[0], current[1] + direction[1])
        if maze[next[0]][next[1]] != 1 and next not in visited:
            visited.add(next)
            path = dfs_rec(maze, next, visited, end)
            if path:
                return [current] + path
    return False

def dfs(maze):
    '''depth first search'''
    start = find_start(maze)
    end = find_end(maze)
    visited = {start}
    return dfs_rec(maze, start, visited, end)
    

def a_star(maze):
    class Node:
        def __init__(self, position, parent=None):
            self.position = position
            self.parent = parent
            self.g = 0
            self.h = 0
            self.f = 0

        def __eq__(self, other):
            return self.position == other.position

        def __lt__(self, other):
            return self.f < other.f

        def __repr__(self):
            return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"


    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])


    start = Node(find_start(maze))
    end = Node(find_end(maze))
    open_list = [start]
    closed_list = []
    while open_list:
        current = min(open_list)
        open_list.remove(current)
        closed_list.append(current)
        if current == end:
            path = []
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Reverse the path to go from start to end
        for direction in directions:
            next = (current.position[0] + direction[0], current.position[1] + direction[1])
            if maze[next[0]][next[1]] != 1:
                next = Node(next, current)
                next.g = current.g + 1
                next.h = heuristic(next.position, end.position)
                next.f = next.g + next.h
                if next in closed_list:
                    continue
                if next in open_list:
                    if next.g > open_list[open_list.index(next)].g:
                        continue
                open_list.append(next)


    return False



def print_path(maze, path):
    '''function to print the path taken to solve the maze.'''
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i,j) in path:
                print('*', end=' ')
            else:
                print(cell, end=' ')
        print()

def main():
    
    tracemalloc.start()
    
    pathBfs = bfs(maze)
    print_path(maze, pathBfs)
    print("BFS","\n", "length of pathBfs:", len(bfs(maze)))

    bfs_size, bfs_peak = tracemalloc.get_traced_memory()
    tracemalloc.reset_peak()
    
    print("DFS","\n", "length of pathDfs:", len(dfs(maze)))
    pathDfs = dfs(maze)
    print_path(maze, pathDfs)

    dfs_size, dfs_peak = tracemalloc.get_traced_memory()
    tracemalloc.reset_peak()

    print("A*","\n", "length of pathAStar:", len(a_star(maze)))
    pathAStar = a_star(maze)
    print_path(maze, pathAStar)

    a_star_size, a_star_peak = tracemalloc.get_traced_memory()

    print("BFS memory size:", bfs_size/1024, "KB")
    print("BFS memory peak:", bfs_peak/1024, "KB")
    print("DFS memory size:", dfs_size/1024, "KB")
    print("DFS memory peak:", dfs_peak/1024, "KB")
    print("A* memory size:", a_star_size/1024, "KB")
    print("A* memory peak:", a_star_peak/1024, "KB")

    tracemalloc.stop()

    




    

if __name__ == '__main__':
    main()

