#思路一
#Python
def twoSum(nums, target):
    list = []                                  #储存下标
    for i in range(len(nums)):                 #第一次循环遍历nums列表
        for j in range(i + 1, len(nums)):      #第二次循环遍历下标为i的后面的nums列表值
            if nums[i] + nums[j] == target:    #判断是否存在两元素和为target
                list.append(i)                 #储存前一下标
                list.append(j)                 #储存后一下标
            else:
                continue
    return list

#思路二：用target减去取出的元素，查看剩下的元素是否在数组中
class Solution:
    def twoSum(self,nums,target):
        for x in range(len(nums)):
            value = target - nums[x]
            if value in nums:
                y = nums.index(value)
                if x == y:   #判断元素下标是否相同
                    continue
                else:
                    return x,y
            break
#思路三 哈希表
#Python
def twoSum1(nums, target):
    hashmap = {}
    for  i, value in enumerate(nums):
        d = target - value
        if d in hashmap:
            return [hashmap.get(d), i]
        hashmap[value] = i

nums = [2, 7, 11, 15]
target = 9
# Solution()
# print(Solution().twoSum(nums,target))
print(twoSum1(nums, target))