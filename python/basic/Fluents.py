#from DiscreteEnvironment import DiscreteEnvironment
#from SimpleEnvironment import SimpleEnvironment
class Fluents:
    def __init__(self):
	#self.sim_env = SimpleEnvironment()
	#self.discrete_env = DiscreteEnvironment(sim_env.resolution, sim_env.lower_limits, sim_env.upper_limits)
        #self.val = False                
        #self.washer_location = washLoc  
        #self.storage_location =  storageLoc
        #self.robot_location = roboLoc
        #self.object_location = objLoc
        #self.Holding = None
        #self.Clean = False
        #self.In(objLoc,washLoc)=False
                                              
    def In(self, obj_loc, region):
        if obj_loc == region:
            print("object placed in required destination")
            return True
        else:        
            print ("object is not in any desired location")
            return False 

    #def Overlaps(self,object_loc,region)
                        
    def ClearX(self,rob_loc,obj_loc):
        rob_x=robo_loc[0]
        rob_y=robo_loc[1]
        neighbor=[[rob_x-1,rob_y-1],[rob_x-1,rob_y],[rob_x-1,rob_y+1],[rob_x,rob_y-1],[rob_x,rob_y+1],[rob_x+1,rob_y-1],[rob_x+1,rob_y],[rob_x+1,rob_y+1]]
        for element in neighbor:
            if obj_loc == element:
                print("robot found object in neighbourhood")
                return True
            else:        
                print ("robot still wandering")
                return False 
                                                        
    def Holding(self,grasp,objec3t_id):
        if (grasp):
            print "holding object" object_id
            return object_id
        else:
            print("not holding anything")
            return None

    def Clean(self,washed,object_id) 
        if (washed):
            print "clean object" object_id
            return True
        else:
            print("not washed anything")
            return False
