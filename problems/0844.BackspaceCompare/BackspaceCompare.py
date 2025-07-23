class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s: str) -> str:
            stack = []
            for c in s:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        
        return build(s) == build(t)

if __name__ == '__main__':
    s = Solution()
    print(s.backspaceCompare('ab#c', 'ad#c'))
    print(s.backspaceCompare('ab##', 'c#d#'))
    print(s.backspaceCompare('a#c', 'b'))