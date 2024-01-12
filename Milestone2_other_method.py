import math                                            
import numpy as np
#reading input data
input_file=open('Milestone2\Input\Testcase3.txt','r')
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
    if x+w<(WaferDiameter/2) and (math.dist([0,0],[x+w,y])<=(WaferDiameter/2)) and [x+w,y] not in visted:
        queue.append([x+w,y])
        visted.append([x+w,y])
    if x-w>=(-1*WaferDiameter/2)and (math.dist([0,0],[x-w,y])<=(WaferDiameter/2)) and [x-w,y] not in visted:
        queue.append([x-w,y])
        visted.append([x-w,y])
    if y+h<(WaferDiameter/2) and (math.dist([0,0],[x,y+h])<=(WaferDiameter/2)) and [x,y+h] not in visted:
        queue.append([x,y+h])
        visted.append([x,y+h])
    if y-h>=(-1*WaferDiameter/2) and (math.dist([0,0],[x,y-h])<=(WaferDiameter/2))and [x,y-h] not in visted:
        queue.append([x,y-h])
        visted.append([x,y-h])
output_file = open ('MileStone2_Output_test_case3.txt', 'w')
temp=[]
for i in visted:
    if i[0]>=0 and i[1]>=0:
        pass
    else:
        if i[0]<0 and i[1]>=0:
            if i[0]-w>(WaferDiameter/2):
                temp.append([i[0]-w,i[1]])
        elif i[0]<0 and i[1]<0:
            if i[0]-w>(WaferDiameter/2) and i[1]-h>((WaferDiameter/2)):
                temp.append([i[0]-w,i[1]-h])
            elif i[0]-w>(WaferDiameter/2) :
                temp.append([i[0]-w,i[1]])
            else:
                temp.append([i[0],i[1]-h])
        else:
            if i[1]-h>((WaferDiameter/2)):
                temp.append([i[0],i[1]-h])
print(temp)
for i in temp:
    if i not in visted:
        visted.append(i)
print(visted)
print(len(visted))
for i in visted:
    output_file.write(("("+str(i[0]//h)+','+str(i[1]//w)+")"+':'+"("+str(i[0])+','+str(i[1])+")"))
    output_file.write('\n')
output_file.close()
