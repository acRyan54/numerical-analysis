m = int(eval(input()))
for n in range(m, m+20):
    a = [1]
    alpha = []
    for i in range(1, n+10):
        ai = a[i-1] + a[(i-1)//2]
        a.append(ai)
    k = (a[n+1]-a[n])/(a[n]-a[n-1])
    print(k)