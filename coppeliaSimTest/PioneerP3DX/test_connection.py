# Make sure to have the server side running in CoppeliaSim: 
# in a child script of a CoppeliaSim scene, add following command
# to be executed just once, at simulation start:
#
# simRemoteApi.start(19999)
#
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!
import os
import sys

api_dir = os.path.join(os.path.dirname(__file__), '..', 'api')

sys.path.append(api_dir)

import sim
import time

print ('Program started')

sim.simxFinish(-1)
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

if clientID != -1:
    print ('Connected to remote API server')

else:
    print ('Failed connecting to remote API server')

time.sleep(1)

error_code, motorLeft = sim.simxGetObjectHandle(clientID, './PioneerP3DX/leftMotor', sim.simx_opmode_oneshot_wait)
error_code, motorRight = sim.simxGetObjectHandle(clientID, './PioneerP3DX/rightMotor', sim.simx_opmode_oneshot_wait)

error_code = sim.simxSetJointTargetVelocity(clientID, motorLeft, 0.2, sim.simx_opmode_oneshot_wait)
error_code = sim.simxSetJointTargetVelocity(clientID, motorRight, -0.2, sim.simx_opmode_oneshot_wait)

print ('Program ended')
