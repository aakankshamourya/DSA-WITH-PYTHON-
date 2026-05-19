def search_in_sorted_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = left + (right - left) // 2
        mid_value = matrix[mid // cols][mid % cols]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
print(search_in_sorted_matrix([[1, 3, 5, 7],
                              [10, 11, 16, 20], 
                              [23, 30, 34, 60]], 3))    



###########################################################################################################




a = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]
n = len(a)
target = 17
found = False
r,c = 0,n-1
while r<n and c>=0:
    if a[r][c] == target:
        print("at index ",r,c)
        found = True
        break
    elif a[r][c] > target:
        c-=1
    else: 
        r+=1

if found==False: print("Not there") 