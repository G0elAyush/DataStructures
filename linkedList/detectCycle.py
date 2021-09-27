from linkedList import linkedList
import random
'''
    this function create a loop in snake type linked list randomly
'''
def createLoop(linkedList):
    print("creating loop in the linked list")
    num=random.randint(1,linkedList.len-1)
    print("num="+str(num))
    node=linkedList.head
    for i in range(1,num):
        node=node.next
    tmp=node
    tmp.data="loopStart="+str(tmp.data)
    while node.next:
        node=node.next
    node.next=tmp
    node.data=None
    print("the loop list created is - ")
    node=linkedList.head
    while node.data != None:
        print(node.data,end=" ")
        node= node.next
    print("loopEnd="+str(node.data))
    print("\n")
''' function detect if the given linked list is null terminated or there exist a loop.
    If there is is a loop it returns the start node and size of loop
'''
def detectCycle(linkedList):
    slow=linkedList.head
    if not slow or not slow.next:
        return "No cycle detected"
    slow=slow.next
    fast=slow.next
    while slow != fast:
        if not fast:
            return "No cycle detected"
        fast = fast.next
        if not fast:
            return "No cycle detected"
        fast = fast.next
        slow=slow.next
    slow=slow.next
    looplen=1
    while slow != fast:
        slow=slow.next
        looplen+=1
    slow=linkedList.head
    while slow != fast:
        slow=slow.next
        fast=fast.next
    return "Cycle detected. Starts at node "+ str(slow.data) + " with loop length "+ str(looplen)
        
if __name__=='__main__':
    myLinkedList=linkedList()
    myLinkedList.buildLinkedList()
    print(myLinkedList)
    print(detectCycle(myLinkedList))
    createLoop(myLinkedList)
    print(detectCycle(myLinkedList))
