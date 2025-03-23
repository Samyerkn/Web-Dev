#1
def count_evens(nums):
  res = 0
  for i in nums:
    if i % 2 == 0:
      res += 1
  return res


#2
def big_diff(nums):
  res = max(nums) - min(nums)
  return res


#3
def centered_average(nums):
  nums.sort()
  new = nums[1:-1]
  return sum(new)//len(new)


#4
def sum13(nums):
  sum = 0
  skip = False
  for num in nums:
    if num == 13:
      skip = True
    elif skip:
      skip = False
    else:
      sum += num
    
  return sum
    

#5
def sum67(nums):
  cnt = True
  sum = 0
  for num in nums:
    if num == 6:
      cnt = False
    elif num == 7 and not cnt:
      cnt = True
    elif cnt:
      sum += num
  return sum
    
#6
def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] == nums[i+1] == 2:
      return True
  return False

