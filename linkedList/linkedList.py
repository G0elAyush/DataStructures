from linkedListNode import linkedListNode
class linkedList:
    '''
    declare constructor
    '''
    def __init__(self):
        self.head=None
        self.len=0
    '''
    override str method to print the list
    '''
    def __str__(self):
        self.printList()
        return ""
    '''
    define function to print the list
    '''
    def printList(self):
        node=self.head
        while node:
            print(node.data,end=" ")
            node=node.next
    '''
    define function to build linked list from input
    '''
    def buildLinkedList(self,lst):
        node=linkedListNode(lst.pop(0))
        self.head=node
        self.len+=1
        while lst:
            node.next=linkedListNode(lst.pop(0))
            myLinkedList.len+=1
            node=node.next
if __name__=='__main__':
    lst=input("enter the list, eg 1 2 3 4 5 6 7 8\n")
    lst=list(lst.strip().split(" "))
    myLinkedList=linkedList()
    myLinkedList.buildLinkedList(lst)
    print(myLinkedList)

