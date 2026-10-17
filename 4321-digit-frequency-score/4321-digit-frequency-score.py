class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        final = 0
        lista = [0]*10
        digitos = [int(d) for d in str(n)]
        for i in range(len(digitos)):
            lista[digitos[i]] += 1
        for i in range(10):
            final += i * lista[i]
        return final