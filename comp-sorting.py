#code
from functools import cmp_to_key
class pair:
    def __init__(self,val,freq,idx):
        self.val = val
        self.freq = freq
        self.idx = idx
        
    def __repr__(self):
        return {'val':self.val,'freq':self.freq, 'idx':self.idx}
        
        
            
    def com(t1,t2):
        if t1.freq != t2.freq:
            return t2.freq - t1.freq
        if t1.val!=t2.val:
            
            return t1.val - t2.val
        return t1.idx - t2.idx
    
T = int(input())
for t in range(T):
    
    n = int(input())
    a = list(map(int,input().split()))
    
    f = [0]*(61)
    for i in range(n):
        f[a[i]] += 1
    v = []
    #print(f)
    for i in range(n):
        t = pair(a[i],f[a[i]],i)
        v.append(t)

    ans = sorted(v,key=cmp_to_key(pair.com))
    for i in ans:
        print(i.val, end =" ")
    print()
