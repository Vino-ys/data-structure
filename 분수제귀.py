# 3. 1 + 1/2 + 1/3 + ..... + 1/n을 구하는 함수를 재귀함수로 작성하세요.
def bun(n):
    if n == 1 : return 1
    return 1 / n + bun(n - 1)

n = int(input())

print(bun(n)) # ex)3 1 + 1/2 1/3 0.3333 0.5 1  = 1.8333333