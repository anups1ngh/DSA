class Solution:
    def average(self, salary: List[int]) -> float:
        if len(salary) < 2:
            return salary
        maxi = max(salary)
        mini = min(salary)
        salary.remove(maxi)
        salary.remove(mini)
        ans = sum(salary)
        return ans/len(salary)