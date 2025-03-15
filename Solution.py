n=int(input());arr=[int(i) for i in input().strip().split()];sm=0
for i in range(n-1):
    for j in range(i+1,n):
        x=sum(arr[i:j+1])
        if x>sm:
            sm=x
print(sm)
