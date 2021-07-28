for i in range(int(input())):
    l=list(map(str,input().split()))
    if len(l)==3:
        print(l[0][0].upper()+"."+l[1][0].upper()+"."+l[2][0].upper()+l[2][1:])
    elif len(l)==2:
        print(l[0][0].upper()+"."+l[1][0].upper()+l[1][1:])
    else:
        print(l[0][0].upper()+l[0][1:])

        
