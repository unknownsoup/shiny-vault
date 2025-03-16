# Handles trading errors and retries 
try: 
    import nxbt
except ImportError:
    print("nxbt module not found.")

# Start the NXBT service
try: 
    nx = nxbt.Nxbt()
except Exception:
    print("Failed to start NXBT service.")
else:
    print("NXBT service started.")
    
# Get a list of all previously connected Switches and pass it as a reconnect_address argument
controller_index = nx.create_controller(
    nxbt.PRO_CONTROLLER,
    reconnect_address=nx.get_switch_addresses())
try: 
    nx.wait_for_connection(controller_index)
except OSError:
    print(f"Connection OSError: {OSError}")
except Exception as e:
    print(f"Connection Error: {e}")

# Press the B button
# press_buttons defaults to pressing a button for 0.1s and releasing for 0.1s
nx.press_buttons(controller_index, [nxbt.Buttons.B])

# Pressing the B button for 1.0s instead of 0.1s
nx.press_buttons(controller_index, [nxbt.Buttons.B], down=1.0)

# This frees up the adapter that was in use by this controller
nx.remove_controller(controller_index)