import os
file_name = 'states.txt'
temp_name = "temp.txt"

with open(file_name) as file_in:
    with open(temp_name, "w") as file_out:
        for line in file_in:
            new_line = line.upper()
            file_out.write(new_line)

os.rename(file_name, file_name + '.BAK')
os.rename(temp_name, file_name)

# if I'm in pyuminn
# use  "c:/Users/Administrator/Desktop/pyuminn/DATA/ctemps.txt"
x = open("c:/Users/Administrator/Desktop/pyuminn/DATA/ctemps.txt")
# if I'm in ANSWERS
# use  "../DATA/mary.txt"