# Itertools
import itertools

# Infinite Counting
for x in itertools.count(50, 5):
    print(x)
    if x == 80:
        break;

# Infinite Cycling
for c in itertools.cycle('Racecar'):
    print(c)

# Infinite Repeating
