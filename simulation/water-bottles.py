class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    
        maxWaterBottles = numBottles

        while numBottles >= numExchange:
            newBottles = numBottles // numExchange

            maxWaterBottles += newBottles

            numBottles = newBottles + (numBottles % numExchange)


        return maxWaterBottles

