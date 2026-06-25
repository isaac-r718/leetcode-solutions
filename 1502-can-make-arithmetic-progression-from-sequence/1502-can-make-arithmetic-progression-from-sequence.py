class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        arr_length = int(len(arr))
        sub_list = []
        for i in range(arr_length - 1):
            sub = arr[i] - arr[i+1]
            sub_list.append(sub)
        first_num = sub_list[0]
        factor = all(i == first_num for i in sub_list)
        return factor