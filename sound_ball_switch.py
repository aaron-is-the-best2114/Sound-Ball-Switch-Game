from gpiozero import Button
from gpiozero import DigitalInputDevice
import time

BALL_SWITCH_PIN = 2
SOUND_SENSOR_DIGITAL_PIN = 4

ball_switch = Button(BALL_SWITCH_PIN)
sound_sensor = DigitalInputDevice(SOUND_SENSOR_DIGITAL_PIN)

ball_switch_state = False

def handle_ball_switch():
    global ball_switch_state
    ball_switch_state = not ball_switch_state
    print("Ball Switch: ", ball_switch_state)
    
ball_switch.when_pressed = handle_ball_switch

try:
    while True:
        sound_level = sound_sensor.value
        print(sound_level)
        
        if sound_level == 1 and ball_switch_state:
            print("Action Triggered")
            
        time.sleep(0.1)
        
except KeyboardInterrupt:
    pass