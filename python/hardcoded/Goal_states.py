import time
class Goal_states:

        def __init__(self,string):

                self.val = False                
                self.washer_location = [5,5]  
                self.storage =  [3,5]
                self.Holding = "None"
                     
                
        def In(self,a,storage):
                self.a = a
                if self.a == storage:
                        print("Robot placed in required destination", self.storage)
                        return True
               # print "robot is in", storage
                return False 
                
        def wash(self,a):
                self.a = a
                if self.val == False:
                        time.sleep(4)
                        print "Object is not yet cleaned---->execute washing " 
                        return False  
                        
                else:
                 return True  
                 
        def place(self,a,loc):
                self.storage = self.washer_location
                #print "assigning storage loc to washer loc"
                Value = self.In(a,loc)
                if Value == False:
                        if self.Holding == "None":
                                print "\n\nCurrently gripper is not holding robot \n\n Robot moving to the Object's location"
                                time.sleep(5)
                else:
                        print "YYYYYYYYAYYYYYYYYYYYYY BLOCK HAS BEEENNN PLACED"
                return                        
                                                 
                
        def Pick(self, robot, pick):
                if (pick!= self.washer_location):
                        if(self.Holding == "None"):
                                #print "\n\nHolding nothing"
                                #print "lets execute clear swept"
                                self.Holding = "Yes"
                                pick = self.washer_location
                                self.Pick(robot,pick)                        
                else:
                        #ClearSwept(robot,self.washer_location)
                        print "\n\nGripper is holding robot now"
                        self.place(robot,pick)
                return        
                 
        
        
