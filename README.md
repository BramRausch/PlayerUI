# PlayerUI
More info: https://hackaday.io/project/26157-pipod

## Features
* Index music from ```/Music``` folder
* Sorting by artist, album and tracks
* Control volume
* Queueing
* Shuffling the queue
* Sleep mode (Backlight off)
* Display artist name, album title and track title

## Controls
While the display is awake:

| Key   | Function                         |
|---|---|
| Up    | Go up one item                   |
| Down  | Go down one item                 |
| Left  | Back                             |
| Right | <b>On music info screen:</b> go to menu |
| Enter | Select item                      |

While the display is asleep:

| Key   | Function                                        |
|---|-----------------------------------------------------|
| Up    | Volume up                                       |
| Down  | Volume down                                     |
| Left  | Previous song                                   |
| Right | Next song                                       |
| Enter | <b>Single press:</b> play/pause, <b>double press:</b> wake up |

## Installation
1. Install git:
```sudo apt-get install git```

2. Install python 3 and pip3:
```sudo apt-get install python3 python3-pip```

3. Install pygame and eyed3 using pip3
4. clone the PlayerUI repo to you machine:
```git clone https://github.com/BramRausch/PlayerUI.git PlayerUI```

If everything went right you should be able to navigate to the PlayerUI folder and run ```__init__.py```
navigate to the PlayerUI: ```cd PlayerUI``` and run the interface: ```sudo python3 __init__.py```
