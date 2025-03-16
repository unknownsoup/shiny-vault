# Handles trading errors and retries 
import nxbt

# Start the NXBT service
nx = nxbt.Nxbt()

# Get a list of all previously connected Switches and pass it as a reconnect_address argument
controller_index = nx.create_controller(
    nxbt.PRO_CONTROLLER,
    reconnect_address=nx.get_switch_addresses())
nx.wait_for_connection(controller_index)

# Press the B button
# press_buttons defaults to pressing a button for 0.1s and releasing for 0.1s
nx.press_buttons(controller_index, [nxbt.Buttons.B])

# Pressing the B button for 1.0s instead of 0.1s
nx.press_buttons(controller_index, [nxbt.Buttons.B], down=1.0)

# This frees up the adapter that was in use by this controller
nx.remove_controller(controller_index)