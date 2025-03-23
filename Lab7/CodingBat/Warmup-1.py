#1
def sleep_in(weekday, vacation):
  if(weekday and (not vacation)):
    return False
  else:
    return True
  
#2
def monkey_trouble(a_smile, b_smile):
  return not(a_smile ^ b_smile)


#3
def sum_double(a, b):
  if a != b:
    return a + b
  else:
    return (a + b)*2
  
#4
def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2
  

#5
def parrot_trouble(talking, hour):
  if talking:
    if hour < 7 or hour > 20:
      return True
    else:
      return False
  else:
    return False
  

#6
def makes10(a, b):
  if a == 10 or b == 10:
    return True
  elif a + b == 10:
    return True
  else:
    return False
  

#7
def near_hundred(n):
  if abs(n - 100) <= 10 or abs(n - 200) <= 10:
    return True
  else:
    return False
  
#8
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
  

#9
def not_string(str):
  if str[:3] == "not":
    return str
  else:
    return "not " + str
  
#10
def missing_char(str, n):
  new = ""
  for i in range(len(str)):
    if i == n:
      continue
    else:
      new += str[i]
  return new


#11
def front_back(str):
    if len(str) <= 1:
      return str
    res = str[-1] + str[1:-1] + str[0]
    return res
# print(front_back("code"))


#12
def front3(str):
  res = ""
  if len(str) < 3:
    res = str*3
  else:
    res = str[:3]*3
  return res

print(front3("Java"))

