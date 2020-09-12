# -*- encoding: utf-8 -*-
def readAndPrintUniqueWords(filename):
    infile = open(filename, 'r')
    #请在此区间内编程完成函数代码
    value=set([])
    wordlist=infile.readlines()
    if wordlist:
        for word in wordlist:
            word=word.replace("\n","")
            if not word in value:
                print(word)
                value.add(word)
    #请在此区间内编程完成函数代码
    infile.close()

if __name__=="__main__":
    readAndPrintUniqueWords("testdata")