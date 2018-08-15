# Itertools Part 2
import itertools

election = {1: 'Barb', 2: 'Karen', 3: 'Erin'}
for p in itertools.permutations(election):
    print(p)

for p1 in itertools.permutations(election.values()):
    print(p1)

# Permutations: Order matters - some copies with same inputs but in different order

# Combinations: Order does not matter - no copies with same inputs
colorsForPainting = ['red', 'blue', 'yellow', 'orange', 'purple', 'pink']
for c in itertools.combinations(colorsForPainting, 2):
    print(c)
