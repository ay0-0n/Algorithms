inp = open('input3_2.txt', 'r')
out = open('output3_2.txt', 'w')

n, amount = list(map(int, inp.readline().split()))
coins = list(map(int, inp.readline().split()))
dp = [[-1] * (n + 1) for i in range(amount + 1)]
def minCoins(coins, amount, index, dp):
    if amount == 0:
        return 0

    if index == len(coins):
        return float('inf')

    if dp[amount][index] != -1:
        return dp[amount][index]

    count_taken = float('inf')
    count_not_taken = float('inf')

    if coins[index] <= amount:
        count_taken = 1 + minCoins(coins, amount - coins[index], index, dp)

    count_not_taken = minCoins(coins, amount, index + 1, dp)

    dp[amount][index] = min(count_taken, count_not_taken)
    return dp[amount][index]


result = minCoins(coins, amount, 0, dp)
out.write(str(result))
out.close()