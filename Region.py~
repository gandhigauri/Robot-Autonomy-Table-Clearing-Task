class Region:

        def __init__(self, min_x, max_x, min_y, max_y):
                self.min_x = min_x
                self.max_x = max_x
                self.min_y = min_y
                self.max_y = max_y
                self.obj = [0]*2
                
        def In(self,obj):
                self.obj = obj
                if obj[0] > self.min_x:
                        if obj[0]< self.max_x:
                                if obj[1]>self.min_y:
                                        if obj[1]<self.max_y:
                                        
                                                print("\n Object is on table")
                                                return True
                print("*********Object is not on the table**************")
                return False                                         
