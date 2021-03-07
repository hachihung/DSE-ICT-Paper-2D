numbers = [8, 7, 6, 5, 4, 3, 2, 1]

def merge(list1, list2):
    templist = []
    while True:
        if list1[0:1] < list2[0:1]:
            if list1:
                templist.append(list1.pop(0))
            else:
                break
        else:
            if list2:
                templist.append(list2.pop(0))
            else:
                break
    if list1:
        templist = templist + list1
    if list2:
        templist = templist + list2
    return templist


def mergesort(list):
    if len(list) == 1:
        return list
    else:
        mid = len(list) // 2
        leftlist = mergesort(list[:mid])
        rightlist = mergesort(list[mid:])
        list = merge(leftlist, rightlist)
        return list

print(numbers)
print(mergesort(numbers))

