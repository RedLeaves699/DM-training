# -*- encoding: utf-8 -*-

def dfs(ans,n,L,N,*args):
    if n==N:
        tmp=tuple(L)
        ans.add(tmp)
        return
    for i in args[0][n]:
        L.append(i)
        dfs(ans,n+1,L,N,*args)
        L.pop()

def DescartesProduct(*args):
    n=len(args[0])
    #请在此区域编程实现函数功能
    L=[];ans=set([])
    dfs(ans,0,L,n,*args)
    #请在此区域编程实现函数功能
    return ans

if __name__=="__main__":
    L=[{1,5,8},{3,6},{'j','q'}]
    print(DescartesProduct(L))