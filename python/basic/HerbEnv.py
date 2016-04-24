import openravepy
import numpy as np
import time
from Fluents import Fluents

openravepy.RaveInitialize(True, level=openravepy.DebugLevel.Info)
openravepy.misc.InitOpenRAVELogging()


class HerbEnv(object):

    def __init__(self):
	    self.fluent = Fluents()
	    self.openrave_init()
	
  

    def openrave_init(self):
        self.env = openravepy.Environment()
        self.env.SetViewer('qtcoin')
        self.env.GetViewer().SetName('HPN Viewer')
        #self.env.Load('models/%s.env.xml' %PACKAGE_NAME)
        # time.sleep(3) # wait for viewer to initialize. May be helpful to uncomment
        self.name = 'herb'
        self.robot = self.env.ReadRobotXMLFile('models/robots/herb2_padded.robot.xml')
        self.env.Add(self.robot)
        
        right_relaxed = [ 5.65, -1.76, -0.26,  1.96, -1.15 , 0.87, -1.43 ]
        left_relaxed = [ 0.64, -1.76,  0.26,  1.96,  1.16,  0.87,  1.43 ]
        
        right_manip = self.robot.GetManipulator('right_wam')
        self.robot.SetActiveDOFs(right_manip.GetArmIndices())
        self.robot.SetActiveDOFValues(right_relaxed)
        
        left_manip = self.robot.GetManipulator('left_wam')
        self.robot.SetActiveDOFs(left_manip.GetArmIndices())
        self.robot.SetActiveDOFValues(left_relaxed)
        
        self.manip = right_manip
        self.robot.SetActiveManipulator('right_wam')
        self.end_effector = self.manip.GetEndEffector()

        self.robot.SetActiveDOFs(self.manip.GetArmIndices())
    
        self.robot.controller = openravepy.RaveCreateController(self.robot.GetEnv(), 'IdealController')
        
        # add a table
        self.table = self.robot.GetEnv().ReadKinBodyXMLFile('models/data/furniture/table.kinbody.xml')
        self.robot.GetEnv().Add(self.table)
        table_pose = np.array([[ 0, 0, -1, 0.6], 
                                  [-1, 0,  0, 0], 
                                  [ 0, 1,  0, 0], 
                                  [ 0, 0,  0, 1]])
        self.table.SetTransform(table_pose)

        # set the camera
        camera_pose = np.array([[ 0.3259757 ,  0.31990565, -0.88960678,  2.84039211],
                                   [ 0.94516159, -0.0901412 ,  0.31391738, -0.87847549],
                                   [ 0.02023372, -0.9431516 , -0.33174637,  1.61502194],
                                   [ 0.        ,  0.        ,  0.        ,  1.        ]])
        self.robot.GetEnv().GetViewer().SetCamera(camera_pose)

        #add kinbodies
        #glass
        self.target_kinbody1 = self.env.ReadKinBodyURI('models/data/objects/plastic_glass.kinbody.xml')
        self.robot.GetEnv().Add(self.target_kinbody1)
        glass_pose = np.array([[ 0, 0, 0, 0.7], 
                                  [-1, 0,  1, -0.5], 
                                  [ 0, 1,  0, 0.7165], 
                                  [ 0, 0,  0, 1]])
        self.target_kinbody1.SetTransform(glass_pose)

        #bowl
        self.target_kinbody2 = self.env.ReadKinBodyURI('models/data/objects/plastic_bowl.kinbody.xml')
        self.robot.GetEnv().Add(self.target_kinbody2)
        bowl_pose = np.array([[ 0, 0, 0, 0.5], 
                                  [-1, 0,  1, -0.4], 
                                  [ 0, 1,  0, 0.7165], 
                                  [ 0, 0,  0, 1]])
        self.target_kinbody2.SetTransform(bowl_pose)

        #plate
        self.target_kinbody3 = self.env.ReadKinBodyURI('models/data/objects/plastic_plate.kinbody.xml')
        self.robot.GetEnv().Add(self.target_kinbody3)
        plate_pose = np.array([[ 0, 0, 0, 0.7], 
                                  [-1, 0,  1, -0.3], 
                                  [ 0, 1,  0, 0.7165], 
                                  [ 0, 0,  0, 1]])
        self.target_kinbody3.SetTransform(plate_pose)

        #add tray
        self.target_tray = self.env.ReadKinBodyURI('models/data/objects/wicker_tray.kinbody.xml')
        self.robot.GetEnv().Add(self.target_tray)
        tray_pose = np.array([[ 0, 1, 0, 0.6], 
                                  [1, 0,  0, 0.5], 
                                  [ 0, 0,  1, 0.7165], 
                                  [ 0, 0,  0, 1]])
        self.target_tray.SetTransform(tray_pose)
        self.fluent.In(self.target_kinbody1,[0.5,0.8,-0.6,-0.3])
        self.fluent.Overlaps(self.target_kinbody1)
        #self.fluent.Holding(self.target_tray)

if __name__ == '__main__':
  robo = HerbEnv()
  time.sleep(10000)
