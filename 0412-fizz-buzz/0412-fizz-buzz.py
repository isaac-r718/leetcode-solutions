class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(n):
            num = i+1
            if num % 15 == 0:
                answer.append('FizzBuzz')
            elif num % 3 == 0:
                answer.append('Fizz')
            elif num % 5 == 0:
                answer.append('Buzz')
            else:
                answer.append(str(num))
        return answer