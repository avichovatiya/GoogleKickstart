x = int(input())
for j in range(x):
    (N,M)= tuple(map(int, input().split()))
    C = list(map(int, input().split()))
    candy=0 
    for k in range(N):
        candy+=C[k]
    rc = candy%M
    print("Case #"+str(j+1)+":",rc)
