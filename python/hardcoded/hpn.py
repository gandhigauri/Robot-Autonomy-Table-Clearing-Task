from Goal_states import Goal_states
import time

def HPN():
        if goal.In(a,robot) is True:
                print "Object is in storage!!"
                
        print "\nGOAL: Object should be in [3,5] \n"
        print "\n SUB-GOAL: checking if Object clean ...\n\n"
        if goal.wash(a) == 1:
                print("A is clean!!")
        else:
                T = goal.place(a,washer_loc)
                print_board1()
                goal.Pick(a,robot)
                time.sleep(5)
                print_board2()
                time.sleep(8)
                print ("\n\n Placing Object in the storage")
                print_board3()
                time.sleep(5)
                
        print "\n\nSUCCESSFULLY PLACED\n"       
        
        
def print_board3():
        
        for row3 in range(7):
                grid3.append([])  
                for col3 in range(7):
                        #if row2 == 5 and col2 == 1:
                                #grid1[row1].append('\033[91mO\033[0m')
                               
                        if row3 == 3 and col3 == 5:
                                grid3[row3].append('\033[91mO\033[0m') 
                               
                        elif row3 == 3 and col3 == 4:
                                grid3[row3].append('\033[92mR\033[0m') 
                                
                        elif row3 == 5 and col3 ==5:
                                grid3[row3].append('\033[94mW\033[0m')                       
                       
                        else:
                                grid3[row3].append('x')         
        
        for row3 in grid3:
                print "  ".join(row3)              

         

def print_board2():
        
        for row2 in range(7):
                grid2.append([])  
                for col2 in range(7):
                        #if row2 == 5 and col2 == 1:
                                #grid1[row1].append('\033[91mO\033[0m')
                               
                        if row2 == 5 and col2 == 5:
                                grid2[row2].append('\033[91mO\033[0m') 
                               
                        elif row2 == 3 and col2 == 5:
                                grid2[row2].append('\033[93mS\033[0m') 
                                
                        elif row2 == 5 and col2 ==4:
                                grid2[row2].append('\033[92mR\033[0m')                       
                       
                        else:
                                grid2[row2].append('x')         
        
        for row2 in grid2:
                print "  ".join(row2)              




                
def print_board1():
        
        for row1 in range(7):
                grid1.append([])  
                for col1 in range(7):
                        if row1 == 1 and col1 == 1:
                                grid1[row1].append('\033[91mO\033[0m')
                               
                        elif row1 == 5 and col1 == 5:
                                grid1[row1].append('\033[94mW\033[0m') 
                               
                        elif row1 == 3 and col1 == 5:
                                grid1[row1].append('\033[93mS\033[0m') 
                                
                        elif row1 == 2 and col1 ==1:
                                grid1[row1].append('\033[92mR\033[0m')                       
                       
                        else:
                                grid1[row1].append('x')         
        
        for row1 in grid1:
                print "  ".join(row1)              


def print_board():
        
        for row in range(7):
                grid.append([])  
                for col in range(7):
                        if row == 1 and col == 1:
                                grid[row].append('\033[91mO\033[0m')
                               
                        elif row == 5 and col == 5:
                                grid[row].append('\033[94mW\033[0m') 
                               
                        elif row == 3 and col == 5:
                                grid[row].append('\033[93mS\033[0m') 
                                
                        elif row == 6 and col ==0:
                                grid[row].append('\033[92mR\033[0m')                       
                       
                        else:
                                grid[row].append('x')         
        
        for row in grid:
                print "  ".join(row)              
                                        
def main():
        
                               
        print "\nThe object is in ", robot, "\n\n"
        print_board()   
        time.sleep(4)
        HPN()                
 
if __name__ == "__main__":
        grid = []
        grid1 = []
        grid2 = []
        grid3 = []
        c = 6
        d = 0
        a = "robot"
        robot = [1,1]
        goal123 = [2,7]
        washer_loc = [5,5]
        storage_loc = [3,5]
        goal = Goal_states("bling")
        main()
