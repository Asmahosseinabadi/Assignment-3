arr= [ int(x) for x in input("Enter array values: ").split() ]
print(arr)

flag = 0
if(arr == sorted(arr)):
    flag = 1
     

if (flag) :
    print ("Yes, List is sorted.")
else :
    print ("No, List is not sorted.")