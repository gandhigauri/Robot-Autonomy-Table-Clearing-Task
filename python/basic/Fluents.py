from DiscreteEnvironment import DiscreteEnvironment
#from SimpleEnvironment import SimpleEnvironment
#from HerbEnv import HerbEnv
class Fluents:
    ''' so we have four fluents: In, Overlaps, IsReachable, Holding
    '''
    def __init__(self):
        self.herb_env = 1

    def In(self,objname,region):
        #obj = self.env.GetKinBody(objname)
        pos = objname.GetTransform()[:2,3]
        if (pos[0] > region[0]) and (pos[0]< region[1]) and (pos[1]> region[2]) and (pos[1]< region[3]):
            print("\n Object is in")
            return True
        print("Object is not in")
        return False 

    def Overlaps(self,objname):
        obj  = objname.ComputeAABB()
        max_xyz =  obj.pos()+obj.extents()
        min_xyz =  obj.pos()-obj.extents()
        # Swept region - entire region of table, minx,max,miny,maxy
             
        print "min  ", min_xyz
        print "max  ", max_xyz                              

    def Holding(self):
        for b in self.env.GetBodies():
            if self.robot.IsGrabbing(b):
                return b.GetName()
            return None

    #def IsReachable(objname):

