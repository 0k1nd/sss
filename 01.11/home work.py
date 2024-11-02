#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Example 1:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#Example 2:
#Input: nums = [3,2,4], target = 6
#Output: [1,2]

#Example 3:
#Input: nums = [3,3], target = 6
#Output: [0,1]

#Constraints:
#2 <= nums.length <= 104
#-109 <= nums[i] <= 109
#-109 <= target <= 109
#Only one valid answer exists.

nums = [1, 3, 6, 7, 8, 9, 10, 23, 30, 45, 98, 22, 1, 5, 15, 100]
target = int(input())

def collect_ind(src):
    dict = {}
    for i,x in enumerate(src):
        dict[x] =  (i)
    return dict

def print_DICK(scr):
     for index, (keys, values) in enumerate((scr).items()):
        print(f" value:{keys}   index:{values}")
        
def get_result(scr):
    answer = []
    for (key, value) in (scr).items():
        result = target - key
        if result in nums_dict and (scr)[result] != (scr)[key]:
            answer.append(value)
        elif len(answer) > 1:
            break
    print(answer)
    
nums_dict = collect_ind(nums)


get_result(nums_dict)       