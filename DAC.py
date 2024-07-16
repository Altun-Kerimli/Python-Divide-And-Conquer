import math as mth
def rct(arr, akey = False):
    mid = mth.floor(len(arr)/2)
    key = akey
    a = []
    b = []    
    
    for i in range(0,mid):    
        a.append(arr[i])
        b.append(arr[i+mid])
        if len(arr)%2 == 1 and i == mid-1:
            b.append(arr[len(arr)-1])
    
    if len(arr) > 2 and key == False:
        a, key = rct(a, key)
        b, key = rct(b, key)
    
    if len(arr) == 1:
        return arr, True
    
    elif len(arr) == 2 or key == True:
        key = True
        for j in range(0, len(b)):            
            if a[len(a)-1] <= b[j]:
                a.append(b[j])                

            elif a[0] >= b[j]:
                a = a[::-1]
                a.append(b[j])
                a = a[::-1] 

            else:
                a.append(b[j])
                i = len(a)-1
                a[i-1],a[i] = a[i],a[i-1] 
                i-=1
                
                while i != 0:
                    if a[i] > a[i-1] and a[i] <= a[i+1]:
                        break
                    else:
                        a[i-1],a[i] = a[i],a[i-1] 
                        i-=1    
        return a, key
    
ret = [78,12,89,34,2,789,1,3,5,12,555, 6]

print(rct(ret)[0])