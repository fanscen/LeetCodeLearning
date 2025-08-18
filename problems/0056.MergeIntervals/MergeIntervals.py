class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        sol = []
        intervals.sort(key= lambda x:x[0])
        for interval in intervals:
            if not sol or sol[-1][1] < interval[0]:
                sol.append(interval)
            else:
                sol[-1][1] = max(sol[-1][1],interval[1])
        return sol 


if __name__ == "__main__":
    mac = Solution()
    print(mac.merge([[1,3],[2,6],[8,10],[15,18]]))