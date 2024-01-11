

#bfd and dfs search of a maze


'''0 represents a wall, 1 represents a path, 2 represents the start, 3 represents the end'''
maze = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0],
        [0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0],
        [0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0],
        [0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0],
        [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
        [0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
        [0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0],
        [0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0],
        [0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0],
        [0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0],
        [0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,3,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]

directions = [(0,1), (1,0), (0,-1), (-1,0)]

def find_start(maze):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 2:
                return (i,j)
            
def find_end(maze):
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
            if maze[next[0]][next[1]] != 0 and next not in visited:
                visited[next] = current  # Store the current node as the previous node for the next node
                queue.append(next)
    return False

def dfs(maze):
    '''depth first search'''
    start = find_start(maze)
    end = find_end(maze)
    stack = [start]
    visited = {start: None}  # Store the previous node for each visited node
    while stack:
        current = stack.pop()
        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = visited[current]
            return path[::-1]  # Reverse the path to go from start to end
        for direction in directions:
            next = (current[0] + direction[0], current[1] + direction[1])
            if maze[next[0]][next[1]] != 0 and next not in visited:
                visited[next] = current  # Store the current node as the previous node for the next node
                stack.append(next)
    return False

def print_path(maze, path):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i,j) in path:
                print('*', end=' ')
            else:
                print(cell, end=' ')
        print()

def main():
    while True:
        choice = input("Choose bfs or dfs, input \"q\" to quit: ")
        match choice:
            case "bfs":
                pathBfs = bfs(maze)
                print_path(maze, pathBfs)
                print("bfs")
            case "dfs":
                pathDfs = dfs(maze)
                print_path(maze, pathDfs)
                print("dfs")
            case "q":
                break
            case _:
                print("Invalid input")
          

if __name__ == '__main__':
    main()

