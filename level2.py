import math

debug = False
level = "2"

if debug:
    files = ["example"]
else:
    files = range(1,6)

for file in files:
    with open(f"level{level}/level{level}_{file}.in") as input_file:
        # read
        honeycombs_number = int(input_file.readline())
        _ = input_file.readline()
        honeycombs = input_file.read().split("\n\n")
        counts = []
        
        # Get position of wasp
        for honeycomb in honeycombs:

            honeycomb_2d = honeycomb.split("\n")
            wasp_index_1d = honeycomb.replace("\n", "").find("W")
            wasp_index_2d = divmod(wasp_index_1d, len(honeycomb_2d[0]))

            # Check the surrounding combs
            offsets = [(-1, -1), (-1, 1), (0, -2), (0, 2), (1, -1), (1, 1)]
            counts.append(str(sum([1 for offset in offsets if honeycomb_2d[wasp_index_2d[0] + offset[0]][wasp_index_2d[1] + offset[1]] == "O"])))
    
    with open(f"level{level}_output/level{level}-{file}.out", "w") as output_file:
        output_file.write("\n".join(counts))
        # compute / write
        pass
