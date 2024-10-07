#using menu

    
arr1= input("enter the array no :").split()

print("menu :")
print("1 = ascending")
print("2 =  descending")

menu = int(input("enter ur oder either 1 or 2 : "))

def sorting(arr):

   

    if menu == 1:
       return arr.sort()
    elif menu == 2:
      return arr.sort(reverse = True)
    else:
        return "not correct input"
        

  
sorting(arr1)
print(arr1)


