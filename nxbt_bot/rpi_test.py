# Handles trading errors and retries 
import time

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

def BOT_changegrip_to_setlinkcode():
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


def navigate(row, col):
            if row < 0:
                for i in range(abs(row)):
                    directionDOWN()
            elif row > 0:
                for i in range(row):
                    directionUP()

            if col < 0:
                for i in range(abs(col)):
                    directionRIGHT()
            elif col > 0:
                for i in range(col):
                    directionLEFT()


def input_linkcode(linkcode):

    pad_positions = {
        "1": (0, 0), "2": (0, 1), "3": (0, 2),
        "4": (1, 0), "5": (1, 1), "6": (1, 2),
        "7": (2, 0), "8": (2, 1), "9": (2, 2),
        "0": (3, 1)
    }
    """
    Always adjust the row first, then the column
    UNLESS the next digit is 0, then just adjust the column first
    """
    cursor_loc = (0, 0)
    for digit in linkcode:
        # get the target digit's position
        target_digit = pad_positions[digit]
        # update linkcode to remove the working digit
        linkcode = linkcode[1:]

        # Special case for digit 0
        #     Move the cursor to the column first, then the row
        if digit == "0":
            col = cursor_loc[1] - target_digit[1]
            navigate(0, col)
            row = cursor_loc[0] - target_digit[0]
            navigate(row, 0)
        else:
            # finding exacltly how many rows and columns to move
            row, col = tuple(a-b for a, b in zip(cursor_loc, target_digit))

            # navigate the cursor
            navigate(row, col)
            pressA()

        # set the current cursor location
        cursor_loc = target_digit
        
        print(f"Moving to {cursor_loc}")
    

# Start the NXBT service
def init_nxbt():
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

init_nxbt()
BOT_changegrip_to_setlinkcode()
input_linkcode("13913090") # example link code