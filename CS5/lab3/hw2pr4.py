# Function 1
"""
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
We sleep in if it is not a weekday or we're on vacation. 
Return True if we sleep in.
"""


def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


# Function 2
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False


# Function 3
def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    else:
        return a + b


# Function 4
def diff21(n):
    abs_diff = abs(n - 21)

    if n > 21:
        return 2 * (abs_diff)

    else:
        return abs_diff


# Function5
def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False


# Functio 6
def makes10(a, b):
    if a == 10 or b == 10 or a + b == 10:
        return True
    else:
        return False


# Function 7
def near_hundred(n):
    if abs((100 - n)) <= 10 or abs((200 - n)) <= 10:
        return True
    else:
        return False


# Function 8
def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return (a < 0 and b > 0) or (a > 0 and b < 0)


# Funciton 9
def not_string(str):
    if str[0:3] == "not":
        return str
    else:
        new_str = "not" + " " + str
        return new_str


# Function 10
def missing_char(str, n):
    new_str = str[0:n] + str[n + 1 :]
    return new_str


# Function 11
def front_back(str):
    if len(str) <= 1:
        return str

    mid = str[1 : len(str) - 1]  # can be written as str[1:-1]

    # last + mid + first
    return str[len(str) - 1] + mid + str[0]


# Function 12
def front3(str):
    if len(str) == 0:
        return str
    else:
        return 3 * str[0:3]


# List 1
# Function 13
def first_last6(nums):
    ind_las = len(nums) - 1
    if len(nums) == 0:
        return False
    elif nums[0] == 6 or nums[ind_las] == 6:
        return True
    else:
        return False


# Function 14
def same_first_last(nums):
    """Given an array of ints, return True if the array is length 1 or more,
    and the first element and the last element are equal.
    """

    if len(nums) >= 1 and nums[0] == nums[-1]:
        return True
    else:
        return False


"""
def same_first_last(nums):
  return (len(nums) >= 1 and nums[0] == nums[-1])
"""


# Funtion 15
def make_pi():
    return [3, 1, 4]


# function 16


def common_end(a, b):
    if len(a) and len(b) < 0:
        return False
    elif a[0] == b[0] or a[-1] == b[-1]:
        return True
    else:
        return False


# function 17
def sum3(nums):
    return nums[0] + nums[1] + nums[2]


# function 18
def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]


# function 19
def reverse3(nums):
    return [nums[2], nums[1], nums[0]]


# function 20
def max_end3(nums):
    if nums[0] < nums[2]:
        return [nums[2], nums[2], nums[2]]
    elif nums[2] < nums[0]:
        return [nums[0], nums[0], nums[0]]
    else:
        return [nums[0], nums[0], nums[0]]


# function 21
def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) < 2:
        return nums[0]

    else:
        return nums[0] + nums[1]


# function 23
def middle_way(a, b):
    return [a[1], b[1]]


# function 24
def make_ends(nums):
    if len(nums) > 1:
        return [nums[0], nums[-1]]
    else:
        return [nums[0], nums[0]]


# function 25
def has23(nums):
    # if 2 or 3 in nums:
    if 2 in nums or 3 in nums:
        return True
    else:
        return False


# function 26
def hello_name(name):
    return "Hello " + name + "!"


# function 27
def make_abba(a, b):
    return a + b + b + a


# function 28
def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"


# function 29
def make_out_word(out, word):
    return out[0:2] + word + out[2:]


# function 30
def extra_end(str):
    return 3 * str[-2:]


# function 31
def first_two(str):
    if len(str) < 2:
        return str
    else:
        return str[0:2]


# function 32
def first_half(str):
    last = int(len(str) / 2)
    return str[0:last]


# function 33
def non_start(a, b):
    if len(a) + len(b) > 1:
        return a[1:] + b[1:]


# function 34
def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a


# function 35


def left2(str):
    if len(str) >= 2:
        return str[2:] + str[0:2]
    else:
        return str


# function 36
def without_end(str):
    return str[1:-1]


# function 37
def cigar_party(cigars, is_weekend):
    if is_weekend and 40 <= cigars:
        return True
    elif 40 <= cigars <= 60:
        return True
    else:
        return False


"""
def cigar_party(cigars, is_weekend):
  if is_weekend:
    return (cigars >= 40)
  else:
    return (cigars >= 40 and cigars <= 60)
    """


# function 38
def squirrel_play(temp, is_summer):
    if is_summer:
        return 60 <= temp <= 100
    else:
        return 60 <= temp <= 90


# function 39
def date_fashion(you, date):
    ## Check the <=2 case first, since it takes precedence

    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2

    else:
        return 1


# function 40
def caught_speeding(speed, is_birthday):
    if is_birthday:
        return 0
    elif speed <= 60:
        return 0
    elif 61 <= speed <= 80:
        return 1
    elif speed >= 81:
        return 2


# function 41
def sorta_sum(a, b):
    if 10 <= a + b <= 19:
        return 20
    else:
        return a + b


# function 42
def near_ten(num):
    if num % 10 <= 2 or 8 <= num % 10 <= 9:
        return True
    else:
        return False


# function 43
def love6(a, b):
    return a == 6 or b == 6 or abs(a - b) == 6 or a + b == 6


# function 44
def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or outside_mode and n >= 10
    elif 1 <= n <= 10:
        return True
    else:
        return False


# 45
def alarm_clock(day, vacation):
    if vacation:
        if day == 0 or day == 6:
            return "off"
        return "10:00"
    else:
        if day == 0 or day == 6:
            return "10:00"
        return "7:00"


# 46
def make_bricks(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - (5 * big)
    else:
        remainder = goal % 5

    return small >= remainder


# function 47
def lone_sum(a, b, c):
    if a == b == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a + b + c


"""
def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c: sum += a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c
  
  return sum
  """


# function 48
def lucky_sum(a, b, c):
    sum = 0
    if a != 13:
        sum += a
    else:
        return sum
    if b != 13:
        sum += b
    else:
        return sum
    if c != 13:
        sum += c
    return sum


# function 49


def no_teen_sum(a, b, c):
    sum = a + b + c
    if 13 <= a < 15 or 16 < a <= 19:
        sum = sum - a

    if 13 <= b < 15 or 16 < b <= 19:
        sum = sum - b

    if 13 <= c < 15 or 16 < c <= 19:
        sum = sum - c

    return sum


# function 50


def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


def round10(num):
    reminder = num % 10
    if reminder < 5:
        return num - (num % 10)

    return num + (10 - num % 10)


# function 51


def close_far(a, b, c):
    if abs(a - c) <= 1 and abs(a - b) >= 2 and abs(b - c) >= 2:
        return True
    elif abs(a - b) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2:
        return True
    else:
        return False


def make_chocolate(small, big, goal):
  # can be done
  if goal >= 5 * big:
      remainder = goal - 5 * big
  else:
      remainder = goal % 5
        
  if remainder <= small:
      return remainder
  return -1