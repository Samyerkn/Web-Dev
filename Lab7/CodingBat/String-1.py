#1
def hello_name(name):
  res = "Hello " + name + "!" 
  return res


#2
def make_abba(a, b):
  res = a + b + b + a
  return res


#3
def make_tags(tag, word):
  t1 = "<" + tag + ">"
  t2 = "</" + tag + ">"
  res = t1 + word + t2
  return res

print(make_tags('i', 'Yay'))


#4
def make_out_word(out, word):
  res = out[:2] + word + out[2:]
  return res


#5
def extra_end(str):
  return str[-2:]*3

#6
def first_two(str):
  if len(str) < 2:
    return str
  else:
    return str[:2]


#7
def first_half(str):
  return str[:len(str)/2]

#8
def without_end(str):
  return str[1:-1]

#9
def combo_string(a, b):
  if len(a) < len(b):
    return a + b + a
  else:
    return b + a + b
  

#10
def non_start(a, b):
  return a[1:] + b[1:]

#11
def left2(str):
  return str[2:] + str[:2]

