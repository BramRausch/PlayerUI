import controls
import pygame

done = False
inter = controls.interface()
inter.musicController()
menu = controls.menu
sensitivity = 200
lastPress = {
	"up": 0,
	"down": 0,
	"left": 0,
	"right": 0,
	"select": 0
}

while not done:
	inter.loop()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
		if event.type == pygame.KEYDOWN:
			print(pygame.time.get_ticks())
			
			if event.key == pygame.K_UP:
				ticks = pygame.time.get_ticks()
				if inter.sleep:
					inter.volumeUp()
				else:
					inter.menuAction("up")
				lastPress["up"] = ticks
			elif event.key == pygame.K_DOWN:
				ticks = pygame.time.get_ticks()
				if inter.sleep:
					inter.volumeDown()
				else:
					inter.menuAction("down")
				lastPress["down"] = ticks
			elif event.key == pygame.K_LEFT:
				ticks = pygame.time.get_ticks()
				if inter.sleep:
					inter.prev()
				else:
					inter.menuAction("left")
				lastPress["left"] = ticks
			elif event.key == pygame.K_RIGHT:
				ticks = pygame.time.get_ticks()
				if inter.sleep:
					inter.next()
				else:
					inter.menuAction("right")
				lastPress["right"] = ticks
			elif event.key == pygame.K_RETURN:
				ticks = pygame.time.get_ticks()
				
				if inter.sleep:
					if ticks-lastPress["select"] < sensitivity:
						inter.toggleSleep()
						inter.playPause()
					else:
						inter.playPause()
				elif menu["current"] == "list" or menu["current"] == "Tracks":
					inter.play(menu[menu["current"]][inter.selectedItem])  # Play the selected song
					menu["Queue"] = list(menu[menu["current"]])  # copy the list where the song is selected to the queue
					menu["Queue"].remove(menu[menu["current"]][inter.selectedItem])  # Remove selected
					menu["Queue"].insert(0, menu[menu["current"]][inter.selectedItem])  # Put selected at first position
				elif menu["current"] == "musicController":
					if inter.selectedItem == 0:
						inter.volumeUp()
					elif inter.selectedItem == 1:
						inter.volumeDown()
					elif inter.selectedItem == 2:
						inter.prev()
					elif inter.selectedItem == 3:
						inter.playPause()
					elif inter.selectedItem == 4:
						inter.next()
					elif inter.selectedItem == 5:
						inter.shuffle()
				else:
					inter.menuAction("select")
				
				lastPress["select"] = ticks
	
	if not inter.sleep :
		# [filename, artist, album, title]
		if menu["current"] == "musicController":
			inter.musicController()
		elif menu["current"] == "Tracks" or menu["current"] == "Queue":
			inter.listView(list(map(lambda x: x[3], menu[menu["current"]])))
		elif menu["current"] == "list":
			inter.listView(list(map(lambda x: x[3], menu["list"])))
		else:
			inter.listView(menu[menu["current"]])
			
		if pygame.time.get_ticks()-max(lastPress.values()) >= 10000:
			inter.toggleSleep()
					
		pygame.display.update()  # display.update() without arguments updates the entire display just like display.flip()		
	pygame.time.Clock().tick(20)  # Limit the framerate to 20 FPS, this is to ensure it doesn't use all of the CPU resources