# 2. a의 n 제곱을 구하는 함수를 재귀함수로 작성하세요.

def gg(a,n):
    if n == 1: return a
    return a * gg(a,n - 1)

a = int(input('a'))
n = int(input('n'))
gg(a,n)