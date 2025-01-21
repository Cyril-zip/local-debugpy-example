import debugpy
debugpy.listen(5678)
debugpy.wait_for_client()

class Solution:
    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1

        # Bug 1: Off-by-One Error: The function might skip evaluating the final element in certain cases.
        while left <= right:
            # while left <= right: # This is the correct code
            # Bug 2: Incorrect mid Calculation: This skews the mid calculation, especially in edge cases with small arrays.
            mid = (left + right + 1) // 2
            # mid = (left + right) // 2 # This is the correct code
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # return -1 # This is the correct code  
        # # Bug 3: Missing Edge Case Handling

    # Observe the call stack 
    def binary_search_recursive(self, nums, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_search_recursive(nums, target, mid + 1, right)
        else:
            return self.binary_search_recursive(nums, target, left, mid - 1)


if __name__ == '__main__':
    s = Solution()
    res = s.binary_search([1, 2, 3, 4, 5], 5)
    print("ans: {0}".format(res))
    assert res == 4

    s = Solution()
    res = s.binary_search([1, 2], 1)
    print("ans: {0}".format(res))
    assert res == 0

    s = Solution()
    res = s.binary_search([3, 3], 6)
    print("ans: {0}".format(res))
    assert res == -1

    s = Solution()
    nums = list(range(1, 1000001))  # Array from 1 to 1,000,000
    target = 999999
    res = s.binary_search_recursive(nums, target, 0, len(nums) - 1)
    print("ans: {0}".format(res))
    assert res == 999998
