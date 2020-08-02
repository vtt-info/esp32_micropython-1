'''
SERVO CONTROL SAMPLE THROUGH THE USE OF 4 BUTTONS (2 for each servo, on  pins 15, 4, 22 and 23)
The servos are controlled through PWM enambled pins 5 and 21
'''

import machine
import time

#button declarations:
button0 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
button1 = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
button2 = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)
button3 = machine.Pin(23, machine.Pin.IN, machine.Pin.PULL_UP)

button_list = [button0, button1, button2, button3]

#servo declarations:
servo0 = machine.PWM(machine.Pin(5), freq=50)
servo1 = machine.PWM(machine.Pin(21), freq=50)

servo_list = [servo0, servo1]

#Increments or decreases the value of both servo duties depending on which button was pressed
def servo_control(button_up0, button_down0, button_up1, button_down1, duty0, duty1):
    if is_pressed(button_up0) and duty0 < 115:
        duty0 += 1
    if is_pressed(button_down0) and duty0 > 40:
        duty0 -= 1
    if is_pressed(button_up1) and duty1 < 115:
        duty1 += 1
    if is_pressed(button_down1) and duty1 > 40:
        duty1 -= 1
    return duty0, duty1

#checks if button is pressed, returns True if button is pressed, else return False
def is_pressed(button):
    if button.value() == 0:
        return True
    else:
        return False

#Outputs the status of buttons
def check_buttons(button_list):
    for button in button_list:
        if is_pressed(button):
            print('button on ' + str(button) + 'was pressed')

#Main program loop
def loop():
    #initial value for the servos' positions
    duty0 = 77
    duty1 = 77

    while True: #This is the actual loop
        check_buttons(button_list) #This can be commented
        duty0, duty1 = servo_control(button0, button1, button2, button3, duty0, duty1)
        servo0.duty(duty0)
        servo1.duty(duty1)
        time.sleep(0.03) #This can me modified to increase/decrease the speed at which the servos rotate

#call to loop
loop()