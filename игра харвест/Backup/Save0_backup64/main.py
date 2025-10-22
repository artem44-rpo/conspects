while True:
	harvest()
	if can_harvest():
		plant(Entities.Bush)
	else:
		move(North)
		

	
