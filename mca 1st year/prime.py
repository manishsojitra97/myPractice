
# try :
n = int(input("enter the num :"))
#    if n<= 0:
#       print ("enter valid positive int")
# except:
list = []
for i in range(2,n):

    for j in range (2,i):
        if i% j == 0 :
            break
    else:
            list.append(i)
print(list)             