# Range -> range instance that holds all nums counting by one between 0 and first input
# List -> lists numbers from the inputted tuple

numberdContestants = range(30)

print(list(numberdContestants))

for c in list(numberdContestants):
    print('Contestant ' + str(c) + ' is here')

luckyWinner = range(7, 30, 5)

print(list(luckyWinner))
