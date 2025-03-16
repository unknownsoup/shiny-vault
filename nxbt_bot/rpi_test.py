# Handles trading errors and retries 
import nxbt

# Start the NXBT service
nx = nxbt.Nxbt()

# Create a Pro Controller and wait for it to connect
controller_index = nx.create_controller(nxbt.PRO_CONTROLLER)
nx.wait_for_connection(controller_index)

# Press the B button
# press_buttons defaults to pressing a button for 0.1s and releasing for 0.1s
nx.press_buttons(controller_index, [nxbt.Buttons.B])

# Pressing the B button for 1.0s instead of 0.1s
nx.press_buttons(controller_index, [nxbt.Buttons.B], down=1.0)

print("Connected")