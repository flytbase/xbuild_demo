from api_library import DroneController
import time

droneHandle = DroneController('84d440b0ba95c19ccd8e56a2cf0e540694798850', 'r6nRDos0')

print "demo"

# print "takeoff"
# print droneHandle.take_off(2.0)
#
# print "sleeping"
# time.sleep(4.0)

print "land"
print droneHandle.land(True)

# print droneHandle.position_hold()
# print droneHandle.position_set_global(37.429353, -122.083684, 5.0, 0.0, 1.0, False, False)
# print droneHandle.velocity_set(0.0, 0.0, 0.0)
# print droneHandle.rtl()
# print droneHandle.get_global_position()
# print droneHandle.get_battery_status()
# print droneHandle.get_local_position()