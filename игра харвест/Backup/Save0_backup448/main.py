a = 0
while True:
	if can_harvest():  
		harvest()
	till()
	plant(Entities.Carrot)  
	get_water()  
	use_item(Items.Water) 
	move(North)
	a += 1
	if a == 8:
		a = 0
		move(East)