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
def isLinkedListLengthEven(linkedList):
	node=linkedList.head
	while node:
		if not node or not node.next:
			return False
		node = node.next.next
	return True
if __name__=='__main__':
	myLinkedList=linkedList();
	myLinkedList.buildLinkedList()
	print(myLinkedList)
	print("Given list is Even = "+ str(isLinkedListLengthEven(myLinkedList)))
	node=getMiddleOfList(myLinkedList)
	if node:
		print("Middle of given list = " + str(node.data))