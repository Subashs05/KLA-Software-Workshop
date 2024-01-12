import math
input_file=open('Milestone1\Input\Testcase4.txt','r')
input_data=input_file.readlines()
input_dict={}
for i in input_data:
    temp=i.split(':')
    input_dict[temp[0]]=int(temp[1])
print(input_dict)
WaferDiameter=input_dict['WaferDiameter']
NumberofPoints=input_dict['NumberOfPoints']
Angle=input_dict['Angle']
adj=math.cos(math.radians(Angle))*(WaferDiameter/2)
opposite=math.sin(math.radians(Angle))*(WaferDiameter/2)
interval=WaferDiameter/(NumberofPoints-1)
print(interval)
k=0
end=[adj,opposite]
start=[-1*adj,-1*opposite]
output=[start]
print(start,end)
temp=-1*WaferDiameter//2
for i in range(NumberofPoints-1):
    k+=interval
    adj=math.cos(math.radians(Angle))*(temp+k)
    opposite=math.sin(math.radians(Angle))*(temp+k)
    output.append([adj,opposite])
print(output)
output_file = open ('MileStone1_Output_test_case4.txt', 'w')
for i in output:
    output_file.write(("("+str(i[0])+','+str(i[1])+")"))
    output_file.write('\n')
output_file.close()