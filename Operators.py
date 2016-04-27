#!/usr/bin/env python

from Fluents import Fluents
from HerbEnv import HerbEnv
import time
import openravepy
import numpy as np
#from herbpy import herbpy

print "INSIDE OPERATOR"

class Operators(object):
    def __init__(self,object_id):
        
        #self.env=HerbEnv()
        #self.robot=env.robot
        self.fluents=Fluents()
        #self.obj_list=env.obj_list

        #self.object_loc = object_id.GetTransform()[:,3]
        #self.tray_loc = env.target_tray.GetTransform()


    def Pick(self,object_id,object_loc):
        if (self.fluents.Holding()==None) and (self.fluents.In(object_id,object_loc)==True) and (self.fluents.ClearX([object_id])==True):
            robot.Grasp(object_id,manip = robot.right_arm)
            print "A has been moved" + str(object_id)
        else:
            print False

    def Place(self,object_id,goal_loc):

        if (Fluents.Holding()==object_id) and (Fluents.ClearX([object_id])==True):
            #robot.place(object_id,goal_loc,manip = robot.right_arm)
            print "A has been placed" + str(object_id)
        else:
            print False