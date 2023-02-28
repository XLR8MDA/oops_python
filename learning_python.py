
def sockMerchant(n, ar):
    # Write your code here
    dict={}
    count=0
    hi=0
    for i in ar:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
    for i in dict:
        hi=dict[i]//2
        count+=hi
        print(dict[i])
    return count

if __name__ == '__main__':
    arr=[10, 20, 20, 10, 10, 3, 50, 10 ,20]
    print(sockMerchant(9,arr))
   

 
