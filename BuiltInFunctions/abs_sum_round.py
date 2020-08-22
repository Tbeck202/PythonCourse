# The absolyte value of any number is equal to itself.
# A negative number would be eqaul to its positive equivalent
import math
print(abs(-5))  # 5
print(abs(-5.3456))  # 5.3456
# math.fabs() will do the same as abs() but will treat everything as a float
# must import math

print(math.fabs(5))  # 5.0

# sum
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums2 = [1, 2, 3.5]
print(sum(nums))  # 45
print(sum(nums, 5))  # 50
print(sum(range(0, 10)))  # 45
print(sum(nums2))  # 6.5

# round

print(round(10.4))  # 10
print(round(10.6))  # 11
print(round(5.2134674374376, 2))  # 5.21
print(round(5.2135674374376, 3))  # 5.214
