#!/usr/bin/env python

from collections import deque
from Fluents import Fluents
from Operators import Operators
from HerbEnv import HerbEnv

print "INSIDE PLANNER"
class Planner(object):

    def __init__(self, planning_env,object_list):
        self.planning_env = planning_env
        self.list = object_list
        print "obj list" + str(object_list)

    def Plan(self,object_list):
    	
        goal_loc= self.planning_env.target_tray.GetTransform()
        print "goal:" + str(goal_loc)
        
        while(self.list):
            for i in range(len(self.list)):
                start_loc = self.list[i].GetTransform()
                if Operators.Pick(self.list[i], start_loc) == True:
                    Operators.Place(self.list[i],goal_loc)
                    del self.list[i]
                else: 
                    i = i+1

print "End of planner"


def main():
  robo = HerbEnv()
  obj_list = robo.openrave_init.obj_list
  plan123 = Planner(robo,obj_list)
  plan123.Plan(obj_list)
  print "**************HERB***********************"
  time.sleep(10000)

if __name__ == '__main__':
  main()