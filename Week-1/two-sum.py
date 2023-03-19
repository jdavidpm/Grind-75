def twoSum(nums, target):
        my_hash = {num: index for index, num in enumerate(nums)}
        actual_index = 0
        for item in nums:
            if ((target - item) in my_hash and my_hash[target - item] is not actual_index):
                return [my_hash[target - item], actual_index]
            actual_index += 1
