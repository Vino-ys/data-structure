# 예제. n!을 구하는 함수를 재귀함수로 작성하세요.

def fac(n):
    if n == 1: return 1
    return n * fac(n - 1)

n = int(input())
print(fac(n))