# -*- encoding: utf-8 -*-
class NaturalNumber(object):
    def __init__(self, pre):
        self.pre = pre

    def __str__(self):
        #该方法在NaturalNumber对象被print时被调用
        #请在下面编程
        result = ''
        if self.pre == None:
            result = "Zero"
        elif self.pre.pre == None:
            result = "Succ Zero"
        else:
            pre = self.pre
            result = "Succ(" + pre.__str__() + ")"
        return result

    def __add__(self, other):
        #该方法重载了+运算，请编程实现自然数系统的加法：
        # a + zero = a
        # a + succ(b) = succ(a + b)
        if other.pre==None:
            return self
        else:
            return NaturalNumber(self.__add__(other.pre))
    
    def __mul__(self, other):
        # 该方法重载了*运算，请编程实现自然数系统的乘法：
        # a * zero = zero
        # a * succ(b) =  a * b + a
        if other.pre==None:
            return None
        elif other.pre.pre==None:
            return self
        else:
            return self*other.pre+self

    def toNumber(self):
        #该方法实现NatrualNumber到其对应的阿拉伯数字的转换
        #如zero->0, one->1，...
        num=0
        while not self.pre==None:
            self=self.pre
            num+=1
        return num

def succ(n):
    #返回一个以NaturalNumber对象n为前继的NaturalNumber对象
    #请在此实现该函数
    return NaturalNumber(n)

def foldn(init, h, n):
    #请在此处实现foldn的功能
    if n==0:
        return NaturalNumber(None)
    else:
        return h(foldn(init,h,n-1))

def foldn2(init, h):
    def f(n):
        #print(type(n))
        #请在此区域内实现foldn2的功能
        if n.pre==None:
            return init
        else:
            return h(foldn2(init,h)(n.pre))
        #请在此区域内实现foldn2的功能
    return f

if __name__ == "__main__":
    zero = NaturalNumber(None)
    print(zero)
    one = NaturalNumber(zero)
    print(one)
    two = NaturalNumber(one)
    three=NaturalNumber(two)
    four=NaturalNumber(three)
    five=NaturalNumber(four)
    print(two)
    print('-'*20)
    print(foldn2(five, succ)(five))
    print(foldn2(zero, foldn2(five, succ))(three))
    print(foldn2(one, foldn2(zero, foldn2(five, succ)))(two))