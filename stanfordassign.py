def is_Possible(p,pre):
    k=pre.copy()
    k=dict(k)
    a=k.keys()
    b=k.values()
    for i in pre:
        if i[::-1] in pre:
            return False 
    i=pre[0]
    while True:
        if len(pre)<=1:
            return True
        if i==pre[-1]:
            return False
        for i in pre:
            if i[1] not in a:
                pre.remove(i)
                k=pre.copy()
                k=dict(k)
                a=k.keys()
                b=k.values()
                break

n=int(input())
p=int(input())
li=[]
for i in range(p):
    li.append(list(map(int,input().split())))
li.sort()
if is_Possible(p,li):
    print("Valid")
else:
    print("Invalid")

