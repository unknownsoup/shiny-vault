# Handles trading errors and retries 
import time
from random import randint

import nxbt
from nxbt import PRO_CONTROLLER
from nxbt import Buttons
from nxbt import Sticks

"""
FIRST GOAL: Go from 'Change Grip/Order screen to Enter Trade Code'


B 
B              
stick up
stick left
stick left
A              Select Game
A              Select User
23 s  seconds to start screen
A
26 s  seconds to to load game
X              Open main menu
stick right    Go over to from party pokemon to menu
stick down     Go down to Poke Portal
stick down
stick down
A              Select poke portal
2 second delay
stick down     Go down to link trade
stick down
A              Select link trade
stick down     begin searching -> set link code
A              SET LINK CODE SCREEN


"""

wait = 1

def pressA():
    try: 
        nx.press_buttons(index, [nxbt.Buttons.A])
        time.sleep(wait)
    except Exception:
        print(f"Press Buttons Error: {Exception}")
    else:
        print("Pressed A button")

def pressB():
    try: 
        nx.press_buttons(index, [nxbt.Buttons.B])
        time.sleep(wait)
    except Exception:
        print(f"Press Buttons Error: {Exception}")
    else:
        print("Pressed B button")

def pressX():
    try: 
        nx.press_buttons(index, [nxbt.Buttons.X])
        time.sleep(wait)
    except Exception:
        print(f"Press Buttons Error: {Exception}")
    else:
        print("Pressed X button")

def pressY():
    try: 
        nx.press_buttons(index, [nxbt.Buttons.Y])
        time.sleep(wait)
    except Exception:
        print(f"Press Buttons Error: {Exception}")
    else:
        print("Pressed Y button")

def directionUP():
    try: 
        nx.press_buttons(index, [nxbt.Buttons.DPAD_UP])
        time.sleep(wait)
    except Exception:
        print(f"Press Buttons Error: {Exception}")
    else:
        print("Pressed UP button")

def directionDOWN():
    try: 
        nx.press_buttons(index, [nxbt.Buttons.DPAD_DOWN])
        time.sleep(wait)
    except Exception:
        print(f"Press Buttons Error: {Exception}")
    else:
        print("Pressed DOWN button")

def directionLEFT():
    try: 
        nx.press_buttons(index, [nxbt.Buttons.DPAD_LEFT])
        time.sleep(wait)
    except Exception:
        print(f"Press Buttons Error: {Exception}")
    else:
        print("Pressed LEFT button")

def directionRIGHT():
    try: 
        nx.press_buttons(index, [nxbt.Buttons.DPAD_RIGHT])
        time.sleep(wait)
    except Exception:
        print(f"Press Buttons Error: {Exception}")
    else:
        print("Pressed RIGHT button")


def random_colour():
    return [randint(0, 255),randint(0, 255),randint(0, 255),]

def changegrip_to_setlinkcode():
    pressB()
    pressB()
    directionUP()
    directionLEFT()
    directionLEFT()
    pressA()
    pressA()
    time.sleep(23)
    pressA()
    time.sleep(30)
    pressX()
    directionRIGHT()
    directionDOWN()
    directionDOWN()
    directionDOWN()
    pressA()
    time.sleep(2)
    directionDOWN()
    directionDOWN()
    pressA()
    directionDOWN()
    pressA()
    print("SUCCESS... now exiting")


def link_code_digit(digit):
    if digit == 1:
        pressA()
    if digit == 2:
        directionRIGHT()
        pressA()
        directionLEFT()
    if digit == 3:
        directionRIGHT()
        directionRIGHT()
        pressA()
        directionLEFT()
        directionLEFT()
    

# Start the NXBT service
try: 
    nx = nxbt.Nxbt()
except Exception:
    print(f"Error initializing Nxbt: {Exception}")
else:
    print("Nxbt initialized successfully")


try: 
    index = nx.create_controller(PRO_CONTROLLER)
except Exception:
    print("Couldn't create controller")
else:
    print("Controller created!")

try: 
    nx.wait_for_connection(index)
except Exception:
    print("Couldn't connect controller")
else:
    print("Controller connected!")

changegrip_to_setlinkcode()