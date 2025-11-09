import sys

args = sys.argv

try:
    assert len(args) < 3, "more than one argument is provided" 
except AssertionError as error:
    print("AssertionError:", error, "\n")
    quit()

if len(args) < 2:
    print("\n")
    quit()

try:
    assert args[1].lstrip("-").isdigit(), "argument is not an integer"
    print("I'm Even.\n") if int(args[1]) % 2 == 0 else print("I'm Odd.\n")
except AssertionError as error:
    print("AssertionError:", error, "\n")

