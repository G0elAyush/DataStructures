from linkedList import linkedList
from linkedListNode import linkedListNode
import random
'''
	function to insert the given data in the sorted linked list
'''
def orderedInsert(linkedList,data):
	newNode=linkedListNode(data)
	node=linkedList.head
	if not node:
		linkedList.head=newNode
		return
	last=None	
	while node and node.data < data:
		last=node
		node=node.next
	last.next=newNode
	newNode.next=node

if __name__=='__main__':
	myLinkedList=linkedList()
	myLinkedList.buildLinkedList();
	print(myLinkedList)
	data=random.randint(0,100)
	orderedInsert(myLinkedList,data)
	print(myLinkedList)
	