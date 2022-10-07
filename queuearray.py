import sys
from array import *
queue=array('i',[])
def enqueue():
    element=int(input("enter the element:"))
    queue.append(element)
    print(element,"is added to your queue")
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print("removed element is",e)
def display():
    print("the elements in the queue is")
    for i in queue:
        print(i)
while True:
    print("1.add 2.delete 3.display 4.exit")
    ch=int(input("enter your choice:"))
    if ch==1:
        enqueue()
    elif ch==2:
        dequeue()
    elif ch==3:
        display()
    elif ch==4:
        sys.exit()
    else:
        print("enter correct option")
        