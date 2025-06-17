values = ['a', 'b', 'c', 'd', 'e', 'f']

x, *y, z = values  # unpack values (which is an iterable) into individual variables

print(x, y, z)
print()

people = [
    ('Bill', 'Gates', 'Microsoft'),
    ('Steve', 'Jobs', 'Apple'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey', 'Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linux', 'Torvalds', 'Linux'),
]

for row in people:  # row is a tuple
    first_name, last_name, _ = row  # unpack row into variables
    print(first_name, last_name)
print()

for first_name, _, _ in people:  # a for loop unpacks if there is more than one variable
    # first_name, last_name, _ = people[0]
    print(first_name)
print()

for first_name, *not_used in people:  # a for loop unpacks if there is more than one variable
    # first_name, last_name, _ = people[0]
    print(first_name)
print()

_ = 12
_ = "Captain Hook"

