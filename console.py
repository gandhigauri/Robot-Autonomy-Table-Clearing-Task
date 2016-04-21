#!/usr/bin/env python
"""
Provides a simple console that sets up basic functionality for 
using herbpy and openravepy.
"""
# Import user defined class

from Region import Region

import os
if os.environ.get('ROS_DISTRO', 'hydro')[0] <= 'f':
    import roslib
    roslib.load_manifest('herbpy')

import argparse, herbpy, logging, numpy, openravepy, sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='utility script for loading HerbPy')
    parser.add_argument('-s', '--sim', action='store_true',
                        help='simulation mode')
    parser.add_argument('-v', '--viewer', nargs='?', const=True,
                        help='attach a viewer of the specified type')
    parser.add_argument('--robot-xml', type=str,
                        help='robot XML file; defaults to herb_description')
    parser.add_argument('--env-xml', type=str,
                        help='environment XML file; defaults to an empty environment')
    parser.add_argument('-b', '--segway-sim', action='store_true',
                        help='simulate base')
    parser.add_argument('-p', '--perception-sim', action='store_true',
                        help='simulate perception')
    parser.add_argument('--debug', action='store_true',
                        help='enable debug logging')
    args = parser.parse_args()

    openravepy.RaveInitialize(True)
    openravepy.misc.InitOpenRAVELogging()

    if args.debug:
        openravepy.RaveSetDebugLevel(openravepy.DebugLevel.Debug)

    herbpy_args = {'sim':args.sim,
                   'attach_viewer':args.viewer,
                   'robot_xml':args.robot_xml,
                   'env_path':args.env_xml,
                   'segway_sim':args.segway_sim,
                   'perception_sim': args.perception_sim}
    if args.sim and not args.segway_sim:
        herbpy_args['segway_sim'] = args.sim
    
    env, robot = herbpy.initialize(**herbpy_args)
    
    # ADDING A TABLE 
    table_path = os.path.join('objects','table.kinbody.xml')
    table = env.ReadKinBodyXMLFile(table_path)
    table_pose = numpy.eye(4) 
    table_pose[:3,:3] = openravepy.rotationMatrixFromAxisAngle([1.20919958, 1.20919958, 1.20919958])
    table_pose[:3,3] = [0.65, 0.0, 0.0]
    table.SetTransform(table_pose)   
    env.Add(table)
    
    # CUP 1
    cup_path = os.path.join('objects', 'plastic_glass.kinbody.xml')
    cup = env.ReadKinBodyXMLFile(cup_path)
    cup_transform = numpy.eye(4)
    cup_transform[:3,3] = [0.6239455840637041, -0.4013916328109689, 0.75]
    cup.SetTransform(cup_transform)
    env.Add(cup)
    
    #CUP 2 -- currently bowl
    cup_path2 = os.path.join('objects', 'bowl.kinbody.xml')
    cup2 = env.ReadKinBodyXMLFile(cup_path2)
    cup2_transform = numpy.eye(4)
    
    # z min 0  - 0.75
    #x min = 0.3 - 1
    # y range = -0.9 - 0.9
    x = [0.3,1]
    y = [-0.9,0.9]
    z = [0, 0.75]
    cup2_transform[:3,3] = [0.4239455840637041, 0.4013916328109689, 0.75]
    cup2.SetTransform(cup2_transform)
    env.Add(cup2)
    
    #Calling fluent In
    region = Region(x[0],x[1],y[0],y[1])
    #obj_region = numpy.eye(3,1)
    obj_region = [0.4, 0.8]
    Value = region.In(obj_region)
    print ("Output of the In fluent is", Value)
    
    #IPython
    import IPython
    IPython.embed()
