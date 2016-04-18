import Fluents from Fluents
import time
class Operators:
    def __init__(self,object_id):#grid_map=[robot,object,washer,storage]
        self.fluents=Fluents()
        self.object_id=object_id
	self.object_loc = [1,1]
        self.washer_loc = [5,5]
        self.storage_loc = [3,5]
        self.robot_loc = [6,0]
	self.grid_map=[self.robot_loc, self.object_loc, self.washer_loc, self.storage_loc]
        self.washed=False
        self.grasp=False    
        
    def Wash(self,self.object_loc):
        if self.fluents.In(self.object_loc,self.washer_loc):
            print "Washing" 
            time.sleep(5)
            self.washed=True
            return self.washed
        if self.washed:
            print "Washed"
        return self.washed

    def Pick(self,self.robo_loc,self.object_loc):
        if self.fluents.Holding(self.grasp,self.object_id) and self.fluents.In()
         
