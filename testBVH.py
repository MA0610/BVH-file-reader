# example.py, Aline Normoyle, 2024
from bvh import *
from bvhvisualize import *
import numpy as np
import matplotlib.pyplot as plt
import glm




animation = BVH()
animation.load("T1.bvh") #change to bvh file name
BVHAnimator(animation)


print(animation.outputJointValues(1,2))




# To visualize a single frame (range [0, animator.numFrames()-1]
# BVHVisualizeFrame(bvh, frame):