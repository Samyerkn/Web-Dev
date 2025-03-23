#1
def cigar_party(cigars, is_weekend):
  if cigars >= 40 and cigars <= 60 and not is_weekend:
    return True
  elif cigars >= 40 and  is_weekend:
    return True
  else:
    return False


#2
def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  elif you >= 8 or date >= 8:
    return 2
  else:
    return 1


#3
def squirrel_play(temp, is_summer):
  if not is_summer:
    if temp >= 60 and temp <=90:
      return True
  else:
    if temp >= 60 and temp <= 100:
      return True
  return False


#4
def caught_speeding(speed, is_birthday):
  res = 0
  if not is_birthday:
    if speed <= 60:
      res = 0
    elif speed >= 61 and speed <= 80:
      res = 1
    elif speed >= 81:
      res = 2
  else:
    if speed <= 65:
      res = 0
    elif speed >= 66 and speed <= 85:
      res = 1
    elif speed >= 86:
      res = 2
  return res


#5
def sorta_sum(a, b):
  sum = a + b
  if sum >= 10 and sum <= 19:
    return 20
  else:
    return sum


#6
def alarm_clock(day, vacation):
  res = ""
  if not vacation:
    if day >= 1 and day <= 5:
      res = "7:00"
    else:
      res = "10:00"
  else:
    if day >= 1 and day <= 5:
      res = "10:00"
    else:
      res = "off"
  return res
    
#7
def love6(a, b):
  if a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6:
    return True
  return False

#8
def in1to10(n, outside_mode):
  if not outside_mode:
    if n >= 1 and n <= 10:
      return True
  else:
    if n <= 1 or n >= 10:
      return True
  return False
    
#9
def near_ten(num):
  r = num % 10
  if r <= 2 or r >= 8:
    return True
  else:
    return False