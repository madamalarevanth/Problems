
END_MARK, VISITED = '*', float('inf')

class Trie:
    def __init__(self,char):
        self.char = char
        self.adjacentChars = {}

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {} # Space O(K * L)
        
        #for all the words in the list
        for word in words: # Time O(K * L)
            #if 1st char in word is not in trie 
            if not word[0] in trie:
                #make a node with that char
                trie[word[0]] = Trie(word[0])
            #move current pointer to that node
            node = trie[word[0]]
            
            #for all the remaining chars in the word
            for char in word[1:]:
                #construct trie by adding them as adjacent chars to the current char
                if not char in node.adjacentChars:
                    node.adjacentChars[char] = Trie(char)
                #move the pointer accordingly
                node = node.adjacentChars[char]
            #mark the end of word
            node.adjacentChars[END_MARK] = None
            
        #xLimit, yLimit = len(board),len(board[[0]])
        output = set()
    
        def backtracking(x,y,node,res):
            nonlocal xLimit, yLimit, output
            
            #marks the end of 0word
            if END_MARK in node.adjacentChars:
                output.add(res)
            
            curChar = board[x][y]
            board[x][y] = VISITED
            #node.adjacentChars.items() gives each item in format of dict_items([('a', <__main__.Trie object at 0x7f92accb6220>)])
            #neighbor => 'a' char, nextNode => node instance
            for neighbor, nextNode in node.adjacentChars.items():
                # Down, up, left and right
                for nextX, nextY in {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}:
                    if 0 <= nextX < xLimit and 0 <= nextY < yLimit and board[nextX][nextY] == neighbor:
                        backtracking(nextX, nextY, nextNode, res + neighbor)
            board[x][y] = curChar          
                        
        xLimit, yLimit = len(board),len(board[0])
        for x in range(xLimit): # Time O(N * M * 3 ^ L)
            for y in range(yLimit):
                curChar = board[x][y]
                if curChar in trie:
                    # Backtracking depth will be L, avg word length
                    backtracking(x, y, trie[curChar], curChar)
        return output
