
class Goal_states:

        def __init__(self,washLoc,storageLoc,roboLoc, objLoc):

                #self.val = False                
                self.washer_location = washLoc  
                self.storage_location =  storageLoc
                self.robot_location = roboLoc
                self.object_location = objLoc
                self.Holding = None
                self.Clean = False
                                              
        def In(self,obj_loc,region):
                if obj_loc == region:
                        print("Robot placed in required destination")
                        return True
                else:        
                        print "robot is not in any desired location", obj_loc
                        return False 
                        
        def ClearX(self,rob_loc,obj_loc):
                rob_x=robo_loc[0]
                rob_y=robo_loc[1]
                neighbor=[[rob_x-1,rob_y-1],[rob_x-1,rob_y],[rob_x-1,rob_y+1],[rob_x,rob_y-1],[rob_x,rob_y+1],[rob_x+1,rob_y-1],[rob_x+1,rob_y],[rob_x+1,rob_y+1]]
                for element in neighbor:
                        if obj_loc == element:
                                print("found object in neighbourhood")
                                return True
                        else:        
                                print ("still wandering")
                                return False 
                                        
        def wash(self,a):
                self.a = a
                if self.val == False:
                        print "not yet cleaned---->executing wash " 
                        return False  
                        
                else:
                 return True  
                 
        def place(self,a,loc):
                self.storage = self.washer_location
                print "assigning storage loc to washer loc"
                Value = self.In(a,loc)
                if Value == False:
                        if self.Holding == "None":
                                print "Its not holding bloody anything"
                else:
                        print "YYYYYYYYAYYYYYYYYYYYYY BLOCK HAS BEEENNN PLACED"
                return                        
                                                 
                
        def Pick(self, robot, pick):
                if (pick!= self.washer_location):
                        if(self.Holding == "None"):
                                print "\n\nHolding nothing"
                                print "lets execute clear swept"
                                self.Holding = "Yes"
                                pick = self.washer_location
                                self.Pick(robot,pick)                        
                else:
                        #ClearSwept(robot,self.washer_location)
                        print "\n\nGripper is holding something"
                        self.place(robot,pick)
                return        
                 
        
        
