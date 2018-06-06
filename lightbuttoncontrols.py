from gpiozero import Button, LED
from time import sleep
 
left_thruster=Button(12)
main_thruster=Button(13)
right_thruster=Button(19)
lose=LED(20)
win=LED(21)
right_light=LED(26)
middle_light=LED(22)
left_light=LED(27)
 
def main_thruster_activated():
    if main_thruster.is_pressed:
        middle_light.on()
    else:
        middle_light.off()  
    return main_thruster.is_pressed
 
def left_thruster_activated():
    if left_thruster.is_pressed:
        left_light.on()
    else:
        left_light.off()
    return left_thruster.is_pressed
 
def right_thruster_activated():
    if right_thruster.is_pressed:
        right_light.on()
    else:
        right_light.off()
    return right_thruster.is_pressed
 
def crashed():
    lose.on()
    sleep(3)
    lose.off()
   
def landed():
    win.on()
    sleep(3)
    win.off()
