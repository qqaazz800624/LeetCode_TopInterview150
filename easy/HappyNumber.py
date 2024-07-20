#%% Floyd's Tortoise and Hare (Cycle Detection) Algorithm

class Solution:
    def getNext(self, number: int) -> int:
        totalSum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            totalSum += digit ** 2
        return totalSum
    
    def isHappy(self, n: int) -> bool:
        slowRunner = n
        fastRunner = self.getNext(n)
        while fastRunner != 1 and slowRunner != fastRunner:
            slowRunner = self.getNext(slowRunner)
            fastRunner = self.getNext(self.getNext(fastRunner))
        return fastRunner == 1

#%% Cycle Detection with set()

class Solution:
    def getNext(self, number: int) -> int:
        totalSum = 0
        while number > 0:
            digit = number % 10
            totalSum += digit ** 2
            number = number // 10
        return totalSum
    
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.getNext(n)
        return n == 1

#%%






#%%





#%%