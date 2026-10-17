class Solution:
    def scoreOfString(self, s: str) -> int:
        contador1, contador2, suma = 0, 0, 0
        for i in range(0, len(s)-1):
            contador1 = ord(s[i])
            contador2 = -ord(s[i + 1])
            suma += abs(contador1 + contador2)
        return suma