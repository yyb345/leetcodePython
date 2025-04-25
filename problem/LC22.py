from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        self.dfs(0, 0, "", n, res)
        return res

    def dfs(self, left, right, s, n: int,res):

        if left > n or right > n or right > left:
            return

        if left == n and right == n:
            res.append(s)
            return

        self.dfs(left + 1, right, s + "(", n,res)
        self.dfs(left, right + 1, s + ")", n,res)


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(2))
