from linkedList import linkedList
'''
	function to find middle of linked List
'''
def getMiddleOfList(linkedList):
	fast=linkedList.head
	slow=fast
	while fast:
		fast=fast.next
		if not fast:
			return slow
		fast=fast.next
		if not fast:
			return slow
		slow=slow.next
if __name__=='__main__':
	myLinkedList=linkedList();
	myLinkedList.buildLinkedList()
	print(myLinkedList)
	node=getMiddleOfList(myLinkedList)
	if node:
		print("middle of given list = " + str(node.data))