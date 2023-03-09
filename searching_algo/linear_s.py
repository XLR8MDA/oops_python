arr=[1,34,65,24,-23,100,3,45,96,-76]

def linear_search(arr,k):
    bool=False
    for i in arr:
        if i == k:
            bool=True
            return('1')
    if bool == False :
        return 0
            


#search for 34
print(linear_search(arr,34))

#search for 80
print(linear_search(arr,80))

