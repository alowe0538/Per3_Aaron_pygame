import pygame as pg

pg.init()

screen = pg.display.set_mode((500, 500))
running = True

while running:
    event = pg.event.poll()
    if event.type == pg.QUIT:
        running = False
