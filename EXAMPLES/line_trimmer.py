def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip('\n\r')  # 'yield' causes this function to return a generator object

mary_in = trimmed('../DATA/mary.txt')
print(f"{mary_in = }")

for trimmed_line in mary_in:
    print(trimmed_line)

def months():
    for month in "January", "February", "March":
        yield month

m = months()
print(f"{m = }")
for thing in m:
    print(thing)


def reversed(iterable):
    last_index = len(iterable) - 1
    for index in range(last_index, -1, -1):
        yield iterable[index]

names = ["Harry", "Hermione", "Ron"]

x = reversed(names)
print(f"{x = }")
for name in x:
    print(name)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]
dob_gen = (p[3] for p in people)
print(f"{dob_gen = }")
