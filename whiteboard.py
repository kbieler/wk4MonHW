# Least Larger
# Given an array of numbers and an index, return the index of the least number
# larger than the element at the given index, or -1 if there is no such index.
# Example:
#numbers: ([4, 1, 3, 5, 6], 0 ) 
# Output: 3
# Input: ([4, 1, 3, 5, 6], 4)
# Output: -1

#isolate the value of the index provided
#compare that value to each of the other values in the list
#take all values higher than the selected value and determine the lowest of those
#return index of that value

def least_larger(nums, i):
    #higher = []
    #for n in nums:
        #if n > nums[i]:
            #higher.append(n)
    higher = [n for n in nums if n> nums[i]]          
    if higher:
        return nums.index(min(higher))
    return -1
    

print(least_larger([4, 1, 3, 5, 6], 4))
print(least_larger([4, 1, 3, 5, 6], 0))



