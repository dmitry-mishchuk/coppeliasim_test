import os
import sys

api_dir = os.path.join(os.path.dirname(__file__), '..', 'api')
sys.path.append(api_dir)

import sim
import time
import keyboard

print ('Program started')
sim.simxFinish(-1)
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

if clientID != -1:
    print ('Connected to remote API server')
else:
    print ('Failed connecting to remote API server')

time.sleep(1)

error, visl = sim.simxGetObjectHandle(clientID,'/LineTracer/LeftSensor', sim.simx_opmode_oneshot_wait) 
error, visr = sim.simxGetObjectHandle(clientID,'/LineTracer/RightSensor', sim.simx_opmode_oneshot_wait) 
while 1: 
    if keyboard.is_pressed('esc'):
        break

    error, result_l, data_l=sim.simxReadVisionSensor(clientID,visl, sim.simx_opmode_oneshot_wait) 
    error, result_r, data_r=sim.simxReadVisionSensor(clientID,visr, sim.simx_opmode_oneshot_wait) 
    
    print(data_l[0]) 
    print(data_r[0])
    # keyboard.on_press(on_key_event)
    # keyboard.wait('esc')
    time.sleep(1)

    # if (data_l[0][11] > 0.4) and (data_r[0][11] > 0.4):
    #     error = sim.simxSetJointTargetVelocity(clientID, Left_wheel, w1, sim.simx_opmode_oneshot_wait)
    #     error = sim.simxSetJointTargetVelocity(clientID, Right_wheel, w2, sim.simx_opmode_oneshot_wait)

    # elif (data_l[0][11] < 0.4) and (data_r[0][11] > 0.4):
    #     error = sim.simxSetJointTargetVelocity(clientID, Left_wheel, 0, sim.simx_opmode_oneshot_wait)
    #     error = sim.simxSetJointTargetVelocity(clientID, Right_wheel, w2*2, sim.simx_opmode_oneshot_wait)

    # elif (data_l[0][11] > 0.4) and (data_r[0][11] < 0.4):
    #     error = sim.simxSetJointTargetVelocity(clientID, Left_wheel, w1*2, sim.simx_opmode_oneshot_wait)
    #     error = sim.simxSetJointTargetVelocity(clientID, Right_wheel, 0, sim.simx_opmode_oneshot_wait)