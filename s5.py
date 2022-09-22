#p1 = "2+2"
#p2 = "1+2*3"
#p3 = "1-2*3"
#print(eval(p1))
#print(eval(p2))
#print(eval(p3))

#l1 = [1, 2, 3, 5, 1, 5, 3, 10]
#print(set(l1))


# from math import log2


# n = int(input())
# i = round(log2(n)) + 1
# flag = True
# while flag:
#     if n % 2 ** i == 0:
#         print(2 ** i)
#         flag = False
#     i -= 1
# if flag:
#     print(1)


# n = 12
# print()

#  writeln(((n xor (n-1)) shr 1)+1);

from math import log2


n = int(input())
i = round(log2(n)) + 1
flag = True
while flag:
    if n % 2 ** i == 0:
        print(2 ** i)
        flag = False
    i -= 1
if flag:
    print(1)

 

