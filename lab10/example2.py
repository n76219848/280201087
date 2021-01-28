def hailstone(x):
    if x==1:
        c=1
        return [c]
    elif x%2==0:
        c= x/2
    elif x%2!=0:
        c= 3*x+1
    return [int(x)]+(hailstone(c))


print(hailstone(11))
