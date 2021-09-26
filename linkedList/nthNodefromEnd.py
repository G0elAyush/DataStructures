from linkedList import linkedList
import random
def nthNodeFrmEnd(linkedList):
    n=int(input("enter the required node number from end\n"))
    fast=linkedList.head
    count=1
    while fast and count < n:
        fast=fast.next
        count+=1
    if not fast  or count < n:
        return "required node does not exist"
    slow=linkedList.head
    while fast.next:
        fast=fast.next
        slow=slow.next
    return slow.data

if __name__=='__main__':
    lst=[]
    num=int(input("enter length of list to populate\n"))
    for i in range(num):
        lst.append(random.randint(1,100))
    myLinkedList=linkedList()
    myLinkedList.buildLinkedList(lst)
    print("the list created is - ")
    print(myLinkedList)
    print(nthNodeFrmEnd(myLinkedList))
