from DiscreteEnvironment import DiscreteEnvironment
#from SimpleEnvironment import SimpleEnvironment
from HerbEnv import HerbEnv
class Fluents:
    ''' so we have four fluents: In, Overlaps, IsReachable, Holding
    '''
    def __init__(self):
	self.sim_env = SimpleEnvironment()
	#self.discrete_env = DiscreteEnvironment(sim_env.resolution, sim_env.lower_limits, sim_env.upper_limits)
        #self.val = False                
        #self.washer_location = washLoc  
        #self.storage_location =  storageLoc
        #self.robot_location = roboLoc
        #self.object_location = objLoc
        #self.Holding = None
        #self.Clean = False
        #self.In(objLoc,washLoc)=False
                                              
    #lek edit
    def In(self,objname,region):
        obj = self.env.GetKinBody(objname)
        pos = obj.GetTransform()[:2,3]
        if (pos[0] > self.min_x) and (pos[0]< self.max_x) and (pos[1]>self.min_y) and (pos[1]<self.max_y):
                print("\n Object is in")
                return True
        print("***Object is not in***")
        return False                                         

    def Overlaps(self,object_loc,region)
                                        
    #keech edit                
    def Holding(self):
        for b in self.env.GetBodies():
            if self.robot.IsGrabbing(b)
                return b.GetName()
            return None
            