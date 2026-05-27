# 1. 피보나치 수열의 n번째 항을 구하는 재귀함수를 작성하세요.

# 피보나치 수열 : 1, 1, 2, 3, 5, 8, 13.... 과 같이 이전 항의 합으로 구성

def fib(n):
    if n == 1 or n == 2: return 1
    return fib(n - 1) + fib(n - 2)

n = int(input())
print(fib(n))