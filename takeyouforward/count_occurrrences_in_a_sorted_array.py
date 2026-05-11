def count_occurrences_in_sorted_array(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            count=1
            left=mid-1
            while left>=0 and arr[left]==target:
                count+=1
                left-=1
            right=mid+1
            while right<len(arr) and arr[right]==target:
                count+=1
                right+=1
            return count
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return 0
print(count_occurrences_in_sorted_array([1,2,2,3,4],2))

        
        
        
def count_occurrence(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            count=1
            left=mid-1
            while left>=0 and arr[left]==target:
                count+=1
                left-=1
            right=mid+1
            while right<len(arr) and arr[right]==target:
                count+=1
                right+=1
            return count
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1  
    return 0
print(count_occurrence([1,2,2,3,4],2))