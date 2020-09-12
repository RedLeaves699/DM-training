# -*- encoding: utf-8 -*-
from random import *
from time import clock


#第一题
def dfs(cost,x,y,m,n):
    if x==m and y==n:
        return cost[x][y]
    tx=x+1;ty=y
    minn=99999999999999999999;a=minn;b=minn
    if 0<=tx and tx<=m and 0<=ty and ty<=n:
        a=dfs(cost,tx,ty,m,n)
    tx=x;ty=y+1
    if 0<=tx and tx<=m and 0<=ty and ty<=n:
        b=dfs(cost,tx,ty,m,n)
    return min(a,b)+cost[x][y]
    
def minPathCost(cost, i, j):
    # 请在下面编写代码
    return dfs(cost,0,0,i,j)
    # 请不要修改下面的代码

def faster_dfs(cost,x,y,m,n,memo):
    if not memo[x][y]==-1:
        return memo[x][y]
    if x==m and y==n:
        memo[x][y]=cost[x][y]
        return memo[x][y]
    memo[x][y]=999999999999999999999;a=memo[x][y];b=memo[x][y]
    tx=x+1;ty=y
    if 0<=tx and tx<=m and 0<=ty and ty<=n:
        a=faster_dfs(cost,tx,ty,m,n,memo)
    tx=x;ty=y+1
    if 0<=tx and tx<=m and 0<=ty and ty<=n:
        b=faster_dfs(cost,tx,ty,m,n,memo)
    memo[x][y]=min(a,b)+cost[x][y]
    return memo[x][y]
#第二题
def minPathCost_Memo(cost, i, j, memo):
    # 请在下面编写代码
    for ii in range(0,len(memo)):
        for jj in range(0,len(memo[ii])):
            memo[ii][jj]=-1
    return faster_dfs(cost,0,0,i,j,memo)
    # 请不要修改下面的代码

#第三题
def countWays(n):
    # 请在下面编写代码
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return countWays(n-1)+countWays(n-2)
    # 请不要修改下面的代码

#第四题
def countWays_Memo(n, memo=[]):
    # 请在下面编写代码
    memo=[]
    memo.append(0);memo.append(1);memo.append(2)
    for i in range(3,n+1):
        memo.append(memo[i-1]+memo[i-2])
    # 请不要修改下面的代码
    return memo[n]

if __name__=="__main__":
    randseeds = [9, 99, 999, 9999, 99999]
    for trial in range(5):
        seed(randseeds[trial])
        cost = []
        for i in range(10):
            temp = []
            for j in range(10):
                temp.append(randint(1,10))
            cost.append(temp)

        #start = clock()
        print(minPathCost(cost, 9, 9))
        #print(clock() - start)

    print('*' * 20)

    randseeds = [9, 99, 999, 9999, 99999]
    for trial in range(5):
        seed(randseeds[trial])
        cost = []
        for i in range(100):
            temp = []
            for j in range(100):
                temp.append(randint(1, 10))
            cost.append(temp)        
        memo = []
        for i in range(100):
            memo.append([0] * 100)
        #start = clock()
        print(minPathCost_Memo(cost, 99, 99, memo))
        #print(clock()-start)

    print('*' * 20)

    for n in range(25,35):
        print(countWays(n))
    print('*' * 20)

    for n in range(90,100):
        print(countWays_Memo(n))
