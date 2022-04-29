def findWords(board, words):
    res = []
    rowLen = len(board)
    colLen = len(board[0])

    def safeToVisit(r, c, w, currIndex, visited):
        # if currIndex == len(w):
        #     return True
        if r >= 0 and r < rowLen and c >= 0 and c < colLen and (r, c) not in visited and board[r][c] == w[currIndex] :
            return True
        return False

    def dfs(row, col, w, currIndex, visited):
        nonlocal rowLen
        nonlocal colLen
        visited.add((row, col))
        currIndex+=1
        if currIndex == len(w):
            return True
        if (safeToVisit(row + 1, col, w, currIndex, visited)):
            if dfs(row + 1, col, w, currIndex, visited):
                return True
        if (safeToVisit(row - 1, col, w, currIndex, visited)):
            if dfs(row - 1, col, w, currIndex, visited):
                return True
        if (safeToVisit(row, col - 1, w, currIndex, visited)):
            if dfs(row, col - 1, w, currIndex, visited):
                return True
        if (safeToVisit(row, col + 1, w, currIndex, visited)):
            if dfs(row, col + 1, w, currIndex, visited):
                return True
        # visited.remove((row, col))
        return False

    for w in words:
        for i in range(rowLen):
            for j in range(colLen):
                if board[i][j] == w[0]:
                    visited = set()
                    if dfs(i, j, w, 0, visited):
                        res.append(w)
                        break
    return res

# board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
board = [["a","b","c"],["a","e","d"],["a","f","g"]]
words = ["eaabcdgfa", "abcdefg","gfedcbaaa"]
k = findWords(board, words)
print(k)

print (5/2)
print(-2 % 6)


