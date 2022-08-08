n=6
m=6

#if tower higher than 1 and even, the second player always win
def towerBreakers(n, m):
    if((m > 1) and (n % 2!=0)):
        return 1
    else:
        return 2


print(towerBreakers(n, m))