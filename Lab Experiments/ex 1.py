from collections import deque

s=(1,2,3,4,0,6,7,5,8)
g=(1,2,3,4,5,6,7,8,0)

q=deque([(s,0)])
v={s}

while q:
    x,c=q.popleft()
    print(x)

    if x==g:
        print("Total Cost:",c)
        break

    z=x.index(0)

    for n in [z-3,z+3,z-1,z+1]:
        if 0<=n<9 and abs(z%3-n%3)<=1:
            a=list(x)
            a[z],a[n]=a[n],a[z]
            t=tuple(a)

            if t not in v:
                v.add(t)
                q.append((t,c+1))
