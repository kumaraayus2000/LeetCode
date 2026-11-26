class Solution:
    def canAliceWin(self, n: int) -> bool:
        coins = 10 

        alice_turn = True

        while n>=coins:

            n = n - coins

            coins -=1

            alice_turn = not alice_turn

        return not alice_turn