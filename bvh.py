
# bvh.py, Aline Normoyle 2013

import glm, math

# Constants
M_PI_2 = math.pi * 0.5
A_EPSILON = 0.001
def clamp(x, a, b): return max(a, min(x, b))


"""
eulerAngle
Utilities for converting from euler angles to quaternion
Parameter xyz: list, or glm.vec3
   Euler angles in degrees;
   Listed in X,Y,Z order regardless of euler angle order
Returns: glm.quat
"""
def eulerAngleXYZ(xyz):
    X = glm.rotate(glm.radians(xyz[0]), glm.vec3(1,0,0))
    Y = glm.rotate(glm.radians(xyz[1]), glm.vec3(0,1,0))
    Z = glm.rotate(glm.radians(xyz[2]), glm.vec3(0,0,1))
    return glm.quat(X * Y * Z)

def eulerAngleXZY(xyz):
    X = glm.rotate(glm.radians(xyz[0]), glm.vec3(1,0,0))
    Y = glm.rotate(glm.radians(xyz[1]), glm.vec3(0,1,0))
    Z = glm.rotate(glm.radians(xyz[2]), glm.vec3(0,0,1))
    return glm.quat(X * Z * Y)

def eulerAngleYXZ(xyz):
    X = glm.rotate(glm.radians(xyz[0]), glm.vec3(1,0,0))
    Y = glm.rotate(glm.radians(xyz[1]), glm.vec3(0,1,0))
    Z = glm.rotate(glm.radians(xyz[2]), glm.vec3(0,0,1))
    return glm.quat(Y * X * Z)

def eulerAngleYZX(xyz):
    X = glm.rotate(glm.radians(xyz[0]), glm.vec3(1,0,0))
    Y = glm.rotate(glm.radians(xyz[1]), glm.vec3(0,1,0))
    Z = glm.rotate(glm.radians(xyz[2]), glm.vec3(0,0,1))
    return glm.quat(Y * Z * X)

def eulerAngleZXY(xyz):
    X = glm.rotate(glm.radians(xyz[0]), glm.vec3(1,0,0))
    Y = glm.rotate(glm.radians(xyz[1]), glm.vec3(0,1,0))
    Z = glm.rotate(glm.radians(xyz[2]), glm.vec3(0,0,1))
    return glm.quat(Z * X * Y)

def eulerAngleZYX(xyz):
    X = glm.rotate(glm.radians(xyz[0]), glm.vec3(1,0,0))
    Y = glm.rotate(glm.radians(xyz[1]), glm.vec3(0,1,0))
    Z = glm.rotate(glm.radians(xyz[2]), glm.vec3(0,0,1))
    return glm.quat(Z * Y * X)

"""
toEulerAngle
Utilities for converting from quaternion to euler angles
Parameter q: glm.quat
Returns: (rx, ry, rz) tuple representing euler angles (radians) 
"""
def toEulerAngleXYZ(q):
    M = glm.mat3(q)
    M = glm.transpose(M) # indices are reverse -> GLM is column major
    z = 0                                                               
    y = math.asin(clamp(M[0][2], -1, 1))
    x = -math.atan2(M[1][0], M[1][1])
    if y > -M_PI_2 + A_EPSILON:
       if y < M_PI_2 - A_EPSILON:
          x = math.atan2(-M[1][2], M[2][2])
          z = math.atan2(-M[0][1], M[0][0])
       else:
          x = -x
    return x, y, z

def toEulerAngleXZY(q):
    M = glm.mat3(q)
    M = glm.transpose(M) # indices are reverse -> GLM is column major
    x = -math.atan2(M[2][0], M[2][2])
    y = 0
    z = math.asin(clamp(-M[0][1], -1, 1))
    if z > -M_PI_2 + A_EPSILON:
        if z < M_PI_2 - A_EPSILON:
            x = math.atan2(M[2][1], M[1][1])
            y = math.atan2(M[0][2], M[0][0])
        else:
            x = -x
    return x, y, z

def toEulerAngleYXZ(q):
    M = glm.mat3(q)
    M = glm.transpose(M) # indices are reverse -> GLM is column major
    X = math.asin(clamp(-M[1][2], -1, 1))
    Z = 0                                                    
    Y = -math.atan2(M[0][1], M[0][0])
    if X > -M_PI_2 + A_EPSILON:
        if X < M_PI_2 - A_EPSILON:
            Y = math.atan2(M[0][2], M[2][2])
            Z = math.atan2(M[1][0], M[1][1])
        else:
            Y = -Y 
    return X, Y, Z

