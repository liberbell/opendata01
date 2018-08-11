# Least to Greatest
pointsInaGame = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(pointsInaGame)
print(sortedGame)

# Alphabetically
childen = ['sue', 'Jerry', 'Linda']
print(sorted(childen))
print(sorted(['Sue', 'jerry', 'linda']))

# Key Parameters
print(sorted('My favorite child is Linda'.split(), key=str.upper))
print(sorted(pointsInaGame,reverse=True))

leaderboard = {231: 'CKL',123: 'abc', 432:'JKC'}
print(sorted(leaderboard,reverse=True))
