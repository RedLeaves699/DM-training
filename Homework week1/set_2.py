# -*- encoding: utf-8 -*-
def shakeSpeare(filename):
    infile = open(filename, 'r')
    #请在此区间内编程实现函数功能
    reverse=set([])
    passage=infile.read()
    RawWordlist=passage.split()
    WordList=[]
    dictory=set([])
    for word in RawWordlist:
        word=word.replace("\n","")
        word=word.rstrip()
        if word in dictory:
            continue
        else:
            dictory.add(word)
        ss=word[::-1]
        if ss in dictory:
            if('a'<=word[0] and word[0]<='z') or ('A'<=word[0] and word[0]<='Z'):
                if len(word)>4:
                    reverse.add(ss)
                    reverse.add(word)
    #请在此区间内编程实现函数功能
    infile.close()
    return reverse


if __name__=="__main__":
    print(shakeSpeare("testdata"))