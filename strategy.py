# here you should implement your strategy for picking the location of the dice roll

def auto_pick_position(roll, grid):
    # naive implementation, simply add number into the next available slot
    if roll == 6:
        for i in range(1, 3):
            for v in range(1, 2):
                if not grid.has_value_been_set(v, i):
                    grid.set_value(v, i, roll)
                    break
                else:
                    pass
    elif roll == 5:
        for x in range(1, 3):
            for y in range(0, 3):
                if grid.has_value_been_set(x, y):
                    pass
                else:
                    grid.set_value(x, y, roll)
    elif roll == 3:
        for s in range(0, 2):
            for t in range(1, 3):
                if grid.has_value_been_set(s, t):
                    pass
                else:
                    grid.set_value(s, t, roll)
    elif roll == 4:
        for x in range(0, 2):
            for t in range(0, 2):
                if grid.has_value_been_set(x, t):
                    pass
                else:
                    grid.set_value(x, t, roll)
    elif roll == 1:
        for f in range(0, 3):
            for d in range(1, 2):
                if grid.has_value_been_set(f, d):
                    pass
                else:
                    grid.set_value(f, d, roll)
    else:
        grid.fill_next_empty_space(roll)
