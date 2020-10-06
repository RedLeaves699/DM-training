import functools
import copy

class Relation(object):
    def __init__(self, sets, rel):
        #rel为sets上的二元关系
        assert not(len(sets)==0 and len(rel) > 0) #不允许sets为空而rel不为空
        assert sets.issuperset(set([x[0] for x in rel]) | set([x[1] for x in rel])) #不允许rel中出现非sets中的元素
        self.rel = rel;self.sets = sets

    def __str__(self):
        relstr = '{}'
        setstr = '{}'
        if len(self.rel) > 0:
            relstr = str(self.rel)
        if len(self.sets) > 0:
            setstr = str(self.sets)
        return 'Relation: ' + relstr + ' on Set: ' + setstr

    def __eq__(self, other):
        return self.sets == other.sets and self.rel == other.rel

    def diagonalRelation(self):
        #返回代表IA的Relation对象
        return Relation(self.sets, set([(a, a) for a in self.sets]))

    def __mul__(self, other):
        assert self.sets == other.sets
        #实现两个关系的合成，即self*other表示other合成self。请注意是先看other的序偶,结果为一个Relation对象
        return Relation(self.sets,set([(i[0],j[1]) for i in other.rel for j in self.rel\
                if i[1]==j[0]]))

    def __pow__(self, power, modulo=None):
        assert power >= -1
        # 实现同一关系的多次合成，重载**运算符，即self*self*self=self**3,结果是一个Relation对象
        if power==-1:
            return Relation(self.sets,set([(i[1],i[0]) for i in self.rel]))
        elif power==0:
            return Relation(self.sets,(frozenset([(a, a) for a in self.sets])))
        elif power==1:
            return Relation(self.sets,set(self.rel))
        else:
            s=self
            for i in range(1,power):
                self*=s
            return self

    def __add__(self, other):
        assert self.sets == other.sets
        #实现两个关系的并运算，重载+运算符，即self+other表示self并other,是Relation对象rel成员的并
        return Relation(self.sets,self.rel | other.rel)
    
    def toMatrix(self):
        #将序偶集合形式的关系转换为矩阵,为保证矩阵的唯一性，需对self.sets中的元素先排序
        matrix = []
        elems = sorted(list(self.sets))
        l=0
        for elem in elems:
            line = [0]*len(self.sets)
            #请在此处编写程序，实现转换为矩阵的功能
            for elem2 in elems:
                if (elem,elem2) in self.rel:
                    line[l]=1
                l+=1
            l=0;matrix.append(line)
            #请在上面编写程序，不要修改下面的代码
        return matrix
    
    def isReflexive(self):
        #判断self是否为自反关系，是则返回True，否则返回False
        for i in self.sets:
            if not (i,i) in self.rel:
                return False
        return True
    def isIrreflexive(self):
        # 判断self是否为反自反关系，是则返回True，否则返回False
        for i in self.sets:
            if (i,i) in self.rel:
                return False
        return True
    
    def isSymmetric(self):
        # 判断self是否为对称关系，是则返回True，否则返回False
        for i in self.rel:
            if not (i[1],i[0]) in self.rel:
                return False
        return True
    def isAsymmetric(self):
        # 判断self是否为非对称关系，是则返回True，否则返回False
        for i in self.rel:
            if (i[1],i[0]) in self.rel:
                return False
        return True
    def isAntiSymmetric(self):
        # 判断self是否为反对称关系，是则返回True，否则返回False
        for i in self.rel:
            if not (not (i[1],i[0]) in self.rel or (i[0]==i[1])):
                return False
        return True

    def isTransitive(self):
        # 判断self是否为传递关系，是则返回True，否则返回False
        for i in self.rel:
            for j in self.rel:
                if i[1]==j[0]:
                    if not (i[0],j[1]) in self.rel:
                        return False
        return True
    def reflexiveClosure(self):
        #求self的自反闭包，注意使用前面已经重载过的运算符,返回一个Relation对象，为self的自反闭包
        return self+self.diagonalRelation()
    def symmetricClosure(self):
        # 求self的对称闭包，注意使用前面已经重载过的运算符,返回一个Relation对象，为self的对称闭包
        return self+self**-1
    def transitiveClosure(self):
        # 求self的传递闭包，注意使用前面已经重载过的运算符,按照传递闭包计算公式求传递闭包
        closure = self;tmp=closure
        tmp*=tmp
        while not closure==tmp:
            closure*=closure
            tmp*=tmp
        return closure
    def transitiveClosure3(self):
        #该方法利用Roy-Warshall计算传递闭包,现将关系转换为矩阵，再调用__warshall函数
        m = self.toMatrix()
        return self.__warshall(m)

    def __warshall(self, a):
        assert (len(row) == len(a) for row in a)
        n = len(a)
        #请在下面编程实现Roy-Warshall求传递闭包的算法,参数a：为一个关系矩阵
        for k in range(0,n):
            for i in range(0,n):
                for j in range (0,n):
                    if (a[i][k] and a[k][j]==True) or a[i][j]==True:
                        a[i][j]=1
        return a

def isEquivalenceRelation(rel):
    #该函数对给定的Relation对象rel，判断其是否为等价关系
    return rel.isReflexive() and rel.isSymmetric() and rel.isTransitive()

def createPartition(rel):
    #对给定的Relation对象rel，求其决定的rel.sets上的划分
    #如果rel不是等价关系，返回空集
    if not isEquivalenceRelation(rel):
        print("The given relation is not an Equivalence Relation")
        return set([])
    #如rel是等价关系，请编程实现求划分的程序
    partition = set([])
    for i in sorted(rel.sets):
        s=set([])
        for j in sorted(rel.sets):
            if (i,j) in rel.rel:
                s.add(j)
        partition.add(frozenset(s))
    return partition

