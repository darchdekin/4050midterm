class Solution:
    def numSplits(self, s: str) -> int: 
        Rmap = [0] * 26;
        Lmap = [0] * 26;
        Rchars = 0;
        Lchars = 0;
        result = 0;
     
        for c in s:
            if Rmap[ord(c)-97] == 0:
                Rchars += 1
            Rmap[ord(c)-97] += 1
                
        for x in s:
            if Lmap[ord(x)-97] == 0:
                Lchars += 1
            Lmap[ord(x)-97] += 1      #add to left map
            if Rmap[ord(x)-97] == 1:
                Rchars -= 1
            Rmap[ord(x)-97] -= 1       #decrement proper place in Rmap
            if Rchars == Lchars:
                result+=1                    
        
        return result