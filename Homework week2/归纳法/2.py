#第一题
def isPal(s):
    # 请在下面编写代码
    strlen = len(s)
    if strlen==0:
        return True
    else:
        return s[0]==s[strlen-1] and isPal(s[1:strlen-1])




    
    # 请不要修改下面的代码
#第二题
def koch(n):
    # 请在下面编写代码
    if n==0:
        return 'F'
    tmp=koch(n-1)
    return tmp+'L'+tmp+'R'+tmp+'L'+tmp
    
    #请不要修改下面的代码
#第三题
def vowel(s):
    #请在下面编写代码
    if len(s)==0:
        return 0
    else:
        if s[0] in 'aeiouAEIOU':
            return 1 + vowel(s[1:])
        else:
            return vowel(s[1:])
    
    #请不要修改下面的代码
#第四题
def squareSum(n):
    #请在下面编写代码
    if n==0:
        return 0
    else:
        return n**2+squareSum(n-1)
    #请不要修改下面的代码
#第五题
def vonNeumann(n):
    # 请在下面编写代码
    if n == 0:
        return '{}'
    else:
        s=''
        for i in range(0, n - 1):
            s += vonNeumann(i) + ', '
        return '{' + s + vonNeumann(n - 1) + '}'

    #请不要修改下面的代码
#第六题
def perm(s):
    # 请在下面编写代码
    if len(s) == 0:
        return ['']
    strings = []
    for i in range(len(s)):
        subStrings = perm(s[:i]+s[i+1:])
        for subString in subStrings:
            strings += [s[i] + subString]
    return strings
    #请不要修改下面的代码
if __name__=="__main__":
    for s in ['', 'abcdefgfedcba', 'I am the king of the world', 'Python', 'madam', 'Able was I ere I saw Elba']:
        print(isPal(s.lower()))
    print('*'*20)
    for n in range(4):
        print(koch(n))
    print('*' * 20)
    for s in ['', 'abcdefgfedcba', 'I am the king of the world', 'Python', 'madam', 'Able was I ere I saw Elba']:
        print(vowel(s))
    print('*' * 20)
    for n in range(10):
        print(squareSum(n))
    print('*' * 20)
    for n in range(6):
        print(vonNeumann(n))
        
    ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for n in range(1,5):
        print('*' * 20)
        string = ALPHABET[:n]
        print(perm(string))