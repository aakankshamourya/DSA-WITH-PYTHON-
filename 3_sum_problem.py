#Brute force approach
def threeSum(arr):
    s=set()
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==0:
                    temp=sorted([arr[i],arr[j],arr[k]])
                    s.add(tuple(temp))
    return list(s)
print(threeSum([-1,0,1,2,-1,-4]))   

####################################################################

#Better approach

def ThreeSum(arr):
    my_set=set()
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            third=-(arr[i]+arr[j])
            if third in my_set:
                temp=sorted([arr[i],arr[j],third])
                my_set.add(tuple(temp))
    return [list(i) for i in my_set] 
print(ThreeSum([-1,1,0,2,-2,-1,3,-3,0]))    