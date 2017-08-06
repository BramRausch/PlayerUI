import controls
import pygame

done = False
music = controls.musicControl()
inter = controls.interface()
inter.musicController()
menu = controls.menu

while not done:
	music.loop()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				if inter.sleep:
					music.volumeUp()
				else:
					inter.menuAction("up")
			elif event.key == pygame.K_DOWN:
				if inter.sleep:
					music.volumeDown()
				else:
					inter.menuAction("down")
			elif event.key == pygame.K_LEFT:
				if inter.sleep:
					music.prev()
				else:
					inter.menuAction("left")
			elif event.key == pygame.K_RIGHT:
				if inter.sleep:
					musix.next()
				else:
					inter.menuAction("right")
			elif event.key == pygame.K_RETURN:
				if inter.sleep:
					music.playPause()
				elif menu["current"] == "list" or menu["current"] == "Tracks":
					music.play(menu[menu["current"]][inter.selectedItem])  # Play the selected song
					menu["Queue"] = list(menu[menu["current"]])  # copy the list where the song is selected to the queue
					menu["Queue"].remove(menu[menu["current"]][inter.selectedItem])  # Remove selected
					menu["Queue"].insert(0, menu[menu["current"]][inter.selectedItem])  # Put selected at first position
				elif menu["current"] == "musicController":
					if inter.selectedItem == 0:
						music.volumeUp()
					elif inter.selectedItem == 1:
						music.volumeDown()
					elif inter.selectedItem == 2:
						music.prev()
					elif inter.selectedItem == 3:
						music.playPause()
					elif inter.selectedItem == 4:
						music.next()
					elif inter.selectedItem == 5:
						music.shuffle()
				else:
					inter.menuAction("select")
	
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