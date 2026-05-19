def trapping_rain_water(arr,height):
    if height<1:
        return 0
    n=len(arr)
    left=[0]*n
    right=[0]*n
    left[0]=arr[0]
    for i in range(1,n):
        left[i]=max(left[i-1],arr[i])
    right[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        right[i]=max(right[i+1],arr[i])
    for i in range(n):
        arr[i]=min(left[i],right[i])-arr[i]
    return sum(arr) 
print(trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1],6))
    
    
    
#########################################################




def trapping_rain_water(arr,height):
    n=len(arr)
    left=[0]*n
    right=[0]*n
    left[0]=arr[0]
    for i in range(1,n):
        left_height=max(left[i],arr[i])
    for i in range(n-2,-1,-1):
        right_height=max(right[i],arr[i])
    for i in range(n):
        res=min(left_height,right_height)-arr[i]
    return res
print(trapping_rain_water(arr=[0,1,0,2,0,0,3,2,0,0,3,2,1,0,1],height=6))   
        
        