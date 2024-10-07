def arrop(arr):
    print("menu")
    print("1= smallest, 2 = largest, 3= sum, 4= average , select ur option :  ")

    option = int(input ("enter ur option :  "))

    if option == 1:
        return min(arr)
    elif option ==2:
        return max(arr)
    elif option== 3:
        return sum(arr)
    elif option ==4:
        return sum(arr)/len(arr)
    else :
        return ("plese select option from given vbalues ")
        
arr1 = list(map(int, input("enter the array :  ").split()))

print(arrop(arr1))



