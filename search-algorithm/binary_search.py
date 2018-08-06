# Python Program for recursive binary search.

def binary_search(arr, left, right, searchValue):

    if right >= left:
        midNo = round(left + (right - left) / 2)

        if arr[midNo] == searchValue:
            return midNo
        elif arr[midNo] > searchValue:
            return binary_search(arr,left, right-1, searchValue)
        else:
            return binary_search(arr,midNo+1, right, searchValue)
    else:
        return -1

arr = [12,34,44,67,88,99,101,123,145,888]

searchValue = 888

result = binary_search(arr, 0, len(arr)-1, searchValue)
 
if result != -1:
    print ("Element is present at index %d" % result)
else:
    print ("Element is not present in array")
