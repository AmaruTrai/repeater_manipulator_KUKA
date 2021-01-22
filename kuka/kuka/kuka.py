
import socket
import math
import struct
import vrep 


class Vrep():
    def __init__(self, host='127.0.0.1', port=19997):
        self.host = host
        self.port = port
        self.clientID = 0
        self.joint = []

    def GetHandles(self, names=['j0', 'j1', 'j2', 'j3', 'j4', 'j5', 'ball']):
        for i in range(len(names)):
            res, j = vrep.simxGetObjectHandle(self.clientID, names[i], vrep.simx_opmode_oneshot_wait)
            self.joint.append(j)
            #print(self.joint[i])
        
    def StartSim(self):    
        print("try to connect")
        vrep.simxFinish(-1)
        self.clientID = vrep.simxStart(self.host, self.port, True, True, 5000, 5)
        return 0

    def SetAngles(self, angles):
        for i in range(len(self.joint)-3):
            res = vrep.simxSetJointPosition(self.clientID, self.joint[i], angles[i], vrep.simx_opmode_oneshot)
            print(self.joint[i])
        res = vrep.simxSetObjectPosition(self.clientID, self.joint[6], -1, (angles[6],angles[7],angles[8]), vrep.simx_opmode_oneshot)
        return 0
     

class recievedata():
    def __init__(self, port=25000, host="127.0.0.1", NoJ=4):
        self.addr = (host, port)
        print(self.addr)
        self.socket = socket.socket(family = socket.AF_INET, 
                                    type = socket.SOCK_DGRAM)
        self.socket.bind(self.addr)
        #self.NoJ = NoJ
        #for i in range(self.NoJ):
        #    self.data.append(0)
        
    def RecieveData(self):
        try:
            data, addr = self.socket.recvfrom(1024)
            data = struct.unpack('ddddddddd', data[0:72])
            print(data)
        except:
            pass
        return data

class modeling():
    def __init__(self):
        self.VREP = Vrep()
        self.RD = recievedata()
        print("nen")
        self.VREP.StartSim()
        self.VREP.GetHandles()
        

    def StartModeling(self):
        while 1:
            self.VREP.SetAngles(self.RD.RecieveData())
mod = modeling()
mod.StartModeling()