def toEulerAngleYZX(q):
    M = glm.mat3(q)
    M = glm.transpose(M) # indices are reverse -> GLM is column major
    Z = math.asin(clamp(M[1][0], -1, 1))
    X = 0
    Y = -math.atan2(M[2][1], M[2][2])
    if Z > -M_PI_2 + A_EPSILON:
        if Z < M_PI_2 - A_EPSILON:
            Y = math.atan2(-M[2][0], M[0][0])
            X = math.atan2(-M[1][2], M[1][1])
        else:
            Y = math.atan2(M[2][1], M[2][2])
    return X, Y, Z

def toEulerAngleZXY(q):
    M = glm.mat3(q)
    M = glm.transpose(M) # indices are reverse -> GLM is column major
    X = math.asin(clamp(M[2][1], -1, 1))
    Y = 0
    Z = -math.atan2(M[0][2], M[0][0])
    if X > -M_PI_2 + A_EPSILON:
        if X < M_PI_2 - A_EPSILON:
            Z = math.atan2(-M[0][1], M[1][1])
            Y = math.atan2(-M[2][0], M[2][2])
        else:
            Z = math.atan2(M[0][2], M[0][0])                             
    return X, Y, Z                   

def toEulerAngleZYX(q):
    M = glm.mat3(q)
    M = glm.transpose(M) # indices are reverse -> GLM is column major
    X = math.atan2(-M[0][1], -M[0][2])
    Y = math.asin(clamp(-M[2][0], -1, 1))
    Z = 0
    if Y > -M_PI_2 + A_EPSILON:
        if Y < M_PI_2 - A_EPSILON:
            Z = math.atan2(M[1][0], M[0][0])
            X = math.atan2(M[2][1], M[2][2])
        else:
            X = math.atan2(M[0][1], M[0][2])
    return X, Y, Z

def EulerToQuat(roo, xyz):
  """
  Convert from euler angles with the given rotation order to quaternion
  roo: str
     Euler Angle rotation order, e.g. "xyz"
  xyz: list, or glm.vec3 
     Euler angles (degrees)
  Returns: glm.quat 
  """
  if roo == "xyz": return eulerAngleXYZ(xyz)
  elif roo == "xzy": return eulerAngleXZY(xyz)
  elif roo == "yxz": return eulerAngleYXZ(xyz)
  elif roo == "yzx": return eulerAngleYZX(xyz)
  elif roo == "zxy": return eulerAngleZXY(xyz)
  elif roo == "zyx": return eulerAngleZYX(xyz)
  else: print("Invalid: ", roo)
  
  return glm.quat(0,0,0,0)

def QuatToEuler(roo, q):
  x = 0
  y = 0
  z = 0 
  if roo == "xyz": x, y, z = toEulerAngleXYZ(q)
  elif roo == "xzy": x, y, z = toEulerAngleXZY(q)
  elif roo == "yxz": x, y, z = toEulerAngleYXZ(q)
  elif roo == "yzx": x, y, z = toEulerAngleYZX(q)
  elif roo == "zxy": x, y, z = toEulerAngleZXY(q)
  elif roo == "zyx": x, y, z = toEulerAngleZYX(q)
  else: print("Invalid: ", roo)

  x = glm.degrees(x)
  y = glm.degrees(y)
  z = glm.degrees(z)
  return [x, y, z]

