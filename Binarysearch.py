def binarysearch(l,low,high,key):
    while low<=high:
        mid=(low+high)//2
        if l[mid]==key:
            return mid
        elif l[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return -1
lst=[]
num=int(input("enter no of elements:"))
l=0
h=num-1
for i in range(num):
    ele=int(input("enter element:"))
    lst.append(ele)
key=int(input("enter element to be found:"))
result=binarysearch(lst,l,h,key)
if result==-1:
    print("element not found")
else:
    print("element found at index:",result)