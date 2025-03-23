#Task: a
# a = int(input())
# b = int(input())

# res = (a**2 + b**2)**(1/2)
# print(res)

#Task: b
# num = int(input())
# next_num = num + 1
# prev_num = num - 1
# print(f'The next number for the number {num} is {next_num}.')
# print(f'The previous number for the number {num} is {prev_num}.')

#Task: c
# n = int(input())
# k = int(input())
# print(k // n)

#Task: d
# n = int(input())
# k = int(input())
# print(k % n)

#Task: e
v = int(input())
t = int(input())
s = 109
if v > 0:
    print((v * t) % s)
else:
    print((s + (v * t) % s) % s)