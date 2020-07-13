class Node:
    """
    Class definition for each node in the linked list
    val  : Data held in node
    next : Pointer to next node 
    """

    def __init__(self):
        self.val = None
        self.next = None


class MyLinkedList:
    """
    Class defnition of the actual Linked List
    head : Head of the list
    tail : Tail of the list
    n    : Number of nodes in the list
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def printList(self, name):
        """
        Prints the values held in the linked list in order
        """
        t = self.head
        print(name)
        while(t != None):
            print(t.val, end=" ")
            t = t.next
        print()

    def get(self, index: int) -> int:
        """
        Gets an element at a particular index
        returns -1 incase of invalid index 
        """
        if index >= self.n:
            return -1
        else:
            t = self.head
            c = 0
            while(c < index):
                t = t.next
                c += 1

            return t.val

    def addAtHead(self, val: int) -> None:
        """
        Add an element to the head of the list
        """
        node = Node()
        node.val = val
        if(self.head == None):
            self.tail = node
        node.next = self.head
        self.head = node
        self.n += 1

    def addAtTail(self, val: int) -> None:
        """
        Adds an element to the tail of the list
        """
        node = Node()
        node.val = val
        node.next = None
        if(self.head == None):
            self.head = node
            self.tail = node
            self.n += 1
            return
        self.tail.next = node
        self.tail = node
        self.n += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Adds an element at a particular index
        Does nothing incase of an invalid index 
        """
        if(index <= self.n):
            if(index == self.n):
                self.addAtTail(val)
                return
            if(index == 0):
                self.addAtHead(val)
                return
            node = Node()
            node.val = val
            t = self.head
            c = 0
            while(c < index-1):
                t = t.next
                c += 1
            node.next = t.next
            t.next = node
            self.n += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Deletes an element at a particular index
        Does nothing incase of an invalid index 
        """
        p = None
        if(index < self.n):
            if(index == 0):
                self.head = self.head.next
                self.n -= 1
                return
            if(index == self.n-1):
                p = self.head
                while(p.next != self.tail):
                    p = p.next
                self.tail = p
                self.tail.next = None
                self.n -= 1
                return
            t = self.head
            c = 0
            while(c < index):
                p = t
                t = t.next
                c += 1
            p.next = t.next
            self.n -= 1
