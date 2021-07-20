'''
https://leetcode.com/problems/two-sum/
3. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''    

# # DEFECTIVE SOLUTION
# def two_sum(nums, target):
#     hash = {}
#     answer_hash = {}
#     for num in nums:
#         hash[num] = nums.index(num)
#         for i in hash:
#             if hash[i] == hash[num]: continue
#             if num + i == target:
#                 answer_hash[num] = hash[num]
#                 answer_hash[i] = hash[i]

#     answer_list = []

#     for j in answer_hash:
#        answer_list.append(answer_hash[j])

#     print(sorted(answer_list))

# # DEFECTIVE SOLUTION 2
# def two_sum(nums, target):
#     hash = {}
#     for num in nums:
#         hash[num] = nums.index(num)
#     print(hash)

#     for i in hash:
#         for j in hash:
#             if hash[i] == hash[j]: continue
#             if i + j == target:
#                 return [hash[i], hash[j]] 

# # IN-CLASS SOLUTION: BRUTE LOOPS
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i == j: continue
#             if nums[i] + nums[j] == target: return [i, j]

# # IN-CLASS SOLUTION: HASH TABLES
# def two_sum(nums, target):
#     hash = {}
#     for i in range(len(nums)):
#         difference = target - nums[i]
#         if difference not in hash:
#             hash[difference] = i
#         else: 
#             return [hash[difference], i]
#     print(hash)


# print(two_sum([3,3], 6))