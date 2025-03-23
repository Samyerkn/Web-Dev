#Task: a
# def minimum(a, b, c, d):
#     minimum = a
#     if b < minimum:
#         minimum = b
#     if c < minimum:
#         minimum = c
#     if d < minimum:
#         minimum = d
#     return minimum
    

# a, b, c, d = map(int, input().split())
# print(minimum(a, b, c, d))



#Task: b
# def power(a, n):
#     return a**n

# a, n = map(float, input().split())
# print(power(a, n))



#Task: c
def xor(x, y):
    if x == y:
        return 0
    else:
        return 1
    
def xor2(x, y):
    return x ^ y

x, y = map(int, input().split())
print(xor(x, y)) 
