#Task: a
# n = int(input())
# massiv = list(map(int, input().split()))

# for i in range(len(massiv)):
#     if i % 2 == 0:
#         print(massiv[i])


#Task: b
# n = int(input())
# massiv = list(map(int, input().split()))
# for i in range(n):
#     if(massiv[i] % 2 == 0):
#         print(massiv[i])


#Task: c
# n = int(input())
# massiv = list(map(int, input().split()))
# cnt = 0
# for i in range(n):
#     if(massiv[i] > 0):
#         cnt += 1
# print(cnt)
#Task: d
# n = int(input())
# massiv = list(map(int, input().split()))
# cnt = 0
# k = 0
# for i in range(1, n):
#     if(massiv[i] > massiv[k]):
#         cnt += 1
#     k += 1
# print(cnt)


#Task: e
# n = int(input())
# massiv = list(map(int, input().split()))
# barma = False
# k = 0
# for i in range(1, n):
#     if(massiv[i] > 0 and massiv[k] > 0) or (massiv[i] < 0 and massiv[k] < 0):
#         barma = True
#         break
#     k += 1
# if barma:
#     print("YES")
# else:
#     print("NO")

#Task: f
# n = int(input())
# massiv = list(map(int, input().split()))
# left = 0
# right = 2
# cnt = 0
# for i in range(1, n - 1):
#     if (massiv[left] < massiv[i] and massiv[right] < massiv[i]):
#         cnt += 1
#     left += 1
#     right += 1
# print(cnt)

#Task: g
n = int(input())
massiv = list(map(int, input().split()))

for i in range(n // 2):
    massiv[i], massiv[n - i - 1] = massiv[n - i - 1], massiv[i]
for i in range(n):
    print(massiv[i])
