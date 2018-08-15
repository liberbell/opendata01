# Command Line Arguments
import sys

# Print Arguments
print('Number of Arguments:', len(sys.argv), ' arguments')
print('Arguments ', sys.argv)

# Remove Arguments
sys.argv.remove(sys.argv[0])

print('Arguments', sys.argv)

# Sum up the Arguments
