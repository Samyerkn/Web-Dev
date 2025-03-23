#1
def make_bricks(small, big, goal):
  max_big = min(big, goal // 5)
  remaining = goal - (max_big * 5)
  return remaining <= small

#2
def lone_sum(a, b, c):
    sum = a + b + c
    if a == b:
        sum = sum - a - b
    elif a == c:
        sum = sum - a - c
    if a == b == c:
        return 0
    elif b == c:
        sum = sum - b - c
    return sum

#3
def lucky_sum(a, b, c):
  sum = 0
  m = [a, b, c]
  for i in range(3):
    if m[i] == 13:
      break
    sum += m[i]
  return sum


#4
def fix_teen(n):
  if n >= 13 and n <= 19 and n != 15 and n !=16:
    return 0
  return n
def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
  

#5
def round10(num):
  if num % 10 >= 5:
    return num + (10 - num % 10)
  else:
    return num - (num % 10)

def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)


#6
def close_far(a, b, c):
  def isClose(x, y):
    return abs(x - y) <= 1
  def isFar(x, y):
    return abs(x - y) >= 2
    
  c1 = isClose(a, b) and isFar(a, c) and isFar(b, c)
  c2 = isClose(a, c) and isFar(a, b) and isFar(b, c)
  
  return c1 or c2
  
#7
def make_chocolate(small, big, goal):
  res = 0
  cnt = 0
  while res != goal:
    res += big * 5
    big = 0
    res += 1
    cnt += 1
    small -= 1
  return cnt
print(make_chocolate(4, 1, 9))


def make_chocolate(small, big, goal):
  max_big = min(big, goal // 5)
  r = goal - (max_big * 5)
  if r <= small:
    return r
  return -1