import math
import hexutil

debug = False
level = "3"

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
        escapes = [False] * honeycombs_number
        
        # Get position of wasp
        for index, honeycomb in enumerate(honeycombs):
            honeycomb_2d = honeycomb.strip().split("\n")
            wasp_index_1d = honeycomb.replace("\n", "").find("W")
            wasp_index_2d = divmod(wasp_index_1d, len(honeycomb_2d[0]))

            # Check the surrounding combs
            offsets = [(-1, -1), (-1, 1), (0, -2), (0, 2), (1, -1), (1, 1)]
            for offset in offsets:
                i = 1
                foundBarrier = False
                while not foundBarrier and 0 <= (wasp_index_2d[0] + i * offset[0]) < len(honeycomb_2d) and 0 <= (wasp_index_2d[1] + i * offset[1]) < len(honeycomb_2d[0]):
                    if honeycomb_2d[wasp_index_2d[0] + offset[0] * i][wasp_index_2d[1] + offset[1] * i] == "X":
                        foundBarrier = True
                    i += 1
                if not foundBarrier:
                    escapes[index] = True
                
    
    with open(f"level{level}_output/level{level}-{file}.out", "w") as output_file:
        output_file.write("\n".join(["FREE" if cond else "TRAPPED" for cond in escapes]))
        # compute / write
        pass
