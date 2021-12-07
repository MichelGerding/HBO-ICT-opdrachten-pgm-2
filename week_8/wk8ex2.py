def double_char(str):
  result = ''
  for c in str:
    result += c*2
  return result

## coding bat challenges
def count_evens(nums):
  """ count all even numbers in a give array
      Argument: nums a list of numbers
  """
  count = 0
  for i in nums:
    if i %2 == 0:
      count += 1
  return count

def big_diff(nums):
  """ Calculate the biggest difference between 
      elements in list nums
      Arguments: nums a list of numbers
  """
  min_val = 18446744073709551615
  max_val = -18446744073709551615
  for i in nums:
    if min_val > i:
      min_val = i
    if max_val < i:
      max_val = i


  return max_val - min_val


def centered_average(nums):
  """ return the centered average of the list nums
      Argument: nums a list of numbers
  """

  # max size of 64 bit intiger
  min_val = 18446744073709551615
  max_val = -18446744073709551615

  total = 0
  for i in nums:
    total += i

    if min_val > i:
      min_val = i
    if max_val < i:
      max_val = i

  total -= (min_val + max_val)
  return total // (len(nums) -2)

def sum13(nums):
  """ add all numbers in a array except number 13 
      and the number directly after
      Argument: nums, list of numbers
  """
  total = 0

  for i in range(len(nums)):

    if nums[i] == 13:
      continue
    if i > 0:
      if nums[i-1] == 13:
        continue

    total += nums[i]

  return total

def sum67(nums):
  """ Return the sum of the numbers in the array, except ignore sections of 
      numbers starting with a 6 and extending to the next 7
      Argument: nums a list of numbers
  """
  total = 0

  in_6 = False
  for i in nums:
    if i == 6:
      in_6 = True
      continue

    if in_6:
      if i == 7:
        in_6 = False      
      continue

    total += i
  return total

# bonus opgaven

def has22(nums):
  """ Given an array of ints, return True if the array
      contains a 2 next to a 2 somewhere.
      Argument: nums a list of ints
  """

  for i in range(len(nums)):
    if i == len(nums) - 1:
      return False
    
    if nums[i] == 2 and nums[i+1] == 2:
      return True
  return False


def count_hi(str):
  """ Return the number of times that the string "hi" 
      appears anywhere in the given string.
      Argument: str a string
  """
  count = 0

  for i in range(len(str)):
    if i == len(str) -1:
      break

    if str[i:i+2] == 'hi':
      count += 1

  return count


def cat_dog(str):
  """ Return True if the string "cat" and "dog" appear the same number
      of times in the given string.
      Argument: str a string
  """
  cats, dogs = 0, 0

  for i in range(len(str)):
    if i == len(str) -2:
      break

    if str[i:i+3] == 'cat':
      cats += 1
    elif str[i:i+3] == 'dog':
      dogs += 1

  return cats == dogs

def count_code(str):
  """ Return the number of times that the string "code" appears anywhere 
      in the given string, except we'll accept any letter for the 'd', 
      so "cope" and "cooe" count.
      Argument: str a string
  """
  count = 0

  for i in range(len(str)):
    if i == len(str) - 3:
      break

    if str[i:i+2] == 'co' and str[i+3] == 'e':
      count += 1

  return count


def end_other(a, b):
  """
  Given two strings, return True if either of the strings appears at the very 
  end of the other string, ignoring upper/lower case differences (in other 
  words, the computation should not be "case sensitive").
  """

  long_s, short_s = (a,b) if len(a) >= len(b) else (b,a)

  ends = True
  for c in zip(long_s[-len(short_s):].lower(), short_s.lower()):
    
    if c[0] != c[1]:
      ends = False

  return ends

def xyz_there(str):
  """ Return True if the given string contains an appearance of "xyz" where the xyz 
      is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
      Argument: str a string
  """
  for i in range(len(str)):
    if i == len(str) -1:
      return False

    if str[i:i+3] == 'xyz' and str[i-1] != '.':
      return True

  return False
