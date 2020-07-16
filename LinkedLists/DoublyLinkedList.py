class Node:
    def __init__(self):
        self.val = None
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.root = None
        self.tail = None
        self.n = 0

    def printList(self, name):
        t = self.root
        print(name)
        while(t != None):
            print(t.val, end=" ")
            t = t.next
        print()

    def get(self, index: int) -> int:
        if index >= self.n:
            return -1
        else:
            t = self.root
            c = 0
            while(c < index):
                t = t.next
                c += 1

            return t.val

    def addAtHead(self, val: int) -> None:
        node = Node()
        node.val = val
        if(self.root == None):
            self.tail = node
            self.root = node
        else:
            node.next = self.root
            self.root.prev = node
            self.root = node
        self.n += 1

    def addAtTail(self, val: int) -> None:
        node = Node()
        node.val = val
        node.next = None
        if(self.root == None):
            self.root = node
            self.tail = node
            self.n += 1
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.n += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if(index <= self.n):
            if(index == self.n):
                self.addAtTail(val)
                return
            if(index == 0):
                self.addAtHead(val)
                return
            node = Node()
            node.val = val
            t = self.root
            c = 0
            while(c < index-1):
                t = t.next
                c += 1
            node.next = t.next
            node.prev = t
            t.next.prev = node
            t.next = node
            self.n += 1

    def deleteAtIndex(self, index: int) -> None:
        p = None
        if(index < self.n):
            if(index == 0):
                self.root = self.root.next
                # self.root.prev=None
                self.n -= 1
                return
            if(index == self.n-1):
                self.tail = self.tail.prev
                self.tail.next = None
                '''p=self.root
                while(p.next!=self.tail):
                    p=p.next
                self.tail=p
                self.tail.next=None'''
                self.n -= 1
                return
            t = self.root
            c = 0
            while(c < index):
                p = t
                t = t.next
                c += 1
            p.next = t.next
            t.next.prev = p
            self.n -= 1
