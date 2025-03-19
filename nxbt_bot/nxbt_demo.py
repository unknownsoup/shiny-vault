# Controls the Switch's trading process
import nxbt
# This prints the device paths for each available adapter.
# If a controller is in use, an adapter will be removed from this list.
nx = nxbt.Nxbt()
print(nx.get_available_adapters)
