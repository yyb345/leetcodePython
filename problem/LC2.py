from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# 添加 main 方法进行测试
def main():
    solution = Solution()

    # 测试用例 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print(f"Test case 1: nums = {nums1}, target = {target1} -> result = {result1}")

    # 测试用例 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(f"Test case 2: nums = {nums2}, target = {target2} -> result = {result2}")

    # 测试用例 3
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    print(f"Test case 3: nums = {nums3}, target = {target3} -> result = {result3}")


if __name__ == "__main__":
    main()
