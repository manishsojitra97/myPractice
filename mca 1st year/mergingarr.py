def merge(arr1,arr2):
    final = []
    i,j = 0,0
    while i<len(arr1)and j<len(arr2):
        if arr1[i]<arr2[j]:
            final.append(arr1[i])
            i += 1
        else:
            final.append(arr2[j])
            j +=1
  

    final.extend(arr1[i:])
    final.extend(arr2[j:])

    return final

arr3 = list(map(int,input('enter the array 1 :').split()))
arr4 = list(map(int, input('enter the array 2 :').split()))



print(merge(arr3,arr4))


        


    