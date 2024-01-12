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
start_x=ReferenceDie_x-(h/2)
start_y=ReferenceDie_y-(w/2)
print(start_x,start_y)
#BFS implementation
total_boxes=(math.ceil(WaferDiameter/h)*math.ceil(WaferDiameter/w))
print(total_boxes)

def condition(x,y):
    flag=0
    if((x>(WaferDiameter/2) or x<-(WaferDiameter/2) )and (y>(WaferDiameter/2) or y<-(WaferDiameter/2))):
        flag+=1
    if((x+h>(WaferDiameter/2) or x+h<-(WaferDiameter/2)) and (y>(WaferDiameter/2) or y<-(WaferDiameter/2))):
        flag+=1
    if((x>(WaferDiameter/2) or x<-(WaferDiameter/2)) and (y+w>(WaferDiameter/2) or y+w<-(WaferDiameter/2))):
        flag+=1
    if((x+h>(WaferDiameter/2) or x+h<-(WaferDiameter/2)) and (y+w>(WaferDiameter/2) or y+w<-(WaferDiameter/2))):
        flag+=1
    if(flag==4):
        return False
    return True
    
    
def bfs(start_x,start_y):
    queue=[]
    from_reference=[]
    visted=[]
    start_x=start_x
    start_y=start_y
    print(start_x,start_y)
    from_reference.append([0,0])
    queue.append([start_x,start_y])
    res=[(0,0)]
    visted.append((start_x,start_y))
    c=0
    while(True):
        x,y=queue.pop(0)
        l1,l2=from_reference.pop(0)
        if(condition(x,y)==False):
            visted.remove((x,y))
            res.remove((l1,l2))
            break
        if((x+h,y) not in visted):
            queue.append([x+h,y])
            from_reference.append([l1+1,l2])
            res.append((l1+1,l2))
            visted.append((x+h,y))
        if((x-h,y) not in visted):
            queue.append([x-h,y])
            from_reference.append([l1-1,l2])
            res.append((l1-1,l2))
            visted.append((x-h,y))
        if((x,y+w) not in visted):
            queue.append([x,y+w])
            from_reference.append([l1,l2+1])
            res.append((l1,l2+1))
            visted.append((x,y+w))
        if((x,y-w) not in visted):
            queue.append([x,y-w])
            from_reference.append([l1,l2-1])
            res.append((l1,l2-1))
            visted.append((x,y-w))
        if((x+h,y+w) not in visted):
            queue.append([x+h,y+w])
            from_reference.append([l1+1,l2+1])
            res.append((l1+1,l2+1))
            visted.append((x+h,y+w))
        if((x+h,y-w) not in visted):
            queue.append([x+h,y-w])
            from_reference.append([l1+1,l2-1])
            res.append((l1+1,l2-1))
            visted.append((x+h,y-w))
        if((x-h,y-w) not in visted):
            queue.append([x-h,y-w])
            from_reference.append([l1-1,l2-1])
            res.append((l1-1,l2-1))
            visted.append((x-h,y-w))
        if((x-h,y+w) not in visted):
            queue.append([x-h,y+w])
            from_reference.append([l1-1,l2+1])
            res.append((l1-1,l2+1))
            visted.append((x-h,y+w))
        c+=1
    return res,visted



resultant,visted=bfs(start_x,start_y)
result=[]
for i in range(len(resultant)):
    s=str(resultant[i]).replace(' ', '')+":"+str(visted[i]).replace(' ','')
    result.append(s)
print(result)
#writing in file
with open('milestone2_output3.txt', 'w') as f:
    for i in result:
        f.write(i)
        f.write('\n')
