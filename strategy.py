
# here you should implement your strategy for picking the location of the dice roll

def auto_pick_position(roll, grid):
	# naive implementation, simply add number into the next available slot		
	grid.fill_next_empty_space(roll)