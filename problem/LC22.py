from typing import List


class Solution:
    res = []
    def generateParenthesis(self, n: int) -> List[str]:

        self.dfs(0, 0, "",n)
        return self.res

    def dfs(self,openP, closeP, s,n:int):
        if openP == closeP and openP + closeP == n * 2:
            self.res.append(s)
            return

        if openP < n:
            self.dfs(openP + 1, closeP, s + "(",n)

        if closeP < openP:
            self.dfs(openP, closeP + 1, s + ")",n)


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))