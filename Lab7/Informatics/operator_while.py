#Task: a
# n = int(input())
# i = 1
# while i <= n**0.5:
#     print(i * i)
#     i += 1

#Task: b
# n = int(input())
# i = 2
# while i <= n:
#     if(n % i == 0):
#         print(i)
#         break
#     i += 1

#Task: c
# n = int(input())
# i = 0
# res = 1
# while res <= n:
#     print(res)
#     i += 1
#     res = 2**i

#Task: d
# n = int(input())
# i = 0
# res = 1
# b = False
# while res <= n:
#     res = 2**i
#     i += 1
#     if res == n:
#         b = True
#         break
        
# if b:
#     print("YES")
# else:
#     print("NO")


#Task: e
n = int(input())
res = 1
i = 0
while res <= n:
    res = 2**i
    
    if res >= n:
        print(i)
        break
    i += 1