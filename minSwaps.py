def minSwap (arr, n, k) : 
    #Complete the function
    
    cnt = 0
    maxc = 0
    x = 0
    
    for i in range(n):
        if arr[i] <= k :
            x +=1
    
    for i in range(x):
        if arr[i] <= k:
            cnt += 1
    maxc = max(maxc,cnt)
    
    for j in range(x,n):
        if arr[j] <= k :
            cnt += 1
        if arr[j-x] <= k:
            cnt -= 1
        maxc = max(maxc,cnt)
    
    return (x-maxc)
