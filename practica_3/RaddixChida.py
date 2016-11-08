def radixSort(a,n,maxLen):
    for x in range(maxLen):
        bins = [[] for i in range(n)]
        for y in a:
            bins[(y/10**x)%n].append(y)
        a=[]
        for section in bins:
            a.extend(section)
    return a


Lista = [2345, 345, 1, 75345, 33, 34, 876]
print(radixSort(Lista, 10, 5))