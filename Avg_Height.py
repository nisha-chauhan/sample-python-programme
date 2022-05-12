# Students_height=input("Enter Students height in cm saprated with space:\n").split()
# for n in range(0,len(Students_height)):
#     Students_height[n]=int(Students_height[n])
# print(Students_height)
# # print(type(Students_height))
# # print(len(Students_height))'
# total_height=0
# for height in Students_height:
#     total_height+=height
# print(total_height) 
# total_student=0
# # for student in total_height:
# #     total_student+=1
# # print(total_student)
# for student in Students_height:
#     total_student+=1
# print(total_student)


Student_height=input("Enter the Height Of Student's in Cm Saprated with coma\n").split()
l=len(Student_height)
print(l)
print(type(Student_height))

# Height=int(Student_height).split()
for i in range(len(Student_height)):#total lenght of list
    Student_height[i]=int(Student_height[i])# we converted list iten in to string
print(Student_height)   # print(type(Student_height[i]))
total_number_of_student=0
for total_student in Student_height:
    total_number_of_student+=1
print(total_number_of_student) #increasing index no.
total_of_height=0
for height in Student_height:
    total_of_height+=height
print(total_of_height)    
average=total_of_height/total_number_of_student
print(average)  