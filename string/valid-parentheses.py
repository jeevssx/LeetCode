class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        hashMap = {'(' : ')', '[' : ']', '{' : '}'}

        newStack = []

        for symbol in s:

            if symbol in hashMap.keys():
                newStack.append(symbol)
            else:
                if not newStack:
                    return False
                temporary = newStack.pop()
                if symbol != hashMap[temporary]:
                    return False
        return newStack == []

        
