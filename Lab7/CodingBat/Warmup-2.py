#1
def string_times(str, n):
    return str*n


#2
def front_times(str, n):
  if len(str) < 3:
    return str*n
  else:
    return str[:3]*n


#3
def string_bits(str):
  return str[::2]

print(string_bits("Hello"))


#4
def string_splosion(str):
  res = ""
  for i in range(len(str)):
    for j in range(i+1):
      res += str[j]
  return res
    
print(string_splosion("Code"))


#5
def last2(string):
    last2_substring = string[-2:]
    count = 0
    for i in range(len(string) - 2):
        if string[i:i+2] == last2_substring:
            count += 1

    return count

#6
def array_count9(nums):
  return nums.count(9)
print(array_count9([1, 2, 9]))


#7
def array_front9(nums):
  if nums[:4].count(9):
    return True
  else:
    return False


#8
def array123(nums):
  for i in range(len(nums) - 2):
    if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
      return True 
  return False  
print(array123([1, 1, 2, 3, 1]))
  

#9
def string_match(a, b):
    count = 0
    for i in range(min(len(a), len(b)) - 1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count


