#Topic          :       利用filter()滤掉非回数
#File Name      :       Palindrome.py
#Author         :       Jack Cui
#Created        :        15 April 2016
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

if __name__ == "__main__":
    n = int(input("您要查询前多少的回数？\n请您输入："))
    result = filter(is_palindrome,range(1,n+1))
    #print(result)      #   <filter object at 0x019331D0>
    #print([result])    #   [<filter object at 0x019331D0>]
    print(list(result))
    

    #print(list(i for i in range(1,n+1) if (str(i) == str(i)[::-1])))
    print([i for i in range(1,n+1) if str(i) == str(i)[::-1]])