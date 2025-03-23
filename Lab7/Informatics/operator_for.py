#Task: a
# a = int(input())
# b = int(input())

# for i in range(a, b + 1):
#     if(i % 2 == 0):
#         print(i)


#Task: b
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# for i in range(a, b + 1):
#     if(i % d == c):
#         print(i)


#Task: c
# a = int(input())
# b = int(input())

# for i in range(a, b + 1):
#     c = (i**0.5)
#     if i % c == 0:
#         print(i)

#Task: d
# x = input()
# d = input()
# cnt = 0
# for i in x:
#     if i == d:
#         cnt += 1
# print(cnt)

#Task: e
# x = input()
# sum = 0
# for i in x:
#     sum += int(i)
# print(sum)


#Task: f
# x = input()
# res = ""
# for i in range(len(x) - 1, -1, -1):
#     res += x[i]
# print(int(res))


#Task: g
# x = int(input())
# for i in range(2, x + 1):
#     if x % i == 0:
#         print(i)
#         break



#Task: h
# x = int(input())
# for i in range(1, x + 1):
#     if (x % i == 0):
#         print(i)


#Task: i
# x = int(input())
# cnt = 0
# for i in range(1, int(x**0.5) + 1):
#     if x % i == 0:
#         cnt += 1  
#         if i != x // i:
#             cnt += 1
# print(cnt)



#Task: j
# sum = 0
# for i in range(100):
#     x = int(input())
#     sum += x
# print(sum)


#Task: k
# n = int(input())
# sum = 0
# for i in range(n):
#     x = int(input())
#     sum += x
# print(sum)

#Task: l
# x = input()
# power = len(x) - 1
# dec = 0
# for i in x:
#     dec += (int(i) * 2**power)
#     power -= 1

# print(dec)


#Task: m
n = int(input())
cnt = 0
for i in range(n):
    x = int(input())
    if x == 0:
        cnt += 1
print(cnt)
