def binarsearch(arr,left,right,x):
    if right>=left:
        mid=(left+right)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]> x:
            return binarsearch(arr,left,mid-1,x)
        else:
            return binarsearch(arr,mid+1,right,x)
    else:
        return -1




arr=[1,34,54,23,65,37,324,54,6,73,889,34,2,335,79]
arr.sort()
print(arr)
k=79


print(binarsearch(arr,0,len(arr)-1,k)+1)

