class RelDB:
    """
    此为代表关系模型的类.
    RelDB用元组来保存关系数据表的表头（attributes_）,将输入为字典形式的
    数据表实际数据转换为元组后保存起来（tuples_），每一行数据的顺序与attributes_
    中的属性顺序一致，即用 attributes_来检索tuples_中的数据。
    """

    def __init__(self, attributes, dictset=set()):
        """
        用给定的attributes创建一个关系表.
        """
        self.attributes_ = tuple(attributes)
        self.tuples_ = set()
        self.tuples_.update(set([self._convert_dict(d) for d in dictset]))

    def __eq__(self, other):
        return self.attributes() == other.attributes() and self._tuples() == other._tuples()

    def __str__(self):
        return str(self.attributes_) + ' : ' + str(self.tuples_)

    def attributes(self):
        """
        返回self的成员attributes_.
        """
        return self.attributes_

    def _convert_dict(self, tup):
        """
        将输入的字典格式数据tup转换为内部的元组格式.
        """
        # 如果输入已经是元组对象，则不需要转换
        if isinstance(tup, tuple):
            return tup
        else:
            return tuple([tup[attribute] for attribute in self.attributes_])

    def add(self, tup=None, **kwargs):
        """
        将字典形式的数据tup或**kwargs格式的关系表数据以元组形式加入到关系表.
        """
        if tup is None:
            tup = kwargs
        self.tuples_.add(self._convert_dict(tup))

    def add_tuple(self, tup):
        """
        将元组形式的关系表数据tup加入到该关系表
        """
        self.tuples_.add(tup)

    def add_multiple(self, tupset):
        """
        将字典tupset中的数据批量加入为该关系数据表的数据
        """
        self.tuples_.update(set([self._convert_dict(tup) for tup in tupset]))

    def _tuples(self):
        return self.tuples_

    def tuples(self):
        """
        一个返回关系数据表中tuples_数据的生成器
        """
        for tup in self._tuples():
            yield dict(zip(self.attributes_, tup))

    def display(self):
        """
        显示该关系数据表
        """
        columns = range(len(self.attributes_))

        col_width = [len(self.attributes_[col]) for col in columns]

        for tupdict in self.tuples():
            tup = self._convert_dict(tupdict)
            for col in columns:
                col_width[col] = max(col_width[col], len(tup[col]))

        hline = ""
        for col in columns:
            hline += "+-" + ("-" * col_width[col]) + "-"
        hline += "+"

        def line(row):
            l = ""
            for col in columns:
                value = row[col]
                l += "| " + value + (" " * (col_width[col] - len(value))) + " "
            l += "|"
            return l

        print(hline)
        print(line(self.attributes_))
        print(hline)

        for tup in self.tuples():
            print(line(self._convert_dict(tup)))

        print(hline)

def defineTables():
    #请在下面的区域编写代码，创建三个数据表，并填入数据
    #请删除pass后再编程
    dept = RelDB(("DNO", "DNAME", "BUDGET"))

    dept.add(DNO="D1", DNAME="Marketing", BUDGET="10M")
    dept.add(DNO="D2", DNAME="Development", BUDGET="12M")
    dept.add(DNO="D3", DNAME="Research", BUDGET="5M")

    emp = RelDB(("ENO", "ENAME", "DNO", "SALARY"))

    emp.add(ENO="E1", ENAME="Lopez", DNO="D1", SALARY="40K")
    emp.add(ENO="E2", ENAME="Cheng", DNO="D1", SALARY="42K")
    emp.add(ENO="E3", ENAME="Finzi", DNO="D2", SALARY="30K")

    emp2 = RelDB(("ENO", "ENAME", "DNO", "SALARY"))
    emp2.add_multiple([
        dict(ENO="E3", ENAME="Finzi", DNO="D3", SALARY="30K"),
        dict(ENO="E4", ENAME="Saito", DNO="D2", SALARY="35K")
    ])
    #请在上方区域编程
    return dept, emp, emp2

def project(orig_dict, attributes):
    #请在下面区域删除pass后编程
    newdict=dict()
    for j in attributes:
        newdict.update({j:orig_dict[j]})
    return newdict

def PROJECT(orig_rel, attributes):
    # 请在下面区域删除pass后编程
    rr=RelDB(attributes)
    newdict=dict()
    for i in orig_rel.tuples():
        rr.add(project(i,attributes))
    return rr

def SELECT(orig_rel, restriction):
    #请在下面区域删除pass后编程
    rr=RelDB(orig_rel.attributes_)
    for i in orig_rel.tuples():
        if restriction(i)==True:
            rr.add(i)
    return rr

def JOIN(rel_1, rel_2):
    assert not(set(rel_1.attributes()) & set(rel_2.attributes()) == set())
    #请在下面区域删除pass后编程
    Title=[];LS=[]
    for i in rel_1.attributes_:
        Title.append(i)
    for head in rel_2.attributes_:
        if not head in rel_1.attributes_:
            Title.append(head)
        else:
            LS.append(head)
    rr=RelDB(tuple(Title))
    for i in rel_1.tuples():
        for j in rel_2.tuples():
            ok=True
            for k in LS:
                if not i[k]==j[k]:
                   ok=False;break
            if ok:
                _tmpl=[]
                for t in i.keys():
                    _tmpl.append(i[t])
                for t in j.keys():
                    if not t in LS:
                        _tmpl.append(j[t])
                rr.add(tuple(_tmpl))
    return rr

if __name__=="__main__":
    dept,emp,emp2=defineTables()
    PROJECT(dept,('DNO','DNAME')).display()
    JOIN(dept,emp).display()