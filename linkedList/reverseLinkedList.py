from linkedList import linkedList
'''
	reverser a linked list using iteration
'''
def reverseLinkedListIteration(linkedList):
	node=linkedList.head
	last=None
	while node:
		tmp=node.next
		node.next=last
		last=node
		node=tmp
	linkedList.head=last
def reverseLinkedListRecursion(linkedList,node):
    if node:
        right=node.next
        if linkedList.head != node:
            node.next = linkedList.head
            linkedList.head = node
        else:
            node.next=None 
        reverseLinkedListRecursion(linkedList,right)
    
    
if __name__=='__main__':
    myLinkedList=linkedList()
    myLinkedList.buildLinkedList()
    print(myLinkedList)
    reverseLinkedListIteration(myLinkedList)
    print(myLinkedList)    
    reverseLinkedListRecursion(myLinkedList,myLinkedList.head)
    print(myLinkedList)