def createEquivalenceRelation(partition, A):
    #对给定的集合A，以及A上的一个划分partition,生成由该划分决定的等价关系
    assert functools.reduce(lambda x, y: x.union(y), partition) == A
    rel=set([])
    for s in partition:
        for i in s:
            for j in s:
                rel.add((i,j))
    return Relation(A,rel)

def isPartialOrder(rel):
    #该函数对给定的Relation对象rel，判断其是否为半序关系
    return rel.isReflexive() and rel.isAntiSymmetric() and rel.isTransitive()
def isQuasiOrder(rel):
    #该函数对给定的Relation对象rel，判断其是否为拟序关系
    return rel.isIrreflexive() and rel.isTransitive()
def isLinearOrder(rel):
    #该函数对给定的Relation对象rel，判断其是否为全序关系
    if not isPartialOrder(rel):
        return False
    else:
        for i in rel.sets:
            for j in rel.sets:
                if not((i,j) in rel.rel or (j,i) in rel.rel):
                    return False
        return True

def join(rel1, rel2):
    #对给定的关系rel1和rel2
    assert rel1.sets == rel2.sets
    #首先得到二者的矩阵
    M1 = rel1.toMatrix()
    M2 = rel2.toMatrix()
    m = len(M1)
    n = m
    M = copy.deepcopy(M1)
    #请在此处编写代码，实现关系矩阵的join运算，结果存于M中
    for i in range(0,n):
        for j in range(0,n):
            M[i][j]=M[i][j] | M2[i][j]
    # 请在上面编写代码，实现关系矩阵的join运算
    return M

def meet(rel1, rel2):
    #对给定的关系rel1和rel2
    assert rel1.sets == rel2.sets
    #首先得到二者的矩阵
    M1 = rel1.toMatrix()
    M2 = rel2.toMatrix()
    m = len(M1)
    n = m
    M = copy.deepcopy(M1)
    #请在此处编写代码，实现关系矩阵的meet运算，结果存于M中
    for i in range(0,n):
        for j in range(0,n):
            M[i][j]=M[i][j] & M2[i][j]
    # 请在上面编写代码，实现关系矩阵的meet运算
    return M

def booleanProduct(rel1, rel2):
    # 对给定的关系rel1和rel2
    assert rel1.sets == rel2.sets
    # 首先得到二者的矩阵
    M1 = rel1.toMatrix()
    M2 = rel2.toMatrix()
    m = len(M1)
    n = m
    M = copy.deepcopy(M1)
    # 请在此处编写代码，实现关系矩阵的布尔乘积运算，结果存于M中
    for i in range(0,n):
        for j in range(0,n):
            M[i][j]=0
            for k in range(0,n):
                M[i][j]|=(M1[i][k] & M2[k][j])
    # 请在上面编写代码，实现关系矩阵的布尔乘积运算
    return M

def printMatrix(M):
    for i in range(len(M)):
        print(M[i])

if __name__ == "__main__":
    print('Relation Composition: ')
    R1 = frozenset([(1, 2), (1, 3), (2, 4), (3, 5)])
    R2 = frozenset([(2, 4), (3, 5)])
    rel1 = Relation({1, 2, 3, 4, 5}, R1)
    rel2 = Relation({1, 2, 3, 4, 5}, R2)
    print(rel2 * rel1)
    print(rel1 * rel2)
    print(Relation({1, 2, 3, 4, 5}, set([]))*rel1)
    print("Relation Power:")
    R1 = frozenset([(1, 2), (1, 3), (2, 4), (3, 5)])
    rel1 = Relation({1, 2, 3, 4, 5}, R1)
    print(rel1**-1)
    print(rel1**0)
    print(rel1**1)
    print(rel1**2)
    print("Relation Union:")
    R1 = frozenset([(1, 2), (1, 3), (2, 4), (3, 5)])
    R2 = frozenset([(2, 4), (3, 5)])
    rel1 = Relation({1, 2, 3, 4, 5}, R1)
    rel2 = Relation({1, 2, 3, 4, 5}, R2)
    print(rel1 + rel2)
    printMatrix(Relation({1, 2, 3}, {(1, 2), (2, 3)}).toMatrix())
    print(createPartition(Relation({1, 2, 3, 4}, {(1, 1), (2, 2), (3, 3), (4, 4), (1, 3), (2, 4), (3, 1), (4, 2)})))
    print(createEquivalenceRelation({frozenset({2}), frozenset({4}), frozenset({1, 3})}, {1, 2, 3, 4}))
    print("Boolean Product:")
    R1 = frozenset([('c', 'v'), ('3', 'v'), ('9', 'a'), ('k', 'c'), ('k', 'v')])
    R2 = frozenset([('k', 't'), ('t', 't'), ('9', 'k'), ('c', 'k')])
    rel1 = Relation({'c', 'a', '9', '3', 't', 'k', 'v'}, R1)
    printMatrix(rel1.toMatrix())
    rel2 = Relation({'c', 'a', '9', '3', 't', 'k', 'v'}, R2)
    printMatrix(rel2.toMatrix())
    printMatrix(booleanProduct(rel1,rel2))
    R1 = frozenset([(2,4),(3,3),(4,2),(4,4)])
    R2 = frozenset([(2,1),(3,2),(4,3)])
    rel1=Relation({1,2,3,4},R1);rel2=Relation({1,2,3,4},R2)
    printMatrix(booleanProduct(rel2,rel1))