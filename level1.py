debug = False
level = "1"

if debug:
    files = ["example"]
else:
    files = range(1,6)

for file in files:
    with open(f"level{level}/level{level}_{file}.in") as input_file:
        # read
        honeycombs = input_file.read().count("O")
    
    with open(f"level{level}_output/level{level}-{file}.out", "w") as output_file:
        output_file.write(str(honeycombs))
        # compute / write
        pass
