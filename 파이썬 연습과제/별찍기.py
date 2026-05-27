def asterisk(n):
    if n >= 1:
        asterisk(n//2)
        asterisk(n//2)
    print('*', end = "")

asterisk(3) # 7개

#다음 시간에 발표 난 아닐수도 있지만