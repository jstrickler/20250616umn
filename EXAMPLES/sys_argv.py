# batch 
#  python script.py arg1 arg2 arg3 ...
import sys

print(f"sys.argv: {sys.argv}\n")

print(f"{sys.argv[0] = }")

first_arg = sys.argv[1]  # First command line argument
print(f"first_arg: {first_arg}")
print(f"{type(first_arg) = }")


