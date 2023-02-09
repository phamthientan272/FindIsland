import sys
from utils.recursion_limit import recursionlimit
from collections import deque
class Map:
    def __init__(self, map):
        self.__map = map
        self.__n_row = len(map)
        self.__n_col = len(map[0])
        self.__count = 0
   
    def count_islands(self):
        visited = [[False for j in range(self.__n_col)] for i in range(self.__n_row)]
        self.__count = 0
        
        default_recursion_limit = sys.getrecursionlimit()
        if self.__n_col * self.__n_row >= default_recursion_limit:
            limit = self.__n_col * self.__n_row * 4
        else:
            limit = default_recursion_limit * 2
        print(f"the recursion limit is {limit}")
           
        with recursionlimit(limit):
            for i in range(self.__n_row):
                for j in range(self.__n_col):
                    if visited[i][j] == False and self.__map[i][j] == 1:
                        self.__count += 1
                        # self.__dfs(i, j, visited)
                        self.__bfs(i, j, visited)
            return self.__count 
        
        
    def __dfs(self, i, j, visited):
        """
        Mark the cell as visited. And call dfs on available cell.
        Each cell has 8 neighbour cells. Need to check its availability before calling dfs.
        """
        visited[i][j] = True
        
        row_index = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_index = [1, 0, 1, -1, 1, -1, 0, 1]
        
        for k in range(8):
            if self.__is_safe_to_visit(i + row_index[k], j + col_index[k], visited):
                self.__dfs(i + row_index[k], j + col_index[k], visited)
    
    def __bfs(self, i, j, visited):
        """
        Perform BFS on the map to traverse the connected cells.
        """
        queue = deque([(i, j)])
        visited[i][j] = True
        
        row_index = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_index = [1, 0, 1, -1, 1, -1, 0, 1]
        
        while queue:
            i, j = queue.popleft()
            for k in range(8):
                if self.__is_safe_to_visit(i + row_index[k], j + col_index[k], visited):
                    visited[i + row_index[k]][j + col_index[k]] = True
                    queue.append((i + row_index[k], j + col_index[k]))
                    
    def __is_safe_to_visit(self, i, j, visited):
        """
        A cell that is available to call a DFS is its position is inside the map,
        it is not visited before,
        and it has a value of 1
        """
        
        if  i >= 0 and i < self.__n_row and \
            j >= 0 and j < self.__n_col and \
            not visited[i][j] and self.__map[i][j] == 1:
                return True
        else:
            return False
        
        
        
        