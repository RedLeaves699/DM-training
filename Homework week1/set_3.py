# -*- encoding: utf-8 -*-
def powSet(S):
    lis=[]
    for tt in S:
        lis.append(tt)
    ans=set([]);n=len(S)
    #请在此区域内编程
    for i in range(0,2**n):
        ti=i;cnt=0;LL=[]
        while ti>0:
            if ti&1:
                LL.append(lis[cnt])
            cnt+=1
            ti>>=1
        ans.add(frozenset(LL))
        LL=[]
    #请在此区域内编程
    return ans

if __name__=="__main__":
    s={1,2}
    print(powSet(s))