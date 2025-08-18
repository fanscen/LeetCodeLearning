class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        downEdge = len(board)
        rightEdge = len(board[0])
        selected = []
        sol = False
        
        lsts = []
        for lst in board:
            lsts += lst
        lstWord = list(word)
        isExst = True
        for ch in lstWord:
            if ch not in lsts:
                isExst = False
                break
        if isExst == False:
            return sol 
        
        for i in range(downEdge):
            for j in range(rightEdge):
                sol = self.search(i,j,board,list(word),selected)
                if sol == True: break
            if sol == True: break
        return sol
    
    def search(self,i,j,board: list[list[str]],word:list,selected:list) ->bool:
        downEdge = len(board)
        rightEdge = len(board[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        sol = False
        if [i,j] in selected:
            return sol
        if board[i][j] == word[0]:
            selected.append([i,j])
            if len(word) == 1:
                return True
            for direction in directions:
                if [i + direction[0],j + direction[1]] not in selected \
                    and i + direction[0] >=0 and i + direction[0] < downEdge \
                    and j + direction[1] >=0 and j + direction[1] < rightEdge:
                    sol = self.search(i + direction[0],j + direction[1],board,word[1:],selected)
                if sol == True:
                    break
            selected.remove([i,j])
        return sol

if __name__ == "__main__":
    mac = Solution()
    print(mac.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]],
"AAAAAAAAAAAABAA"))