class Solution:
    def decodeString(self, s: str) -> str:
        #stack to store the input so we can pop and perform operations
        #currnum to store the number of times the bracketed string should be repeated
        #curr_string stores the temp string that needs to be repeated
        stack=[]; currnum=0; curr_string=''
        
        for c in s:
            
            #if the character is open brace then push the already existing string which we have and also number if any and initialize them for other operations
            if c=='[':
                stack.append(curr_string)
                stack.append(currnum)
                curr_string=''
                currnum=0
            
            #if close brace compute the operation i.e string multiplication
            elif c==']':
                #first pop would be a number as we pushed number last 
                num = stack.pop()
                #prev string is the remaining string 
                prevString = stack.pop()
                
                #updated string
                curr_string = prevString + num*curr_string
            
            #if number then store it. This logic helpful if number is two or more digits 
            elif c.isdigit():
                currnum=currnum*10+int(c)
            
            #base case that c is a character in this case store it to push it into stack
            else:
                curr_string +=c
        
        return curr_string
