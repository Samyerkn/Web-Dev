#1
# n = int(input().strip())
# if n % 2 == 1:
#     print("Weird")
# elif (n % 2 == 0) and (n >= 2 and n <= 5):
#     print("Not Weird")
# elif (n % 2 == 0) and (n >= 6 and n <= 20):
#     print("Weird")
# elif (n % 2 == 0) and (n > 20):
#     print("Not Weird")


#2
# a = int(input())
# b = int(input())
# sum = a + b
# dif = a - b
# pro = a * b
# print(sum)
# print(dif)
# print(pro)


#3
# a = int(input())
# b = int(input())
# print(a//b)
# print(a/b)


#4
def print_full_name(first, last):
    res = f"Hello {first} {last}! You just delved into python."
    print(res)

first_name = input()
last_name = input()
print_full_name(first_name, last_name)

#5
# def is_leap(year):
#     leap = False
#     if(year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#         leap = True

#     return leap
# year = int(input())
# print(is_leap(year))

#6
# import math
# ab = int(input())
# bc = int(input())
# o = math.atan(ab/bc)
# ans = round(math.degrees(o))
# print(f'{ans}{chr(176)}')

#7
# n = int(input())
# arr = map(int, input().split())
# s = list(set(arr))
# s.sort()
# print(s[-2])

#8
# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()
# res = 0
# for score in student_marks[query_name]:
#     res += score

# ans = res/len(student_marks[query_name])
# print(f"{ans:.2f}")



#9
# n = int(input())
# res = ""
# for i in range(1, n + 1):
#     res += str(i)
# print(res)


#10
def swap_case(s):
    result = "" 
    for char in s:
        if char.islower():
            result += char.upper()  
        elif char.isupper():
            result += char.lower() 
        else:
            result += char 
    return result

s = input()
result = swap_case(s)
print(result)
