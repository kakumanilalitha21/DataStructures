def mergesort(lst):
    if len(lst) > 1:
 
         
        mid = len(lst)//2
        L = lst[:mid]
 
        R = lst[mid:]
        mergesort(L)
        mergesort(R)
 
        i = 0
        j =0
        k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1
    return lst
n=int(input("enter no of elements:"))
l=[]
for i in range(n):
    ele=int(input("enter element:"))
    l.append(ele)
print(mergesort(l))    
 
