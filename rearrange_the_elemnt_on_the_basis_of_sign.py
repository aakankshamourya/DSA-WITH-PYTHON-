def rearrange_sign(arr):
    negatives = []
    positives = []
    for x in arr:
        if x < 0:
            negatives.append(x)
        else:
            positives.append(x)
    return negatives + positives

print(rearrange_sign([1,-2,3,-4,5,-6]))
