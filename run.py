#!/usr/bin/env python

import openravepy
from HerbEnv import HerbEnv
from Planner import Planner

def main(planning_env):

    raw_input('Press any key to begin planning')
    plan = Planner.Plan(planning_env,obj_list)
    
    #traj = robot.ConvertPlanToTrajectory(plan)
    #robot.ExecuteTrajectory(traj)    

if __name__ == "__main__":

    planning_env = HerbEnv()
    main(planning_env)

    import IPython
    IPython.embed()