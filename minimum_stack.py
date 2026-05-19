def push(val):
    item=[]
    if len(item)==0:
        item.append([val,val])
    else:
        minimum=min(val,item[-1][1])
        item.append([val,minimum])
    return item
    
def pop(item):
    if len(item)==0:
        return "empty stack"
    return item[-1][1] 