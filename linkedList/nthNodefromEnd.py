from linkedList import linkedList
''' This funciton return the nth node from the end of the linked list.
    return "required node does not exist" if such node does not exist"
'''
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
    myLinkedList=linkedList()
    myLinkedList.buildLinkedList()
    print("the list created is - ")
    print(myLinkedList)
    print(nthNodeFrmEnd(myLinkedList))
