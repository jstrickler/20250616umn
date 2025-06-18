# define function
def main():
    print("main function")
    say_hello()

def say_hello():
    print("Hello, world")

# say_hello()  # Call function
main()

def spam():
    return 42

x = spam() * 10
print(f"{x = }")
print(f"{spam() = }")

def toast():
    print("Hello")

x = toast()
print(f"{x = }")

def c2f(cel_value):
    return 212, False

value, flag = c2f(100)
print(f"{value = }")
print(f"{flag = }")

x = c2f(98)
print(f"{x = }")
