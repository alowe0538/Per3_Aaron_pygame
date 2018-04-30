import pygame as pg

def get_brightness(hour):
    """
    Sets the brightness based off of the hour of the day in military time.
    """

    if not hour.isinstance(Integer):
        raise TypeError("the specified hour is not an int");
    hour %= 24
    hour += 1

    SUNRISE = 6
    SUNSET = 20

    return (0, 0, 255 / hour)


pg.init()

screen = pg.display.set_mode((500, 500))
running = True

while running:
    event = pg.event.poll()
    if event.type == pg.QUIT:
        running = False

        # clear the screen
        screen.fill(get_brightness(6))
        pg.display.flip()

