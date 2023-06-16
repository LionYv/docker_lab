import sys

# Check if a username argument is provided
if len(sys.argv) > 1:
    inp = sys.argv[1]
    print("you entered:", inp)
else:
    print("Please provide an argument.")
