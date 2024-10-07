def updateelement(arr,index,value):
   
    if 0<=index<len(arr):
        arr[index] = value 
        return arr
    else:
        print("given index is not appropriate")

arr1= list(map(int,input("enter the array value :  ").split()))
index1 = int(input("enter the index at which u wanna change the value :"))
value1= int(input("enter the value u want to replace at given index : "))

print(updateelement(arr1,index1,value1))


def deleteelement(arr,index):
    if 0<= index<len(arr):
        arr.pop(index)
        return arr
    else :

        return "not right index"
    
arr1= list(map(int,input("enter the array value :  ").split()))
index1 = int(input("enter the index at which u wanna delete the value :"))
c = deleteelement(arr1,index1)
print(c)

