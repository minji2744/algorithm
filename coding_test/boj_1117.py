W,H,f,c,x1,y1,x2,y2 = map(int, input().split())

if W//2 >= f > x1:
    if x2 >= f:
        print(W*H - ((x2-x1)*(y2-y1)+(f-x1)*(y2-y1)) * (c+1))
    else:
        print(W*H - (x2-x1)*(y2-y1)*(c+1)*2)
elif f > W//2:
    x3 = W-f
    if x1 >= x3:
        print(W*H - (x2-x1)*(y2-y1)*(c+1))
    else:
        if x2 > x3:
            print(W*H - ((x3-x1)*(y2-y1)*(c+1)*2 + (x2-x3)*(y2-y1)*(c+1)))
        else:
            print(W*H - (x2-x1)*(y2-y1)*(c+1)*2)
else:
    print(W*H - ((x2-x1)*(y2-y1)) * (c+1))