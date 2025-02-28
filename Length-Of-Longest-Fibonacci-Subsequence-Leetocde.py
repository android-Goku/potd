for t in range(int(input())):
    arr=list(map(int,input().split()))
    n=len(arr)
    s=set(arr)
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            a = arr[j]
            b = arr[i] + arr[j]
            l = 2

            while b in s:
                c = a + b
                a = b
                b = c
                l += 1
                ans = max(ans, l)
    print (ans if (ans >=3) else 0)