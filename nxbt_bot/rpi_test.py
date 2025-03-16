# Handles trading errors and retries 
import nxbt

# Start the NXBT service
try: 
    nx = nxbt.Nxbt()
except Exception:
    print(f"Error initializing Nxbt: {Exception}")
else:
    print("Nxbt initialized successfully")

# Get a list of all previously connected Switches and pass it as a reconnect_address argument
try: 
    controller_index = nx.create_controller(nxbt.PRO_CONTROLLER, reconnect_address=nx.get_switch_addresses())
    nx.wait_for_connection(controller_index)
except OSError:
    print(f"Connection OSError: {OSError}")
except Exception as e:
    print(f"Connection Error: {e}")
else: 
    print("Connected to Switch")

# Press the B button
# press_buttons defaults to pressing a button for 0.1s and releasing for 0.1s
try: 
    nx.press_buttons(controller_index, [nxbt.Buttons.A])
except Exception:
    print(f"Press Buttons Error: {Exception}")
else:
    print("Pressed A button")

# Pressing the B button for 1.0s instead of 0.1s
try: 
    nx.press_buttons(controller_index, [nxbt.Buttons.B])
except Exception:
    print(f"Press Buttons Error: {Exception}")
else:
    print("Pressed B button")

# This frees up the adapter that was in use by this controller
nx.remove_controller(controller_index)