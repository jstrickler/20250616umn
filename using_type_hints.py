import typing

def rectangle_area(length: typing.Union[int, float], width: int | float) -> int | float:
    return length * width

x = rectangle_area(5, 10)
print(f"{x = }")

rectangle_area(4.5, 8.9)

result: str

result = rectangle_area(5, 10)
print(f"{result = }")

Number = int | float

def total(items: typing.Iterable[Number]) -> Number:
    return sum(items)

nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]

print(f"{total(nums) = }")

values = 1, 5, 99, 42, 89.6

print(f"{total(values) = }")

