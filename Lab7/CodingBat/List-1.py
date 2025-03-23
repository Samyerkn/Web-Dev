#1
def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  return False

#2
def same_first_last(nums):
  if len(nums) >= 1:
    if nums[0] == nums[-1]:
      return True
  return False


#3
def make_pi():
  return [3, 1, 4]


#4
def common_end(a, b):
  if a[0] == b[0] or a[-1] == b[-1]:
    return True
  return False


#5
def sum3(nums):
  sum = 0
  for i in range(len(nums)):
    sum += nums[i]
  return sum


#6
def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]


#7
def reverse3(nums):
  rev = []
  for i in range(len(nums) - 1, -1, -1):
    rev.append(nums[i])
  return rev


#8
def max_end3(nums):
  maxi = max(nums[0], nums[-1])
  for i in range(len(nums)):
    nums[i] = maxi
  return nums


#9
def sum2(nums):
  sum = 0
  if len(nums) == 0:
    return 0
  elif len(nums) < 2:
    for i in range(len(nums)):
      sum += nums[i]
  else:
    sum = nums[0] + nums[1]
  return sum
      
#10
def middle_way(a, b):
  return [a[len(a)/2], b[len(b)/2]]


#11
def make_ends(nums):
  return [nums[0], nums[-1]]


#12
def has23(nums):
  if 2 in nums or 3 in nums:
    return True
  return False
  