class Joint:
    def __init__(self):
        self.offset = []
        self.channels = []
        self.name = ""
        self.children = []
        self.parent = None
        self.id = 0
        self.channelvals = []
        self.rotOrder = "xyz"

    def setLocalRotQuat(self, q):
        euler = QuatToEuler(self.rotOrder, q)
        try:
           self.channelvals[self.channels.index("Xrotation")] = euler[0]
           self.channelvals[self.channels.index("Yrotation")] = euler[1]
           self.channelvals[self.channels.index("Zrotation")] = euler[2]
        except: pass

    def setLocalPos(self, pos):
        self.offset[0] = pos[0]
        self.offset[1] = pos[1]
        self.offset[2] = pos[2]

        if "Xposition" in self.channels: 
            self.channelvals[self.channels.index("Xposition")] = pos[0]
        
        if "Yposition" in self.channels: 
            self.channelvals[self.channels.index("Yposition")] = pos[1]

        if "Zposition" in self.channels: 
            self.channelvals[self.channels.index("Zposition")] = pos[2]

    def localRotQuat(self):
        rot = self.localRotEuler()
        return EulerToQuat(self.rotOrder, rot)

    def localRotEuler(self):
        rot = [0, 0, 0]
        try:
           rot[0] = self.channelvals[self.channels.index("Xrotation")]
           rot[1] = self.channelvals[self.channels.index("Yrotation")]
           rot[2] = self.channelvals[self.channels.index("Zrotation")]
        except: pass
        return rot         

    def localPos(self):
        loc = [0, 0, 0]
        try:
           loc[0] = self.channelvals[self.channels.index("Xposition")]
           loc[1] = self.channelvals[self.channels.index("Yposition")]
           loc[2] = self.channelvals[self.channels.index("Zposition")]
           return loc
        except: pass
        return self.offset

    def globalPos(self):
        listp = self.localPos()
        p = glm.vec3(listp[0], listp[1], listp[2])

        parent = self.parent
        while parent != None:
              p = parent.localRotQuat() * p + parent.localPos()
              parent = parent.parent
        return [p.x, p.y, p.z]

    def globalRot(self):
        r = self.localRotQuat()

        parent = self.parent
        while parent != None:
              r = parent.localRotQuat() * r
              parent = parent.parent
        return r

