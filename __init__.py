import controls
import pygame

done = False
inter = controls.interface()
inter.musicController()
menu = controls.menu

while not done:
	inter.loop()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				if inter.sleep:
					inter.volumeUp()
				else:
					inter.menuAction("up")
			elif event.key == pygame.K_DOWN:
				if inter.sleep:
					inter.volumeDown()
				else:
					inter.menuAction("down")
			elif event.key == pygame.K_LEFT:
				if inter.sleep:
					inter.prev()
				else:
					inter.menuAction("left")
			elif event.key == pygame.K_RIGHT:
				if inter.sleep:
					inter.next()
				else:
					inter.menuAction("right")
			elif event.key == pygame.K_RETURN:
				if inter.sleep:
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
					
		pygame.display.update()  # display.update() without arguments updates the entire display just like display.flip()		
	pygame.time.Clock().tick(20)  # Limit the framerate to 20 FPS, this is to ensure it doesn't use all of the CPU resources