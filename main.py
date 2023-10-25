from time import time
from random import randint
import pgzrun

WIDTH = 800
HEIGHT = 600

satellites = []
lines = []

next_satellite = 0
start_time = 0
total_time = 0
end_time = 0

number_of_satellite = 8

def create_satellites():
    global start_time
    for count in range(0,number_of_satellite):
        sat = Actor("satellite")
        sat.pos = randint(40, WIDTH-40), randint(40, HEIGHT-40)
        satellites.append(sat)
    start_time = time()

def draw():
    global total_time
    screen.blit("galaxy",  (0,0))
    number = 1
    for satellite in satellites:
        screen.draw.text(str(number), (satellite.pos[0], satellite.pos[1]+20 ))
        satellite.draw()
        number = number + 1

    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))

    if next_satellite < number_of_satellite:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)), (10,10) , fontsize = 30)
    else:
        screen.draw.text(str(round(total_time,1)), (10,10) , fontsize=30)

def on_mouse_down(pos):
    global next_satellite, lines
    if next_satellite < number_of_satellite:
        if next_satellite:
            lines.append((satellites[next_satellite-1].pos, satellites[next_satellite].pos))
        next_satellite = next_satellite + 1
    else:
        lines = []
        next_satellite = 0

def update():
    pass

create_satellites()
pgzrun.go()