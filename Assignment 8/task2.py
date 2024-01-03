inp = open('input2_4.txt', 'r')
out = open('output2_4.txt', 'w')

n = int(inp.readline())

def countWays(N):
    ways = [0] * (N + 1)
    ways[0] = 1
    ways[1] = 1

    for i in range(2, N + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[N]


out.write(f'{countWays(n)}')
