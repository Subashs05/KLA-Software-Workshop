import math                                            
import numpy as np
#reading input data
input_file=open('Milestone2\Input\Testcase1.txt','r')
input_data=input_file.readlines()
input_dict={}
for i in input_data:
    temp=i.split(':')
    input_dict[temp[0]]=temp[1]
print(input_dict)
#creating class for die
class Die:
    def __init__(self, height, width):
        self.height = height
        self.width = width
# initializing Variables
WaferDiameter=int(input_dict['WaferDiameter'])
DieSize=input_dict['DieSize'].split('x')
DieShiftVector=input_dict['DieShiftVector'].replace('(','').replace(')','').split(',')
ReferenceDie=input_dict['ReferenceDie'].replace('(','').replace(')','').split(',')
h=int(DieSize[0])
w=int(DieSize[1])
DieShiftVector_x=int(DieShiftVector[0])
DieShiftVector_y=int(DieShiftVector[1])
ReferenceDie_x=int(ReferenceDie[0])
ReferenceDie_y=int(ReferenceDie[1])
# Trying to find angle
Die_shift_vector_Distance=math.dist([0,0],[DieShiftVector_x,DieShiftVector_y])
print("\nResult...",math.degrees(np.arcsin(0.5)))
#number_of_die= area of a sqaure of side diameter of wafer/area of each die
print(WaferDiameter)
number_of_die=(WaferDiameter**2)/(h*w)
print(number_of_die)
our_initial_point=[DieShiftVector_x,DieShiftVector_y]
print(our_initial_point)
#inplementing bfs
queue=[our_initial_point]
visted=[our_initial_point]
output_dict={}
while(queue):
    node=queue.pop(0)
    x=node[0]
    y=node[1]
    if x+w<(WaferDiameter/2)  and [x+w,y] not in visted:
        if  (math.dist([0,0],[x+w,y])<=(WaferDiameter/2)):
            queue.append([x+w,y])
            visted.append([x+w,y])
        else:
            if  (math.dist([0,0],[x,y])<=(WaferDiameter/2)) and [x,y] not in visted:
                 visted.append([x,y])
            
    if x-w>=(-1*WaferDiameter/2)and [x-w,y] not in visted:
        if (math.dist([0,0],[x-w,y])<=(WaferDiameter/2)) :
            queue.append([x-w,y])
            visted.append([x-w,y])
        else:
            if  (math.dist([0,0],[x,y])<=(WaferDiameter/2)) and [x,y] not in visted:
                 visted.append([x,y])
    if y+h<(WaferDiameter/2) and [x,y+h] not in visted:
        if (math.dist([0,0],[x,y+h])<=(WaferDiameter/2)):
            queue.append([x,y+h])
            visted.append([x,y+h])
        else:
            if  (math.dist([0,0],[x,y])<=(WaferDiameter/2)) and [x,y] not in visted:
                 visted.append([x,y])
    if y-h>=(-1*WaferDiameter/2) and [x,y-h] not in visted :
        if (math.dist([0,0],[x,y-h])<=(WaferDiameter/2)):
            queue.append([x,y-h])
            visted.append([x,y-h])
        else:
            if  (math.dist([0,0],[x,y])<=(WaferDiameter/2)) and [x,y-h] not in visted:
                 visted.append([x,y-h])
print(visted)
visted.sort()
print(len(visted))
output_file = open ('MileStone2_Output_test_case1.txt', 'w')
for i in visted:
    output_file.write(("("+str(i[0])+','+str(i[1])+")"+':'+"("+str(i[0]/30)+','+str(i[1]/30)+")"))
    output_file.write('\n')
output_file.close()
