m = []
n = {}
for a in range(1,7):
    for b in range(1,7):
        for c in range(1,7):
            for d in range(1, 7):
                for e in range(1, 7):
                    for f in range(1, 7):
                        m.append(a+b+c+d+e+f)
for z in range(6,37):
    n[z]=0
for i in m:
    n[i]+=1
print(m)
print(n)
for i in n:
    print(str(i)+";"+str(n[i]))