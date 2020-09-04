

#print("Enter the no. of testcases.")
test = int(input())

for i in range(0, test):
    size, escape = input().split()
    
    array = []
    arr = input()
    num = arr.split(" ")

    for j in range(0, int(size)):
        w = num[j]
        array.append(w)
        
   
    suraj = (array[int(escape):] + array[0:int(escape)])
    ele = " "
    nu = ele.join(suraj)
    print(nu)




