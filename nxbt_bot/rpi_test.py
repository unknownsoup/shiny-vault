# Handles trading errors and retries 
import time
from random import randint

import nxbt
from nxbt import Buttons
from nxbt import Sticks

def random_colour():
    return [randint(0, 255),randint(0, 255),randint(0, 255),]

# Start the NXBT service
try: 
    nx = nxbt.Nxbt()
except Exception:
    print(f"Error initializing Nxbt: {Exception}")
else:
    print("Nxbt initialized successfully")

# Get a list of all previously connected Switches and pass it as a reconnect_address argument
# Get a list of all available Bluetooth adapters
adapters = nx.get_available_adapters()
# Prepare a list to store the indexes of the
# created controllers.
controller_idxs = []
# Loop over all Bluetooth adapters and create
# Switch Pro Controllers
for i in range(0, len(adapters)):
    index = nx.create_controller(
        nxbt.PRO_CONTROLLER,
        adapter_path=adapters[i],
        colour_body=random_colour(),
        colour_buttons=random_colour())
    controller_idxs.append(index)

    # Select the last controller for input
    controller_idx = controller_idxs[-1]

    # Wait for the switch to connect to the controller
    nx.wait_for_connection(controller_idx)

# Press the B button
# press_buttons defaults to pressing a button for 0.1s and releasing for 0.1s
try: 
    nx.press_buttons(controller_index, [nxbt.Buttons.A])
except Exception:
    print(f"Press Buttons Error: {Exception}")
else:
    print("Pressed A button")

time.sleep(1.0)

try: 
    nx.press_buttons(controller_index, [nxbt.Buttons.B])
except Exception:
    print(f"Press Buttons Error: {Exception}")
else:
    print("Pressed B button")

# Clears all macros from a given controller
nx.clear_macros(controller_index)