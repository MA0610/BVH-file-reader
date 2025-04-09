# example.py, Aline Normoyle, 2024
from bvh import *
from bvhvisualize import *
import numpy as np
import matplotlib.pyplot as plt
import glm

###########
# USE THIS FOR WHAT JOINT YOU WANT

# joint_motion_map = {
#         "ROOT": [0, 5],  # Values 1 to 6
#         "torso_1": [6, 11],  # Values 7 to 12
#         "torso_2": [12, 17],  # Values 13 to 18
#         "torso_3": [18, 23],  # Values 19 to 24
#         "torso_4": [24, 29],  # Values 25 to 30
#         "torso_5": [30, 35],  # Values 31 to 36
#         "torso_6": [36, 41],  # Values 37 to 42
#         "torso_7": [42, 47],  # Values 43 to 48
#         "neck_1": [48, 53],  # Values 49 to 54
#         "neck_2": [54, 59],  # Values 55 to 60
#         "head": [60, 65],  # Values 61 to 66
#         "l_shoulder": [66, 71],  # Values 67 to 72
#         "l_up_arm": [72, 77],  # Values 73 to 78
#         "l_low_arm": [78, 83],  # Values 79 to 84
#         "l_hand": [84, 89],  # Values 85 to 90
#         "r_shoulder": [90, 95],  # Values 91 to 96
#         "r_up_arm": [96, 101],  # Values 97 to 102
#         "r_low_arm": [102, 107],  # Values 103 to 108
#         "r_hand": [108, 113],  # Values 109 to 114
#         "l_up_leg": [114, 119],  # Values 115 to 120
#         "l_low_leg": [120, 125],  # Values 120 to 125
#         "l_foot": [126, 131],  # Values 125 to 130
#         "l_toes": [132, 137],  # Values 130 to 135
#         "r_up_leg": [138, 143],  # Values 135 to 140
#         "r_low_leg": [144, 149],  # Values 140 to 145
#         "r_foot": [150, 155],  # Values 145 to 150
#         "r_toes": [156, 161],  # Values 150 to 155
#         }    

###########


animation = BVH()
animation.load("T1.bvh") #change to bvh file name
BVHAnimator(animation)


# print(animation.outputJointValues(1,2))

print(animation.outputJointValues(0,"ROOT"))



##############

#Notes
#Might want 10 make shot bvh files & 10 miss bvh files, this is at least to start out
#figure out relationship between angle between certain throw/shot/swing
#can attempt other methods later on

#

##############



# To visualize a single frame (range [0, animator.numFrames()-1]
# BVHVisualizeFrame(bvh, frame):
