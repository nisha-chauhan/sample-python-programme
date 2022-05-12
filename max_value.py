from multiprocessing.sharedctypes import Value


Values=input("Enter the value\n").split()
# print(type(Values))
for i in range(len(Values)):
    Values[i]=int(Values[i])
# print(Values,type(Values[i]))    
highest_value=0
for i in Values:
    if i>highest_value:
        highest_value=i
print (highest_value)
