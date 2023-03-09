arr=[1,34,65,24,-23,100,3,45,96,-76]

def BinarySearch(arr,k,l,h):
    
    if h>=l:
        mid=(l+h)//2
        if arr[mid]==k:
            return 1
        elif k>arr[mid]:
            
            return BinarySearch(arr,k,mid+1,h)
        else:
            
            return BinarySearch(arr,k,l,mid-1)
    else:
        return -1


#search 65
print(BinarySearch(arr,65,0,len(arr)))

#search 30 which is not present
print(BinarySearch(arr,30,0,len(arr)))

