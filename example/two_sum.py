from typing import List, Optional

# import debugpy
# debugpy.listen(5678)
# debugpy.wait_for_client()

class Solution:
    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):  # Inspect variables:  bug 1: As the target indexes should be distinct so i and j should not be the same -> j should not start at i
                # for j in range(i + 1, len(nums)): 
                if nums[i] - nums[j] == target:  # Watch the expression: bug 2: We should find the program by nums[i] + nums[j] instead of nums[i] - nums[j] -> watch the express can help you observe and debug
                # if nums[i] + nums[j] == target:
                    return [i, j]
        return None

# import pytest
# @pytest.fixture()
# def solution() -> None:
#     return Solution()


# def testcase1(solution):
#     s = solution
#     res = s.twoSum([11, 7, 2, 15], 9)
#     print("ans: {0}".format(res))
#     assert res == [1, 2] or res == [2, 1]


# def testcase2(solution):
#     s = solution
#     res = s.twoSum([3, 3, 1, 5], 6)
#     print("ans: {0}".format(res))
#     assert res == [0, 1] or res == [1, 0]


# def testcase3(solution):
#     s = solution
#     res = s.twoSum([3, 3], 6)
#     print("ans: {0}".format(res))
#     assert res == [0, 1] or res == [1, 0]


# def testcase4(solution):
#     s = solution
#     res = s.twoSum([1, 1], 6)
#     print("ans: {0}".format(res))
#     assert res == None

if __name__ == '__main__':
    s = Solution()
    res = s.twoSum([11, 7, 2, 15], 9)
    print("ans: {0}".format(res))
    assert res == [1, 2] or res == [2, 1]

    s = Solution()
    res = s.twoSum([3, 2, 1, 3], 6)
    print("ans: {0}".format(res))
    assert res == [0, 3] or res == [3, 0]

    s = Solution()
    res = s.twoSum([3, 3], 6)
    print("ans: {0}".format(res))
    assert res == [0, 1] or res == [1, 0]

    s = Solution()
    res = s.twoSum([1, 1], 6)
    print("ans: {0}".format(res))
    assert res == None
