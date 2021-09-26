from linkedListNode import linkedListNode
import random
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
    def buildLinkedList(self):
        lst=[]
        num=int(input("enter length of list to populate\n"))
        for i in range(num):
            lst.append(random.randint(1,100))
        node=None
        for i in range(len(lst)):
            if i==0:    
                self.head=linkedListNode(lst[i])
                self.len+=1
                node=self.head
            else:
                node.next=linkedListNode(lst[i])
                self.len+=1
                node=node.next
if __name__=='__main__':
    myLinkedList=linkedList()
    myLinkedList.buildLinkedList()
    print(myLinkedList)

