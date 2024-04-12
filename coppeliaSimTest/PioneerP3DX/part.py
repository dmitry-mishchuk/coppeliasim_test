import sys
import os

api_dir = os.path.join(os.path.dirname(__file__), '..', 'api')
sys.path.append(api_dir)

import sim
import simConst
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

while True:
    error_code = sim.simxSetJointTargetVelocity(clientID, motorLeft, 0.2, sim.simx_opmode_oneshot_wait)
    error_code = sim.simxSetJointTargetVelocity(clientID, motorRight, -0.2, sim.simx_opmode_oneshot_wait)

print ('Program ended')

