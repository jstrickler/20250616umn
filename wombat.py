import typing as T
from convert_temps import c2f
# from MODULE import NAME
# import MODULE
# MODULE.NAME
import convert_temps as ct

for ctemp in -40, 0, 32, 100:
    f = c2f(ctemp)
    print(f"{ctemp} C is {f} F")

x = ct.c2f(123)
print(f"{x = }")

# T.Iterable