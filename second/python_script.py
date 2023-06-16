import sys
if len(sys.argv) > 2:
    try:
        times = int(sys.argv[1])
    except:
        print('The first argument should be a number')
    else:
        string = sys.argv[2]
        print("Result:", string * times)
else:
    print("Please provide 2 arguments <string> <times to print>.")
