
def rectangle_area(length, width):
    return length * width

x = rectangle_area(50, 40)
print(f"{x = }")

data = [10, 15]
x = rectangle_area(*data)  # same as rectangle_area(data[0], data[1])
print(f"{x = }")

def spam(foo, *bar):
    pass

spam(*data)

# x * y
