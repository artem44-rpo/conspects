while True:
	for i in range(3):
		if can_harvest():
			harvest()
			plant(Entities.Bush)
		else:
			move(North)
			if can_harvest():
				harvest()
			else:
				move(East)
			plant(Entities.Bush)
			
		

	
