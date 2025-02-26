def subSum(idx1, idx2, arr):
    si = min(idx1,idx2)
    ei = max(idx1,idx2)
    if( 0 <= ei and si == 0 ):
        return arr[ei]
    else:
        return arr[ei] - arr[si-1]

for t in range(int(input())):
    arr=list(map(int,input().split()))
    n = len(arr)
    lpfx = [0]*n
    rpfx = [0]*n
    lmin, lni, lmax, lmi  = 1000000007, 0, -1000000007, 0
    rmin, rni, rmax, rmi = 1000000007, 0, -1000000007, 0

    for i in range(n):
        print(i)
        lpfx[i] = lpfx[i-1] + arr[i]
        if(lmin >= lpfx[i]):
            lmin = lpfx[i]
            lni = i
        if(lmax <= lpfx[i]):
            lmax = lpfx[i]
            lmi = i
        rpfx[n-i-1] = rpfx[(n-i)%n] + arr[n-i-1]
        if(rmin >= rpfx[n-i-1]):
            rmin = rpfx[n-i-1]
            rni = n-i-1
        if(rmax <= rpfx[n-i-1]):
            rmax = rpfx[n-i-1]
            rmi = n-i-1
    print(lmin, lni, lmax, lmi)
    print(rmin, rni, rmax, rmi)
    print(lpfx, rpfx)

    #postive
    pans = abs(subSum(lmi,rmi,lpfx))
    nans = abs(subSum(lni,rni,lpfx))

    print(max(pans,nans))

    