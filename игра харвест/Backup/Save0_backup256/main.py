while True:
	for i in range(3):
		if can_harvest():
			harvest()
#			till()
			plant(Entities.Tree)
			use_item(Items.Water)
		else:
			move(North)
			if can_harvest():
				harvest()
			else:
				move(East)
#			till()
			plant(Entities.Tree)
			use_item(Items.Water)
			
		

	
