def binary_search(data,target,low,high):
    if low > high:
        return False
    
    mid = (low + high) // 2

    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data,target,low,mid -1)
    else:
        return binary_search(data,target, mid+1,high)


with open('test.txt','r') as file:
    data = []
    for row in file:
        #print(row.split('|')[0])
        data += [int(row.split('|')[0])]

    print(data)

    target = int(input('What idDispositivo would you like to find?'))
    found = binary_search(data, target, 0, len(data) - 1)

    print(found)