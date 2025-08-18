class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) <=2:
            return 0

        max_height = max(height)
        max_index = height.index(max_height)
        if max_index == 0:
            result = self.trapright(height[1:])
        elif max_index == len(height) -1:
            result = self.trapleft(height[:max_index])
        result = self.trapleft(height[:max_index]) + self.trapright(height[max_index+1:])
        return result

    def trapleft(self,height: list[int]) -> int:
        if len(height) <=1:
            return 0
        secmax_height = max(height)
        secmax_index = height.index(secmax_height)
        i = secmax_index + 1
        result = 0
        while i < len(height):
            result = result + secmax_height - height[i] 
            i = i + 1
        if secmax_index > 0:
            return result + self.trapleft(height[:secmax_index])
        else : return result

    def trapright(self,height: list[int]) -> int:
        if len(height) <= 1:
            return 0
        secmax_height = max(height)
        secmax_index = height.index(secmax_height)
        i = 0
        result = 0
        while i < secmax_index:
            result = result + secmax_height - height[i]
            i = i + 1
        if secmax_index < len(height) - 1:
            return result + self.trapright(height[secmax_index + 1:])
        else : return result

if __name__ == "__main__":
    mac = Solution()

#    print(mac.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
#    print(mac.trap([4,2,0,3,2,5]))
    print(mac.trap([2,0,2]))