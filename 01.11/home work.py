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

import time

nums = [0, 1, 1, -3, -1]

def collect_ind(src):
    dict = {}
    for i,x in enumerate(src):
        dict[i] = (x)
    return dict

def get_key(scr, search):
    for key, value in scr.items():
        if value == search:
            return(key)

def print_DICK(scr):
    dict = collect_ind(scr)
    for index, (keys, values) in enumerate(dict.items()):
        print(f" index:{keys}   value:{values}")
        
def get_result(scr):
    dict = collect_ind(scr)
    answer = []
    for (key, value) in dict.items():
        result = target - value
        if result in dict and get_key(dict, result) != key and get_key(dict, result) != None:
            answer.append(get_key(dict, result))
            answer.append(key)
            if len(answer) >= 2:
                break
    print(answer)

target = int(input())    

def main(scr):
    start_time = time.time()
    get_result(scr)
    end_time = time.time()
    print(float((end_time - start_time)*10000))
    
main(nums)
    

            