class BVH:

    def __init__(self):
        self.clear()

    def clear(self):
        self.joints = []
        self.jointMap = {}
        self.root = None
        self.frames = []
        self.frameRate = 30

    def skeletonRoot(self):
        return self.root

    def load(self, filename):
        self.clear()

        file = open(filename)
        lines = file.readlines()
        if "HIERARCHY" not in lines[0]:
           return False

        parent = None
        current = None
        motion = False

        for line in lines[1:len(lines)]:
            tokens = line.split()
            if len(tokens) == 0: # Empty line
                continue

            if tokens[0] in ["ROOT", "JOINT", "End"]:

               if current is not None:
                  parent = current

               current = Joint()
               current.name = tokens[1]

               current.id = len(self.joints)
               if current.id == 0:
                   self.root = current

               current.parent = parent
               if parent is not None:
                   current.parent.children.append(current)

               self.joints.append(current)
               self.jointMap[current.name] = current

            elif "OFFSET" in tokens[0]:
                 offset = []
                 for i in range(1,len(tokens)):
                     offset.append(float(tokens[i]))
                 current.offset = offset

            elif "CHANNELS" in tokens[0]:
                 current.channels = tokens[2:len(tokens)]
                 for i in range(len(current.channels)):
                     current.channelvals.append(0)

                 str = ""
                 chans = list(current.channels)
                 #chans.reverse() # Maya is reversed
                 for channel in chans:
                     if channel == "Xrotation": str += "x" #HERE
                     elif channel == "Yrotation": str += "y"
                     elif channel == "Zrotation": str += "z"
                 current.rotOrder = str

            elif "{" in tokens[0]:
                 pass

            elif "}" in tokens[0]:
                 current = current.parent
                 if current: 
                     parent = current.parent

            elif "MOTION" in tokens[0]:
                 motion = True

            elif "Frames:" in tokens[0]:
                 pass 

            elif "Frame" in tokens[0]:
                 self.frameRate = 1.0/float(tokens[2])

            elif motion: # Read frame data
                 vals = []
                 for token in tokens:
                     vals.append(float(token))
                 self.frames.append(vals)

        if self.numFrames() > 0:
            self.readFrame(0) # IMPORTANT! Saves pose to joints

    def save(self, filename):
        fileid = open(filename, "w")

        fileid.writelines("HIERARCHY\n")
        self.saveSkeleton(fileid, self.skeletonRoot())
        fileid.writelines("\n")
       
        fileid.writelines("MOTION\n")
        fileid.writelines("Frames: %d\n"%self.numFrames())
        fileid.writelines("Frame Time: %f\n"%(1.0/self.frameRate))

        for each in self.frames:
            for v in each:
               fileid.writelines("%.4f "%v)
            fileid.writelines("\n")

    def saveSkeleton(self, fileid, joint, indent = ""):
        line1 = "%sJOINT %s"%(indent, joint.name)
        line2 = "%s{"%(indent)
        fileid.writelines(line1+"\n")
        fileid.writelines(line2+"\n")

        x = joint.offset[0] 
        y = joint.offset[1] 
        z = joint.offset[2] 
        line1 = "\t%sOFFSET %.4f %.4f %.4f\n"%(indent, x, y, z)  #HERE
        fileid.writelines(line1)
        fileid.writelines("\t%sCHANNELS %d "%(indent, len(joint.channels)))
        for channel in joint.channels:
           fileid.writelines ("%s "%channel)
        fileid.writelines("\n")

        for eachChild in joint.children:
            self.saveSkeleton(fileid, eachChild, indent + "\t")

        line2 = "%s}"%(indent)
        fileid.writelines(line2+"\n")

    def numFrames(self):
        return len(self.frames)

    def writeFrame(self, frameNum):
        """
        Write the values currently stored in each joint to the saved frames
        """
        idx = 0
        for joint in self.joints:
            for i in range(len(joint.channels)): 
                v = joint.channelvals[i]
                self.frames[frameNum][idx] = v
                idx = idx + 1

    def readFrame(self, frameNum):
        """
        Loads the values for frameNum into each joint
        """
        idx = 0
        for joint in self.joints:
            for i in range(len(joint.channels)): 
                v = self.frames[frameNum][idx]
                joint.channelvals[i] = v  #HOW TO GET POSITION VALUES => CAN USE TO PERFORM ANALYSIS OF CERTAIN JOINTS AT CERTAIN FRAMES
                idx = idx + 1



    # def outputJointValues(self, frameNum, idx):  
    
    #     #The frameNum refers to the "row" at the bottom in the MOTION section
    #     #The idx value refers to the "column" at the bottom in the MOTION section
        
    #     return self.frames[frameNum][idx]
    




  
    
    def outputJointValues(self, frameNum, jointName):
        

        
        joint_motion_map = {
                "ROOT": [0, 5],  # Values 1 to 6
                "torso_1": [6, 11],  # Values 7 to 12
                "torso_2": [12, 17],  # Values 13 to 18
                "torso_3": [18, 23],  # Values 19 to 24
                "torso_4": [24, 29],  # Values 25 to 30
                "torso_5": [30, 35],  # Values 31 to 36
                "torso_6": [36, 41],  # Values 37 to 42
                "torso_7": [42, 47],  # Values 43 to 48
                "neck_1": [48, 53],  # Values 49 to 54
                "neck_2": [54, 59],  # Values 55 to 60
                "head": [60, 65],  # Values 61 to 66
                "l_shoulder": [66, 71],  # Values 67 to 72
                "l_up_arm": [72, 77],  # Values 73 to 78
                "l_low_arm": [78, 83],  # Values 79 to 84
                "l_hand": [84, 89],  # Values 85 to 90
                "r_shoulder": [90, 95],  # Values 91 to 96
                "r_up_arm": [96, 101],  # Values 97 to 102
                "r_low_arm": [102, 107],  # Values 103 to 108
                "r_hand": [108, 113],  # Values 109 to 114
                "l_up_leg": [114, 119],  # Values 115 to 120
                "l_low_leg": [120, 125],  # Values 120 to 125
                "l_foot": [126, 131],  # Values 125 to 130
                "l_toes": [132, 137],  # Values 130 to 135
                "r_up_leg": [138, 143],  # Values 135 to 140
                "r_low_leg": [144, 149],  # Values 140 to 145
                "r_foot": [150, 155],  # Values 145 to 150
                "r_toes": [156, 161],  # Values 150 to 155
                }  

        # Check if the joint name exists in the joint_motion_map
        if jointName not in joint_motion_map:
            raise ValueError(f"Joint name '{jointName}' not found in the hierarchy.")
        
        # Get the range of indices associated with the joint
        idx_range = joint_motion_map[jointName]
        
        #Get the values from the map
        joint_values = self.frames[frameNum][idx_range[0]:idx_range[1] + 1] 

       
        return joint_values

    def numJoints(self):
        return len(self.joints)

    def jointById(self, idx):
        return self.joints[idx]

    def jointByName(self, jointName):
        joint = self.jointMap[jointName]
        return joint
