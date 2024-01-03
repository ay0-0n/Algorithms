inp = open("Input Files/Task 06/input6_3.txt", 'r')
out = open("output6_3.txt", 'w')

row, col = tuple(map(int, inp.readline().split()))
map = [inp.readline()[:-1] for i in range(row)]

def max_diamonds(map, row, col):
    visited = [[False for i in range(col)] for i in range(row)]
    maxD = 0

    def dfs(map, r, c):
        if r < 0 or r >= len(map) or c < 0 or c >= len(map[0]):
            return 0
        elif visited[r][c] or map[r][c] == '#':
            return 0

        visited[r][c] = True
        diamond_collected = 0

        if map[r][c] == 'D':
            diamond_collected += 1

        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for rx, cx in move:
            diamond_collected += dfs(map, r+rx, c+cx)

        return diamond_collected

    for r in range(row):
        for c in range(col):
            if map[r][c] == '.' and visited[r][c] is False:
                maxD = max(maxD, dfs(map, r, c))
    return maxD


out.write(str(max_diamonds(map, row, col)))
