class Solution(object):
    def twoSum(self, nums, target):
        # Diccionario para guardar {valor: Ã­ndice}
        vistos = {}
        
        # 'enumerate' nos da tanto el Ã­ndice (i) como el valor (num)
        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in vistos:
                return [vistos[complemento], i]
            vistos[num] = i
            