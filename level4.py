import math

debug = False
level = "4"

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
            honeycomb_2d = [list(s) for s in honeycomb.strip().split("\n")]
            wasp_index_1d = honeycomb.replace("\n", "").find("W")
            # start the wasp as active cell
            actives = [divmod(wasp_index_1d, len(honeycomb_2d[0]))]

            # Check the surrounding combs
            offsets = [(-1, -1), (-1, 1), (0, -2), (0, 2), (1, -1), (1, 1)]
            while len(actives) > 0:
                print(actives)
                new_actives = []
                for cell in actives:
                    for offset in offsets:
                        position = (cell[0] + offset[0], cell[1] + offset[1])
                        if 0 > position[0] or position[0] >= len(honeycomb_2d) or 0 > position[1] or position[1] >= len(honeycomb_2d[0]):
                            escapes[index] = True
                            break
                        if honeycomb_2d[cell[0] + offset[0]][cell[1] + offset[1]] == "O":
                            honeycomb_2d[cell[0] + offset[0]][cell[1] + offset[1]] = "A"
                            new_actives.append((cell[0] + offset[0], cell[1] + offset[1]))
                    if escapes[index]:
                        break
                if escapes[index]:
                        break
                actives = new_actives
                
    
    with open(f"level{level}_output/level{level}-{file}.out", "w") as output_file:
        output_file.write("\n".join(["FREE" if cond else "TRAPPED" for cond in escapes]))
        # compute / write
        pass
