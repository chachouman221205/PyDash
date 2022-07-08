import pygame as pg

window = pg.display.set_mode((100, 100))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
