a = 0
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():  
				harvest()
			till()
			plant(Entities.Carrot)  
			get_water()  
			use_item(Items.Water) 
			move(North)
		move(East)