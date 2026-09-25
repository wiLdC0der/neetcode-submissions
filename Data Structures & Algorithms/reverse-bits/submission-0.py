class Solution:
    def reverseBits(self, n: int) -> int:

        temp = f"{n:032b}"
        reversed_n = temp[::-1]
        ans = int(reversed_n,2)
        return ans


        