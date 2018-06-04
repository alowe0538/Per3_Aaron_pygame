import sys
import pyaudio
import array
from random import *
import pygame
from pygame import *
from math import *
from lightbuttoncontrols import *

init()  # the pygame module

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

clock = time.Clock()
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

BLACK = (0, 0, 0)

BLANK_MSG = ''
LANDED_MSG = 'LANDING'
CRASH_MSG = 'CRASH'

o = 100
crashed = False
INITIAL_FUEL = 400
n = 255
z = 10
Z = INITIAL_FUEL - z
mh = INITIAL_FUEL / 20
w = (n, n, n)
lp = 14
pl = 20
f = INITIAL_FUEL
ph = randint(0, INITIAL_FUEL)
am = INITIAL_FUEL / 5
fs = INITIAL_FUEL / 32
cl = cr = BLACK
ss = BLANK_MSG
y = z
T = 11025
x = randint(z, Z)
u = v = 0
r = 5
cg = w
wi = n
q = 127
p = -q
game_status = BLANK_MSG
key.set_repeat(o)
P = 0.01
pygame.font.init()
status_font = pygame.font.SysFont('courier', 20)
N = n * 4
mn = 40
st = array.array('b', (max(p, min(q, int(T * sin(i * P)))) for i in range(N))).tostring()
se = array.array('b', (randint(p, q) for i in range(N))).tostring()
mx = []
my = []
a = 2
for i in range(mn + 1):
    mx.append(z * i)
    my.append(int(randint(-mh, 0) + am * (4 - sin((i + ph) / 5.))) - fs)
mx.append(INITIAL_FUEL)
my.append(randint(INITIAL_FUEL - mh, INITIAL_FUEL))
mx[pl] = mx[pl - 1] + lp
my[pl] = my[pl - 1]
while not crashed:
    for event in pygame.event.get():
        if event.type == QUIT:
            crashed = True
    if main_thruster_activated() and f > 0:
        v -= a
        f -= 5
        cl = w
        cr = w
        ss = se
    if left_thruster_activated() and f > 0:
        u = u + a
        f = f - 5
        cl = w
        ss = se
    if right_thruster_activated() and f > 0:
        u = u - a
        f = f - 5
        cr = w
        ss = se
    if game_status == BLANK_MSG and (x < 0 or x > INITIAL_FUEL):
        x = x - (abs(x) / x) * INITIAL_FUEL
    if game_status == BLANK_MSG:
        v = v + 1
        x = (10 * x + u) / 10
        y = (10 * y + v) / 10
    if (y + 8) >= my[pl] and x > mx[pl - 1] and x < mx[pl] and v < 30:
        game_status = LANDED_MSG
        landed()
    for i in range(mn):
        if game_status == BLANK_MSG and mx[i] <= x and mx[i + 1] >= x and (my[i] <= y or my[i + 1] <= y):
            cr = 1
            cg = BLACK
            game_status = CRASH_MSG
            crashed()
    screen.fill(BLACK)
    draw.line(screen, w, (mx[pl - 1], my[pl - 1]), (mx[pl], my[pl]), 3)
    if wi > 10 and game_status == CRASH_MSG:
        r = r + z
        wi = wi - z
        ss = st
    for i in range(50):
        ax = sin(i / 8.)
        ay = cos(i / 8.)
        draw.line(screen, (wi, wi, wi), (x + r * ax, y + r * ay), (x + r * ax, y + r * ay))
    draw.line(screen, cg, (x + 3, y + 3), (x + 4, y + 6))
    draw.line(screen, cg, (x - 3, y + 3), (x - 4, y + 6))
    draw.line(screen, cl, (x + 2, y + 5), (x, y + 9))
    draw.line(screen, cr, (x - 2, y + 5), (x, y + 9))
    txt = 'FUEL %3d     ALT %3d     VERT SPD %3d     HORZ SPD %3d' % (f, INITIAL_FUEL - y, v, u)
    sp = status_font.render(txt, 0, w)
    screen.blit(sp, (0, INITIAL_FUEL - 12))
    cl = BLACK
    cr = BLACK
    for i in range(mn):
        draw.line(screen, w, (mx[i], my[i]), (mx[i + 1], my[i + 1]))
    sp = status_font.render(game_status, 0, w)
    screen.blit(sp, (INITIAL_FUEL / 3, INITIAL_FUEL / 2))
    display.flip()
    clock.tick(5)
    ss = BLANK_MSG
pygame.quit()
stream.close()
