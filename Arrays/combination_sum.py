#__author__ = ritvikareddy2
#__date__ = 2019-02-20'


# can reuse same element more than once
def combinationSum1(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    def dfs(nums, target, index, path):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if nums[i] > target:
                break
            dfs(nums, target - nums[i], i, path + [nums[i]])

    res = []
    candidates.sort()
    dfs(candidates, target, 0, [])
    return res


# unique numbers
def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    def dfs(nums, target, index, path):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            if nums[i] > target:
                break
            dfs(nums, target - nums[i], i+1, path + [nums[i]])

    res = []
    candidates.sort()
    dfs(candidates, target, 0, [])
    return res


# dynamic programming soln
def combinationSum2_dp(candidates, target):
    candidates.sort()
    dp = [set() for i in range(target + 1)]
    dp[0].add(())
    for num in candidates:
        for t in range(target, num - 1, -1):
            for prev in dp[t - num]:
                dp[t].add(prev + (num,))
    return list(dp[-1])


def combinationSum3(k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """

    def dfs(nums, target, index, path):
        if target < 0:
            return  # backtracking
        if target == 0 and len(path) == k:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target or len(path) >= k:
                break
            dfs(nums, target - nums[i], i + 1, path + [nums[i]])

    res = []

    dfs(range(1, 10), n, 0, [])
    return res


if __name__ == '__main__':
    print(combinationSum1([2, 3, 6, 7], 7))
    print(combinationSum2([2, 3, 6, 7], 7))
    print(combinationSum2_dp([2, 3, 6, 7], 7))
    print(combinationSum3(3, 7))

