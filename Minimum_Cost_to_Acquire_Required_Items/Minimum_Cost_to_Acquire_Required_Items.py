class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if costBoth > cost1 + cost2:
            costBoth = cost1 + cost2
        if need1 > need2:
            need1, need2, cost2 = need2, need1, cost1
        
        if cost2 > costBoth:
            cost2 = costBoth

        return costBoth * need1 + cost2 * (need2 - need1)