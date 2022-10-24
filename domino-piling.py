def rectfilldomino():
    row,col = map(int,input().split())
    mult = row * col
    maxnum = mult//2
    return maxnum


print(rectfilldomino())
